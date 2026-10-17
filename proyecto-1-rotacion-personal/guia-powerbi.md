# Proyecto 1 — Dashboard de Rotación de Personal (Power BI)

**Qué demuestra:** análisis de datos de RRHH de punta a punta — justo el nicho de *People Analytics / HR Data Analyst*, donde tu experiencia en SAP SuccessFactors te diferencia.

**Tiempo estimado:** 4–6 horas (ideal hacerlo dentro del curso de Power BI).

> **Nota:** si prefieres practicar Tableau (también lo sabes), puedes construir este mismo dashboard ahí — los datos y los hallazgos son los mismos. Pero hacerlo en Power BI te cuenta para el certificado de diciembre, así que conviene más aquí.

## Paso 1 — Importar los datos
1. Abre Power BI Desktop → **Get Data → Text/CSV** → selecciona `hr_attrition.csv`.
2. En Power Query, verifica tipos: `MonthlyIncome` = número entero, `Attrition`/`Overtime` = texto, `JobSatisfaction` = número entero.
3. **Close & Apply**.

## Paso 2 — Crear medidas DAX (pestaña Modeling → New Measure)
```dax
Total Employees = COUNTROWS(hr_attrition)

Attrition Count = CALCULATE(COUNTROWS(hr_attrition), hr_attrition[Attrition] = "Yes")

Attrition Rate = DIVIDE([Attrition Count], [Total Employees])

Avg Satisfaction = AVERAGE(hr_attrition[JobSatisfaction])

Avg Income = AVERAGE(hr_attrition[MonthlyIncome])
```

## Paso 3 — Armar el dashboard (1 página)
Arriba, 4 tarjetas **KPI**: Total Employees · Attrition Rate · Avg Satisfaction · Avg Income.

Abajo, estos gráficos:
1. **Attrition Rate por Department** (barras) — Sales sale más alto (9.3%).
2. **Attrition Rate por JobRole** (barras) — Sales Representative 11.8%.
3. **Attrition: Overtime Yes vs No** (barras o donut) — 14.5% vs 6.0%. Este es tu hallazgo estrella.
4. **Attrition Rate por JobSatisfaction** (columnas) — a menor satisfacción, más renuncias.
5. **Dispersión MonthlyIncome vs YearsAtCompany**, coloreado por Attrition — muestra que los que se van suelen ganar menos con poca antigüedad.
6. **Slicer** por Department y Gender para que el dashboard sea interactivo.

## Paso 4 — Hallazgos y recomendaciones (esto es lo que impresiona en entrevistas)
Escribe 3–4 bullets en una caja de texto del dashboard o en el README:
- Los empleados con horas extra renuncian **2.4 veces más** (14.5% vs 6.0%) → revisar cargas de trabajo.
- Satisfacción = 1 → **11.7%** de rotación → programa de retención enfocado.
- Sales concentra el riesgo (9.3%, y 11.8% en Sales Representative).

## Paso 5 — Publicar el portafolio
1. En Power BI Desktop: **File → Export → Export to PDF** (guarda el dashboard como imagen/reporte).
2. Sube el archivo `.pbix`, el PDF y este CSV a un repositorio en GitHub (ver `portafolio/README.md`).
3. Agrega el proyecto a tu CV y a LinkedIn (sección Featured/Proyectos).

## Preguntas típicas de entrevista sobre este proyecto (practícalas en inglés)
- *"Walk me through this dashboard."* → cuenta la historia: KPIs → dónde está el problema → qué recomiendas.
- *"How did you validate the data?"* → tipos en Power Query, conteos que cuadran con el total.
- *"What would you do with real company data?"* → conectar al HRIS (como SuccessFactors), automatizar el refresh mensual.
