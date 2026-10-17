# Proyecto 2 — Análisis de Ventas Retail (SQL + Python)

**Qué demuestra:** consultas SQL de negocio + análisis exploratorio en Python — las dos habilidades que casi todos los puestos de Data Analyst piden en la descripción.

**Archivos:**
| Archivo | Qué es |
|---|---|
| `retail_sales.csv` | 5,000 órdenes de venta (2023–2025). Datos sintéticos generados para portafolio. |
| `retail.db` | Misma data en SQLite, tabla `orders` — lista para practicar SQL. |
| `consultas.sql` | 10 consultas de negocio: ventas por categoría, márgenes, tendencia mensual, ticket promedio, top clientes, detección de anomalías, comparativo anual. |
| `analisis_ventas.py` | EDA en Python (pandas + matplotlib): limpieza, validación y 4 gráficos. |
| `eda_ventas.png` | Gráficos generados por el script. |

**Cómo correrlo:**
1. Instala Python y luego: `pip install pandas matplotlib`
2. `python analisis_ventas.py` → verás el resumen en consola y se crea `eda_ventas.png`.
3. Para SQL: abre `retail.db` con [DB Browser for SQLite](https://sqlitebrowser.org/) (gratis) y pega las consultas de `consultas.sql` una por una.

**Hallazgos principales (úsalos en entrevistas):**
- Margen global 16.3%; Office Supplies tiene el mejor margen (**27.9%**) con las ventas más bajas → oportunidad de impulsar la categoría más rentable.
- Furniture vende mucho ($1.83M) pero con el margen más bajo (12.0%) → revisar precios o costos.
- Ticket promedio parejo entre segmentos (~$885–$916).

**Preguntas típicas de entrevista (practícalas en inglés):**
- *"How did you check data quality?"* → nulos, duplicados de OrderID, rangos de fechas, utilidades negativas.
- *"What business recommendation would you make?"* → impulsar Office Supplies, revisar pricing de Furniture.
- *"Walk me through a complex query."* → explica la #7 (margen bajo + ventas altas con HAVING).
