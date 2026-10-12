# Data files and refresh notes

Data packaged 2026-10-12. The browser reads only the embedded snapshots in `index.html`; the files below preserve source observations and source lineage.

| File | Contents | Source |
|---|---|---|
| `indicators.json` | Annual national CPI and BEA personal income per-capita values/indexes, 1970–2024; annual CPI index by Census region, 1978–2024 | CSV observations in `source/` |
| `cex-snapshot.json` | BLS region and division food-at-home and pre-tax income means, plus the ratio of means for 2021–2022 | BLS Tables 1800 and 2700 |
| `us-map.svg` | Static state outline map | Generated from `source/us-states-albers-10m.json` |
| `source/CUUR*.csv` | Monthly BLS CPI-U food-at-home index observations retrieved from FRED | Series IDs are in the filenames |
| `source/A792RC0A052NBEA.csv` | Annual BEA personal income per capita | FRED series ID in filename |
| `source/us-states-albers-10m.json` | Albers USA TopoJSON states geometry | `us-atlas` project; U.S. Census Bureau cartographic boundaries |

`indicators.json` annual CPI is calculated as the arithmetic mean of the twelve monthly observations for each full calendar year. Index values are each series divided by its own base-year annual value, multiplied by 100. CEX shares are `foodAtHome / income * 100`; dollar means are rounded to whole dollars as reported by BLS.

The division and region values in the CEX snapshot are taken directly from Tables 2700 and 1800, respectively. Their labels preserve the source's 2021–2022 period. The BLS table list is the source of truth for later available periods.

Run `python3 scripts/refresh-site.py` after replacing source CSVs or the CEX snapshot. It rebuilds annual means and indexes, regenerates the map, and embeds the packaged data in `index.html`. It does not fetch data from the network. The map geometry generation script is `scripts/build-map.py`; it scales the public `us-atlas` TopoJSON into an inline SVG and associates Census division membership for visual grouping. It does not attach statistical values to states.
