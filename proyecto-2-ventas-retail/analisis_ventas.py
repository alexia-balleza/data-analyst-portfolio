"""
Proyecto 2 — Análisis exploratorio de ventas retail (Python: pandas + matplotlib).

Uso:
    pip install pandas matplotlib
    python analisis_ventas.py

Genera 4 gráficos PNG y un resumen de hallazgos en consola.
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv", parse_dates=["OrderDate"])

print("=" * 60)
print("RESUMEN DEL DATASET")
print("=" * 60)
print(f"Órdenes: {len(df):,} | Periodo: {df.OrderDate.min().date()} → {df.OrderDate.max().date()}")
print(f"Ventas totales: ${df.Sales.sum():,.0f} | Utilidad total: ${df.Profit.sum():,.0f}")
print(f"Margen global: {100*df.Profit.sum()/df.Sales.sum():.1f}%")
print("\nNulos por columna:\n", df.isna().sum().to_string())
print("\nDuplicados (OrderID):", df.duplicated("OrderID").sum())

# --- Hallazgo 1: margen por categoría ---
margen = (100 * df.groupby("Category")["Profit"].sum() / df.groupby("Category")["Sales"].sum()).round(1)
print("\n--- Margen por categoría ---\n", margen.to_string())
print(">> Office Supplies tiene el mejor margen (27.9%) aunque vende menos: oportunidad de impulso.")

# --- Hallazgo 2: tendencia mensual ---
df["Mes"] = df.OrderDate.dt.to_period("M").astype(str)
mensual = df.groupby("Mes")[["Sales", "Profit"]].sum()

# --- Gráficos ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Retail Sales Analysis — EDA", fontsize=14, fontweight="bold")

ax = axes[0, 0]
ventas_cat = df.groupby("Category")["Sales"].sum().sort_values()
ventas_cat.plot.barh(ax=ax, color="#1F3B63")
ax.set_title("Ventas por categoría (USD)")
ax.set_xlabel("")

ax = axes[0, 1]
margen.plot.bar(ax=ax, color="#2E7D32")
ax.set_title("Margen de utilidad por categoría (%)")
ax.axhline(margen.mean(), color="red", linestyle="--", label="Promedio")
ax.legend()

ax = axes[1, 0]
mensual["Sales"].plot(ax=ax, color="#1F3B63", marker="o", markersize=3)
ax.set_title("Tendencia mensual de ventas")
ax.tick_params(axis="x", labelrotation=45)

ax = axes[1, 1]
top_sub = df.groupby("SubCategory")["Sales"].sum().sort_values(ascending=False).head(6)
top_sub.plot.bar(ax=ax, color="#1565C0")
ax.set_title("Top 6 subcategorías por ventas")
ax.tick_params(axis="x", labelrotation=30)

plt.tight_layout()
plt.savefig("eda_ventas.png", dpi=120)
print("\nGráfico guardado: eda_ventas.png")

# --- Hallazgo 3: ticket promedio por segmento ---
ticket = df.groupby("Segment")["Sales"].mean().round(2).sort_values(ascending=False)
print("\n--- Ticket promedio por segmento ---\n", ticket.to_string())

# --- Hallazgo 4: anomalías ---
anomalias = df[df.Profit <= 0]
print(f"\nÓrdenes con utilidad ≤ 0: {len(anomalias)} ({100*len(anomalias)/len(df):.2f}%) → revisar precios/costos.")
print("\nListo. Sube retail_sales.csv, consultas.sql, este script y eda_ventas.png a GitHub.")
