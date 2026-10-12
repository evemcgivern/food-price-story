# Food price story — approved design

## Plain-English summary

This standalone, public data story compares grocery price growth with personal income growth in the United States, then lets readers inspect the result by Census region and division. A second view shows what consumer units reported spending on food at home relative to their pre-tax income. The map is the main navigation surface; a synchronized region/division tree and a table make every value accessible without relying on color or map precision.

## Question and audience

**Question:** Since 1970, how has the price of groceries changed relative to personal income, and how does the share of pre-tax income spent on food at home vary across Census regions and divisions?

Audience: curious public readers who need a clear distinction between price inflation, income growth, and a survey-based expenditure ratio.

## Measures

1. **Indexed change:** CPI-U food-at-home price index and BEA per-capita personal income, each independently indexed to 100 in the selected base year. Show growth paths together; index points are relative change and do not mean affordability or purchasing power. National coverage begins in 1970. Regional CPI coverage begins in 1977/78; regional income should be calculated from official state personal income and population data, with explicit formula and source period.
2. **Food-at-home budget share:** BLS average annual food-at-home expenditures divided by BLS average annual income before taxes for consumer units. This is a ratio of survey averages, not the average of each unit's personal share and not a typical household measure. Annual regional series are available from 1989 and division series from 2017; package only observed years. If a vintage/area is absent, display unavailable rather than interpolate.

## Geography and visual design

- Map-first hybrid with US state outlines as orientation only. Color and values apply to Census regions/divisions, never individual states.
- Census regions: Northeast, Midwest, South, West.
- Census divisions: New England, Middle Atlantic, East North Central, West North Central, South Atlantic, East South Central, West South Central, Mountain, Pacific.
- Region/division hierarchy selector is synchronized with map and details. Use explicit labels and a data table alongside the SVG map.
- Two-measure switch for indexed change and food-at-home budget share. Annual snapshots and year control. Period wording matches the underlying data.
- Responsive behavior: map and tree together on wide screens; list/detail first on narrow screens.
- Keyboard selection, visible focus, accessible names, text labels, non-color distinctions, reduced motion, and a no-JS source note.

## Sources and limits

- BLS CPI-U food at home: national series since 1970; regional/divisional price indexes are not state observations and start later. Source and series IDs are listed next to the chart.
- BEA state personal income and Census population estimates: used to compute division/region per-capita personal income as total personal income divided by population, with state geography crosswalk documented.
- BLS Consumer Expenditure Survey: expenditure and pre-tax income averages. Annual region/division rows for 2023 are included in BLS's 2023 Consumer Expenditures report. Region history is listed back to 1989; division history to 2017. These estimates refer to consumer units, not households in a uniform size/shape.
- BLS also publishes separate overlapping two-year geographic means tables. The app will not describe those as annual data or mix them into the annual series.
- BLS and BEA data are public federal statistics. Show retrieval date, table/series links, units, transformations, and methodology notes.

## Scope

Static HTML/CSS/JS, packaged data, GitHub Pages, no runtime API requests or secrets. Public repo under `evemcgivern`. Include an MIT license, visitor-focused README, CI, SEO metadata, sitemap, `llms.txt`, and a VS Code workspace file. No state-level affordability claims.

## Experiment boundary

Experiment created 2026-10-12; review or archive by 2026-11-11. Continue only if the source-backed map/story is useful enough to share and maintain.
