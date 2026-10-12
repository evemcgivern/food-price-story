# The Grocery Gap

A static, source-first data story about grocery prices, personal income, and food-at-home spending across U.S. Census regions and divisions. It is built as an experiment that can run directly from GitHub Pages and can also be opened as a single HTML file.

## Open it

- Open `index.html` in a browser. It makes no network requests.
- Or serve this folder locally with any static file server.
- To edit in VS Code, open `food-price-story.code-workspace`.

## What the page shows

1. **Annual change, 1970–2024.** The national chart compares each year’s percent change in annual-average food-at-home CPI-U with nominal personal income per capita. The map shows regional year-over-year CPI change from 1979; 1978 is the first complete regional year and provides the comparison baseline. Use Play to animate the annual map through 2024 or scrub to a year. Division outlines inherit their region’s CPI change because the packaged BLS series does not provide a comparable division food-at-home index.
2. **Food-at-home budget share, 2017–2018 through 2021–2022.** BLS average annual food-at-home expenditures divided by average annual income before taxes for consumer units. “At home” describes where food is purchased: grocery-store food counts even if eaten elsewhere; restaurant takeout and delivery count as “away from home,” even if eaten at home. Both Census regions and divisions are available in the cited tables. Use Play or scrub to move through five overlapping two-year snapshots; the newer 2022–2023 and 2023–2024 spreadsheets are listed on the [BLS geographic table index](https://www.bls.gov/cex/tables/geographic/mean.htm) but are not included in this package. This is a ratio of two averages, not the average of individual shares or a “typical household” measure. Each point is an overlapping two-year mean, not a one-year estimate.

The map’s state outlines are for orientation. Statistics belong to regions/divisions, never individual states. The map and synchronized list can be operated by pointer or keyboard. A screen-reader-friendly detail panel and source notes accompany the visuals.

## Sources

- BLS CPI-U food-at-home series: national [`CUUR0000SAF11`](https://fred.stlouisfed.org/series/CUUR0000SAF11), and four Census regions [`Northeast`](https://fred.stlouisfed.org/series/CUUR0100SAF11), [`Midwest`](https://fred.stlouisfed.org/series/CUUR0200SAF11), [`South`](https://fred.stlouisfed.org/series/CUUR0300SAF11), [`West`](https://fred.stlouisfed.org/series/CUUR0400SAF11). Retrieved from FRED; underlying source is the U.S. Bureau of Labor Statistics.
- BEA personal income per capita, annual: [`A792RC0A052NBEA`](https://fred.stlouisfed.org/series/A792RC0A052NBEA).
- BLS Consumer Expenditure Survey [geographic table index](https://www.bls.gov/cex/tables/geographic/mean.htm), including Tables 1800 (regions) and 2700 (divisions). Period-specific PDF links are embedded with each snapshot in `data/cex-snapshot.json`.
- Census geography: [regions and divisions](https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html). State outline geometry is from [`us-atlas`](https://github.com/topojson/us-atlas), based on U.S. Census Bureau cartographic boundaries.

Raw annual source observations and processed snapshots live in `data/`.

## Data notes

- CPI is an index of price change, not household spending in dollars.
- BEA personal income per capita is not wages, take-home pay, or median income. The comparison is about broad nominal growth rates, not full affordability.
- Annual price and income changes compare each year’s annual value with the prior year. Regional CPI change begins in 1979 because 1978 supplies the first full regional annual average.
- Annual CPI values are arithmetic averages of the twelve monthly non-seasonally-adjusted observations. The packaged personal-income series is annual.
- The regional/division spending snapshot is a two-calendar-year BLS table. A ratio of the reported means does not reveal how food spending is distributed within the geography.
- No state-level food-price or spending observation is included.

## License

The visualization code is MIT licensed. Source datasets retain their source agencies’ terms and citations; see `data/README.md`.

## Experiment boundary

Started 2026-10-12. Review, renew, or archive by 2026-11-11.
