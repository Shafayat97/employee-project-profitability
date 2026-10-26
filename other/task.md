# Employee & Project Profitability Analysis — Beginner Project

## Scenario
Analyze fictional employee, project, timesheet, and expense data for July–September 2026.

## Files
- `practice_data.xlsx`: all tables in separate sheets, plus README
- `employees.csv`
- `projects.csv`
- `timesheets.csv`
- `expenses.csv`

## Intentional data-quality issues to find
The raw data includes duplicated timesheet records, inconsistent approval-status formatting, missing hours, negative hours, an unknown employee ID, an unknown project ID in timesheets, and an unknown project ID in expenses. Identify and document each issue before deciding how to handle it. Do not silently delete records; record your rationale.

## Assumptions for practice
- Project monthly revenue applies in each of July, August, and September. Confirm and state this assumption in your report.
- Approximate labor cost rate = monthly salary / 160 hours.
- Project labor cost = sum of valid timesheet hours multiplied by each employee's hourly cost rate.
- For utilization, use 160 available hours per employee per month. Since the sample has only project hours, explain that utilization may be overstated if non-project duties are not captured.
- Expense amounts are USD.
- Keep revenue, labor cost, and expenses at compatible monthly/project grain to avoid double-counting.

## Deliverables
1. Data quality log and cleaned tables
2. SQL schema, joins, and project-level summary query
3. Excel pivot table and formulas
4. Python cleaning/validation script
5. Power BI dashboard with KPI cards, project profitability, monthly trend, and utilization
6. Statistics section (mean, median, spread, and one careful comparison)
7. One-page management summary with three evidence-based recommendations
8. GitHub repository with README, scripts, queries, and screenshots (do not upload confidential company data)

## Business questions
1. Which project has the highest revenue, cost, and profit?
2. Which project has the highest and lowest profit margin?
3. How did project profitability change month by month?
4. What is average employee utilization by month?
5. Which records were invalid or incomplete, and how did cleaning decisions affect the result?
6. What are three practical recommendations for management?

## Suggested Git workflow
- Initialize a repository.
- Commit raw fictional data, scripts, SQL, documentation, and final screenshots in separate logical commits.
- Use a `.gitignore` for temporary files and local environments.
- Include an AI usage note describing what AI helped with and how outputs were verified.
