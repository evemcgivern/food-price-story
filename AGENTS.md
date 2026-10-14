# AGENTS.md

Workspace-wide rules (commits, security, plan-before-code, approval gates) live in `/Applications/Development/Projects/AGENTS.md`; this file only adds what is specific to this project.

## Project Overview

"The Grocery Gap": a static, source-first data story on U.S. grocery prices, food-budget shares, and income across Census regions and divisions. One `index.html` with the data embedded; it makes no network requests. Published to GitHub Pages. It is a timeboxed experiment: started 2026-10-12, review, renew, or archive by 2026-11-11 (see the README).

## Development Commands

```bash
python3 scripts/refresh-site.py   # rebuild annual means, indexes and map, re-embed data in index.html (no network)
python3 scripts/build-map.py      # map geometry only (refresh-site.py runs it)
```

There is no package manager, build step, or test suite. To preview, open `index.html` or serve the folder with any static file server.

## Architecture

- `index.html`: the whole page, with data snapshots embedded. `llms.txt`, `sitemap.xml`, `social-card.svg` are its metadata.
- `data/`: `indicators.json` (CPI and income), `cex-snapshot.json` (BLS region/division snapshots), `source/` (raw CSVs and TopoJSON), `us-map.svg`. `data/README.md` lists each file and its source.
- `scripts/`: the two Python scripts above.
- `.github/workflows/pages.yml`: publishes the site on every push to `main`.

## Common Gotchas

- Data claims are source-cited. Never add a number without a source series ID or table; keep the README and `data/README.md` in step with any change.
- Do not attach statistics to individual states. Values belong to regions or divisions; state outlines are orientation only.
- Pushing to `main` deploys the site. `refresh-site.py` rewrites `index.html`, so review the diff before committing.
- `.gitignore` excludes `private/`, `data/local/`, `data/private/`, and `.env*`. Keep private plans and local files there.
