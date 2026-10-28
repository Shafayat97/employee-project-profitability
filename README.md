# Employee & Project Profitability Analysis
Project P&amp;L and employee utilization analysis using SQL, Excel, Python and Power BI

Analysis of 5 software projects, 8 employees and 3 months (Jul–Sep 2026)
of timesheet and expense data.

## Business questions
1. Which projects generate the most profit?
2. Which projects have the highest employee utilization and cost?
3. What should management do to improve profitability?

## Tools
SQL (SQLite) · Excel · Python · Power BI

## Data cleaning
- Removed blank and total rows from all files
- Converted text amounts ("12,000.00") to numbers
- Excluded 5 invalid timesheet entries (negative hours, missing hours,
  unknown employee/project, pending approval) and 1 expense for an unknown project

## Key findings
- Briclab is the most profitable project ($27.5k profit over 3 months)
- Amina Rahman and Tanvir Hasan work 120–137% of standard hours,
  while some colleagues are at 56–62%

## Repository structure
- `Data/` – raw and cleaned datasets
- `Sql/` – data cleaning and analysis queries (SQLite)
- `Excel/` – P&L, PivotTable utilization analysis and charts
- `Python/` – automated cleaning and analysis script, results and charts
- `PowerBI/` – interactive dashboard (.pbix), PDF export and screenshot
- `Report/` – management report with findings and recommendations
Author

Md. Shafayat Hossain LinkedIn https://www.linkedin.com/in/shafayat-hossain-305aa5173/
