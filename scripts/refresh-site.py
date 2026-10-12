#!/usr/bin/env python3
"""Rebuild embedded annual indicators and map from the packaged source files."""
import csv
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "source"

def annual_means(series_id: str) -> dict[int, float]:
    values: dict[int, list[float]] = defaultdict(list)
    with (SOURCE / f"{series_id}.csv").open(newline="") as stream:
        for row in csv.DictReader(stream):
            raw = row[series_id]
            if raw and raw not in {".", "NA"}:
                values[int(row["observation_date"][:4])].append(float(raw))
    return {year: round(sum(months) / 12, 3) for year, months in values.items() if len(months) == 12}

def annual_personal_income() -> dict[int, int]:
    path = SOURCE / "A792RC0A052NBEA.csv"
    with path.open(newline="") as stream:
        return {
            int(row["observation_date"][:4]): int(float(row["A792RC0A052NBEA"]))
            for row in csv.DictReader(stream)
            if row["A792RC0A052NBEA"] not in {"", ".", "NA"}
        }

def replace_between(document: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = document.index(start_marker) + len(start_marker)
    end = document.index(end_marker, start)
    return document[:start] + "\n" + replacement + "\n" + document[end:]

national_cpi = annual_means("CUUR0000SAF11")
income = annual_personal_income()
national = [
    {
        "year": year,
        "foodCpi": national_cpi[year],
        "income": income[year],
        "foodChangePercent": round((national_cpi[year] / national_cpi[year - 1] - 1) * 100, 2),
        "incomeChangePercent": round((income[year] / income[year - 1] - 1) * 100, 2),
    }
    for year in sorted(national_cpi.keys() & income.keys())
    if 1970 <= year <= 2024 and year - 1 in national_cpi and year - 1 in income
]
regions = {}
for region, series_id in {
    "Northeast": "CUUR0100SAF11",
    "Midwest": "CUUR0200SAF11",
    "South": "CUUR0300SAF11",
    "West": "CUUR0400SAF11",
}.items():
    observations = annual_means(series_id)
    regions[region] = {
        "seriesId": series_id,
        "annual": [
            {
                "year": year,
                "changePercent": round((value / observations[year - 1] - 1) * 100, 2)
                if year - 1 in observations else None,
            }
            for year, value in sorted(observations.items()) if year <= 2024
        ],
    }
indicators = {"national": national, "regions": regions}
(ROOT / "data" / "indicators.json").write_text(json.dumps(indicators, indent=2) + "\n")
subprocess.run([sys.executable, str(ROOT / "scripts" / "build-map.py")], check=True, cwd=ROOT)
page = (ROOT / "index.html").read_text()
page = replace_between(page, "<!-- GENERATED MAP START -->", "<!-- GENERATED MAP END -->", (ROOT / "data" / "us-map.svg").read_text().strip())
page = replace_between(page, "<!-- GENERATED INDICATORS START -->", "<!-- GENERATED INDICATORS END -->", f'<script id="indicators" type="application/json">{json.dumps(indicators, separators=(",", ":"))}</script>')
cex = json.loads((ROOT / "data" / "cex-snapshot.json").read_text())
for snapshot in cex["snapshots"]:
    for geography in (snapshot["regions"], snapshot["divisions"]):
        for row in geography.values():
            row["sharePercent"] = round(row["foodAtHome"] / row["income"] * 100, 2)
page = replace_between(page, "<!-- GENERATED CEX START -->", "<!-- GENERATED CEX END -->", f'<script id="cex" type="application/json">{json.dumps(cex, separators=(",", ":"))}</script>')
(ROOT / "index.html").write_text(page)
print(f"Embedded {len(national)} complete national years through {national[-1]['year']}; refreshed {len(regions)} regional CPI series.")
