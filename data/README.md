# Data files and refresh notes

Data packaged 2026-10-12. The browser reads only the embedded snapshots in `index.html`; the files below preserve source observations and source lineage.

| File | Contents | Source |
|---|---|---|
| `indicators.json` | Annual national CPI and BEA personal income per-capita values and year-over-year percentage changes, 1970–2024; regional CPI observations, annual changes, and cumulative changes from the 1978 baseline, 1978–2024 | CSV observations in `source/` |
| `cex-snapshot.json` | Seven BLS region and division food-at-home and pre-tax income mean snapshots, 2017–2018 through 2023–2024, plus computed ratios of means and percentage-point changes from the first snapshot | BLS Tables 1800 and 2700 |
| `us-map.svg` | Static state outline map | Generated from `source/us-states-albers-10m.json` |
| `source/CUUR*.csv` | Monthly BLS CPI-U food-at-home index observations retrieved from FRED; national series includes 1969 as the baseline for the 1970 annual change | Series IDs are in the filenames |
| `source/A792RC0A052NBEA.csv` | Annual BEA personal income per capita; includes 1969 as the baseline for the 1970 annual change | FRED series ID in filename |
| `source/us-states-albers-10m.json` | Albers USA TopoJSON states geometry | `us-atlas` project; U.S. Census Bureau cartographic boundaries |

`indicators.json` annual CPI is calculated as the arithmetic mean of the twelve monthly observations for each full calendar year. Annual changes compare each year’s annual-average CPI or personal income with the prior year. The national CPI and income files include 1969 only to calculate the first displayed change in 1970. Regional CPI starts in 1978; cumulative growth is each year’s annual-average index divided by its 1978 average, minus one. CEX shares are `foodAtHome / income * 100`; dollar means are rounded to whole dollars as reported by BLS. Budget-share change is shown in percentage points relative to each geography’s 2017–2018 share.

The region and division CEX values are transcribed from BLS Tables 1800 and 2700 for seven overlapping periods from 2017–2018 through 2023–2024. Each snapshot includes its period-specific source URLs. Ratios are computed from the reported whole-dollar means. Newer periods use the Excel workbooks linked by the [BLS geographic table index](https://www.bls.gov/cex/tables/geographic/mean.htm).

Run `python3 scripts/refresh-site.py` after replacing source CSVs or the CEX snapshot. It rebuilds annual means and indexes, regenerates the map, and embeds the packaged data in `index.html`. It does not fetch data from the network. The map geometry generation script is `scripts/build-map.py`; it scales the public `us-atlas` TopoJSON into an inline SVG and associates Census division membership for visual grouping. It does not attach statistical values to states.
