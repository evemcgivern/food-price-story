# Implementation plan: food price story

## Plain-English summary

Build one self-contained public page that lets a reader move from the national grocery-price timeline to regional and division comparisons. Package source data with citations so the page works offline and on GitHub Pages. Every chart label explains what the number measures and where it stops being available.

## Tasks

1. **Set up public project docs**
   - Replace the scaffold README with purpose, data definitions, limitations, local preview steps, GitHub Pages notes, and source citations.
   - Add MIT license, `.gitignore`, VS Code workspace shortcut, and experiment review date.
   - Add design and implementation docs.

2. **Assemble cited data snapshots**
   - Package annual national food-at-home CPI-U from BLS/FRED (1970–2024 complete common annual data; later observations are excluded where the annual CPI has missing months).
   - Package four regional CPI series from BLS/FRED and the national BEA per-capita personal-income series. Division CPI is unavailable in this dataset and inherits the division's region on the map with an explicit label.
   - Include verified BLS 2021–2022 regional and divisional CEX means for food at home and income before taxes; compute their ratio of means without conflating it with individual or annual household affordability.
   - Record exact IDs, source URLs, units, retrieval date, geography membership, and calculations in the data README/metadata.

3. **Build the map-first page**
   - Create accessible SVG map and explicit state-orientation disclaimer.
   - Add metric selector, annual year selector, region/division tree, synchronized map, trend plot, summary value, and text equivalents for map values.
   - Render indexed price/income separately from the CEX ratio, with unavailable-state messaging.
   - Add citations and plain-language methodology.

4. **Prepare public static launch**
   - Add metadata, canonical/OG/Twitter tags, JSON-LD, `sitemap.xml`, and `llms.txt`.
   - Add GitHub Actions workflow to publish the static root to GitHub Pages.
   - Add a browser-friendly local preview command.

5. **Verify and publish**
   - Refresh packaged data from checked-in source snapshots, inspect the page in a browser at desktop and mobile widths, check map keyboard navigation, inspect data points against citations, and run full-history Gitleaks with the repository-provided Gitleaks configuration.
   - Confirm GitHub identity is `evemcgivern`; create/use the public repo, publish the feature branch through a reviewable PR/merge, enable Pages, and verify the live URL.
   - Prepare the portfolio card and Search Console sitemap URL for the public site.

## Acceptance

- A stranger can follow README instructions and reproduce a local preview.
- Page is static and does not request secrets or external data at runtime.
- National index comparison reaches 1970–2024 complete annual data; regional CPI views begin in 1978 and division selection is labeled as inherited region CPI.
- Census regions and divisions are named; state outlines are clearly only visual context.
- CEX 2021–2022 ratios use official average food-at-home expenditures and average pre-tax incomes and are labeled as ratios of means for an overlapping two-year period.
- All views have text equivalents, keyboard operation, citations, and explicit unavailable data.
- Public repo includes a license, Pages deployment workflow, source/method notes, and no secrets/history hits. No separate automated test suite is included in this static experiment.
- GitHub Pages is live under `evemcgivern` and the deployed page is checked directly.
