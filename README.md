# The Grocery Gap

A static, source-first data story about grocery prices, personal income, and food-at-home spending across U.S. Census regions and divisions. It is built as an experiment that can run directly from GitHub Pages and can also be opened as a single HTML file.

## Open it

- Open `index.html` in a browser. It makes no network requests.
- Or serve this folder locally with any static file server.
- To edit in VS Code, open `food-price-story.code-workspace`.

## What the page shows

1. **Indexed growth, 1970–2024.** The national food-at-home CPI-U and BEA personal income per capita each start at 100 in 1970. The map adds regional CPI-U growth from the first complete year, 1978. Division outlines inherit their region’s CPI value because the packaged BLS series does not provide a comparable division food-at-home index.
2. **Food-at-home budget share, 2021–2022.** BLS average annual food-at-home expenditures divided by average annual income before taxes for consumer units. “At home” describes where food is purchased: grocery-store food counts even if eaten elsewhere; restaurant takeout and delivery count as “away from home,” even if eaten at home. Both Census regions and divisions are available in the cited tables. This is a ratio of two averages, not the average of individual shares or a “typical household” measure. It is an overlapping two-year mean, not a one-year estimate.

The map’s state outlines are for orientation. Statistics belong to regions/divisions, never individual states. The map and synchronized list can be operated by pointer or keyboard. A screen-reader-friendly detail panel and source notes accompany the visuals.

## Sources

- BLS CPI-U food-at-home series: national [`CUUR0000SAF11`](https://fred.stlouisfed.org/series/CUUR0000SAF11), and four Census regions [`Northeast`](https://fred.stlouisfed.org/series/CUUR0100SAF11), [`Midwest`](https://fred.stlouisfed.org/series/CUUR0200SAF11), [`South`](https://fred.stlouisfed.org/series/CUUR0300SAF11), [`West`](https://fred.stlouisfed.org/series/CUUR0400SAF11). Retrieved from FRED; underlying source is the U.S. Bureau of Labor Statistics.
- BEA personal income per capita, annual: [`A792RC0A052NBEA`](https://fred.stlouisfed.org/series/A792RC0A052NBEA).
- BLS Consumer Expenditure Survey 2021–2022 geographic means: [Table 1800, regions](https://www.bls.gov/cex/tables/geographic/mean/cu-region-2-year-average-2021-2022.pdf) and [Table 2700, divisions](https://www.bls.gov/cex/tables/geographic/mean/cu-division-2-year-average-2021-2022.pdf).
- Census geography: [regions and divisions](https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html). State outline geometry is from [`us-atlas`](https://github.com/topojson/us-atlas), based on U.S. Census Bureau cartographic boundaries.

See [the design notes](docs/plans/2026-10-12-food-price-story-design.md) for definitions, scope, and experiment boundary. Raw annual source observations and processed snapshots live in `data/`.

## Data notes

- CPI is an index of price change, not household spending in dollars.
- BEA personal income per capita is not wages, take-home pay, or median income. The comparison is about broad nominal growth rates, not full affordability.
- Each national index is divided by its own 1970 value and multiplied by 100. Each regional CPI index uses that region’s 1978 annual mean as 100.
- Annual CPI values are arithmetic averages of the twelve monthly non-seasonally-adjusted observations. The packaged personal-income series is annual.
- The regional/division spending snapshot is a two-calendar-year BLS table. A ratio of the reported means does not reveal how food spending is distributed within the geography.
- No state-level food-price or spending observation is included.

## License

The visualization code is MIT licensed. Source datasets retain their source agencies’ terms and citations; see `data/README.md`.

## Experiment boundary

Started 2026-10-12. Review, renew, or archive by 2026-11-11.
