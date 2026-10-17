-- Proyecto 2 — Análisis de ventas retail (SQLite)
-- Base: retail.db, tabla: orders

-- 1. Ventas y utilidad totales
SELECT COUNT(*) AS num_ordenes,
       ROUND(SUM(Sales), 2) AS ventas_totales,
       ROUND(SUM(Profit), 2) AS utilidad_total
FROM orders;

-- 2. Ventas y margen por categoría
SELECT Category,
       ROUND(SUM(Sales), 2) AS ventas,
       ROUND(SUM(Profit), 2) AS utilidad,
       ROUND(100.0 * SUM(Profit) / SUM(Sales), 1) AS margen_pct
FROM orders
GROUP BY Category
ORDER BY ventas DESC;

-- 3. Top 5 subcategorías por ventas
SELECT SubCategory,
       ROUND(SUM(Sales), 2) AS ventas,
       ROUND(SUM(Profit), 2) AS utilidad
FROM orders
GROUP BY SubCategory
ORDER BY ventas DESC
LIMIT 5;

-- 4. Ventas por región y segmento
SELECT Region, Segment,
       COUNT(*) AS ordenes,
       ROUND(SUM(Sales), 2) AS ventas
FROM orders
GROUP BY Region, Segment
ORDER BY ventas DESC;

-- 5. Tendencia mensual de ventas
SELECT SUBSTR(OrderDate, 1, 7) AS mes,
       ROUND(SUM(Sales), 2) AS ventas,
       ROUND(SUM(Profit), 2) AS utilidad
FROM orders
GROUP BY mes
ORDER BY mes;

-- 6. Ticket promedio por segmento
SELECT Segment,
       COUNT(*) AS ordenes,
       ROUND(AVG(Sales), 2) AS ticket_promedio
FROM orders
GROUP BY Segment
ORDER BY ticket_promedio DESC;

-- 7. Subcategorías con margen bajo (<15%) y ventas altas: candidatas a revisar precios
SELECT SubCategory,
       ROUND(SUM(Sales), 2) AS ventas,
       ROUND(100.0 * SUM(Profit) / SUM(Sales), 1) AS margen_pct
FROM orders
GROUP BY SubCategory
HAVING margen_pct < 15
ORDER BY ventas DESC;

-- 8. Mejores 10 clientes por ventas
SELECT CustomerID,
       COUNT(*) AS ordenes,
       ROUND(SUM(Sales), 2) AS ventas_totales
FROM orders
GROUP BY CustomerID
ORDER BY ventas_totales DESC
LIMIT 10;

-- 9. Detección de anomalías: órdenes con utilidad negativa o cero
SELECT OrderID, OrderDate, Region, SubCategory, Sales, Profit
FROM orders
WHERE Profit <= 0
ORDER BY Profit;

-- 10. Comparativo año contra año
SELECT SUBSTR(OrderDate, 1, 4) AS anio,
       COUNT(*) AS ordenes,
       ROUND(SUM(Sales), 2) AS ventas,
       ROUND(SUM(Profit), 2) AS utilidad
FROM orders
GROUP BY anio
ORDER BY anio;
