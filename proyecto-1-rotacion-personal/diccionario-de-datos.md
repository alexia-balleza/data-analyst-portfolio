# Diccionario de datos — `hr_attrition.csv`

Datos sintéticos generados para fines de portafolio (1,470 empleados). Simulan la información típica de un sistema HRIS como SAP SuccessFactors.

| Columna | Descripción | Ejemplo |
|---|---|---|
| EmployeeID | Identificador único del empleado | 1001 |
| Age | Edad | 34 |
| Gender | Género | Female |
| Department | Departamento | Sales |
| JobRole | Puesto | Sales Executive |
| MonthlyIncome | Sueldo mensual (USD) | 6500 |
| Overtime | ¿Hace horas extra? | Yes / No |
| JobSatisfaction | Satisfacción laboral (1=baja, 4=alta) | 3 |
| WorkLifeBalance | Balance vida-trabajo (1=malo, 4=bueno) | 2 |
| YearsAtCompany | Antigüedad en la empresa (años) | 5 |
| YearsInCurrentRole | Años en el puesto actual | 2 |
| TrainingTimesLastYear | Capacitaciones el último año | 3 |
| DistanceFromHome_mi | Distancia casa–trabajo (millas) | 12 |
| Attrition | ¿Renunció? (variable objetivo) | Yes / No |

**Hallazgos principales (para usar en el dashboard y en entrevistas):**
- Rotación general: **8.5%**
- Con horas extra: **14.5%** vs sin horas extra: **6.0%** (≈2.4x más)
- Satisfacción = 1: **11.7%** de rotación
- Departamento Sales: **9.3%** (el más alto); puesto Sales Representative: **11.8%**
