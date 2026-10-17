# Data Analyst Portfolio — Alexia Balleza

Actuary (UNAM) turned Data Analyst. Two end-to-end projects using the tools real job postings ask for: **SQL, Python, Power BI, Excel**.

| Project | Skills | Folder |
|---|---|---|
| 1. Employee Attrition Dashboard | Power BI, DAX, People Analytics storytelling | `proyecto-1-rotacion-personal/` |
| 2. Retail Sales Analysis | SQL (10 business queries), Python (pandas, matplotlib), EDA | `proyecto-2-ventas-retail/` |
| 3. Power BI Course Dashboards (3) | Forecasting, time series, AI visuals (key influencers, decomposition tree) | `tableros-powerbi-curso/` |

## Project 1 — Employee Attrition Dashboard (Power BI)

HR analytics on a 1,470-employee dataset: attrition rate by department, role, overtime, and job satisfaction, plus income-vs-tenure analysis.

**Key finding:** employees working overtime quit at **2.4x the rate** (14.5% vs 6.0%) — the basis for a workload-review recommendation. See `hallazgos_rotacion.png` for the visual summary.

→ Full build guide (DAX measures + dashboard layout): `proyecto-1-rotacion-personal/guia-powerbi.md`

## Project 2 — Retail Sales Analysis (SQL + Python)

Business analysis on 5,000 retail orders (2023–2025): 10 SQL queries (sales by category, margins, monthly trends, average ticket, top customers, anomaly detection) + Python EDA with data-quality checks and charts.

**Key finding:** Office Supplies has the **highest margin (27.9%)** despite the lowest sales → push the most profitable category; Furniture sells the most ($1.83M) at the thinnest margin (12.0%) → review pricing.

→ Run it: `pip install pandas matplotlib` → `python analisis_ventas.py`; open `retail.db` in [DB Browser for SQLite](https://sqlitebrowser.org/) and run `consultas.sql`.

*All datasets are synthetic, generated for portfolio purposes.*
