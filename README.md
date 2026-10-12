# The Grocery Gap

A static, source-first data story about grocery prices, food-budget shares, personal income, and food-at-home spending across U.S. Census regions and divisions. It is built as an experiment that can run directly from GitHub Pages and can also be opened as a single HTML file.

## Open it

- Open `index.html` in a browser. It makes no network requests.
- Or serve this folder locally with any static file server.
- To edit in VS Code, open `food-price-story.code-workspace`.

## What the page shows

1. **Cumulative food-price growth, 1978–2024.** The map shows each region’s annual-average food-at-home CPI-U increase relative to its 1978 index. Use Play or scrub through 1979–2024 to watch the cumulative increase build. Division outlines inherit their region’s rate because BLS does not provide a comparable division food-at-home CPI series. The national chart separately compares annual price and income growth.
2. **National food-budget share, 1997–2025.** The USDA chart shows food at home, food away from home, and total food as shares of disposable personal income. Use Play or scrub to see the annual estimate. The current USDA series starts in 1997; it is a national aggregate, not a particular household’s budget.
3. **Regional food-at-home share, 2017–2018 through 2023–2024.** The BLS map detail shows average annual food-at-home expenditures divided by average annual income before taxes for consumer units. Map color shows the percentage-point change in that share since 2017–2018; the current share remains visible in the detail. “At home” describes where food is purchased: grocery-store food counts even if eaten elsewhere; restaurant takeout and delivery count as “away from home,” even if eaten at home. Both Census regions and divisions are available in the cited tables. Use Play or scrub to move through seven overlapping two-year snapshots. This is a ratio of two averages, not the average of individual shares or a “typical household” measure. Each point is an overlapping two-year mean, not a one-year estimate.

The map’s state outlines are for orientation. Statistics belong to regions/divisions, never individual states. The map and synchronized list can be operated by pointer or keyboard. A screen-reader-friendly detail panel and source notes accompany the visuals.

## Sources

- BLS CPI-U food-at-home series: national [`CUUR0000SAF11`](https://fred.stlouisfed.org/series/CUUR0000SAF11), and four Census regions [`Northeast`](https://fred.stlouisfed.org/series/CUUR0100SAF11), [`Midwest`](https://fred.stlouisfed.org/series/CUUR0200SAF11), [`South`](https://fred.stlouisfed.org/series/CUUR0300SAF11), [`West`](https://fred.stlouisfed.org/series/CUUR0400SAF11). Retrieved from FRED; underlying source is the U.S. Bureau of Labor Statistics.
- BEA personal income per capita, annual: [`A792RC0A052NBEA`](https://fred.stlouisfed.org/series/A792RC0A052NBEA).
- USDA ERS [Food Expenditure Series](https://www.ers.usda.gov/data-products/food-expenditure-series/) and its [current normalized household-final-user CSV](https://www.ers.usda.gov/media/5198/normalized-food-expenditures-by-all-purchasers-and-household-final-users.csv?v=29412). The CSV contains annual national food-budget shares for 1997–2025.
- BLS Consumer Expenditure Survey [geographic table index](https://www.bls.gov/cex/tables/geographic/mean.htm), including Tables 1800 (regions) and 2700 (divisions). Period-specific PDF links are embedded with each snapshot in `data/cex-snapshot.json`.
- Census geography: [regions and divisions](https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html). State outline geometry is from [`us-atlas`](https://github.com/topojson/us-atlas), based on U.S. Census Bureau cartographic boundaries.

Raw annual source observations and processed snapshots live in `data/`.

## Data notes

- CPI is an index of price change, not household spending in dollars.
- BEA personal income per capita is not wages, take-home pay, or median income. The comparison is about broad nominal growth rates, not full affordability.
- The national chart’s price and income changes compare each year’s annual value with the prior year. Map price growth compares each selected annual CPI average with its region’s 1978 average.
- Food-budget-share map changes are percentage-point differences from each geography’s 2017–2018 ratio of means.
- USDA national food shares use USDA’s reported percentage of disposable personal income. They are not the BLS ratio of regional mean expenses to mean pre-tax income, so the two views have different denominators and should not be directly ranked against each other.
- Annual CPI values are arithmetic averages of the twelve monthly non-seasonally-adjusted observations. The packaged personal-income series is annual.
- The regional/division spending snapshot is a two-calendar-year BLS table. A ratio of the reported means does not reveal how food spending is distributed within the geography.
- No state-level food-price or spending observation is included.

## License

The visualization code is MIT licensed. Source datasets retain their source agencies’ terms and citations; see `data/README.md`.

## Experiment boundary

Started 2026-10-12. Review, renew, or archive by 2026-11-11.
