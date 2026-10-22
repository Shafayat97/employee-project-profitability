-- 01_data_cleaning.sql
-- Creates clean tables from the raw_* tables imported from CSV.
-- Removes blank rows, total rows, negative/empty hours, unknown employees/projects,
-- non-approved timesheets; converts text numbers ("12,000.00") to real numbers.
-- Hourly rate = monthly salary / 160 working hours.

DROP TABLE IF EXISTS employees;
CREATE TABLE employees AS
SELECT TRIM(employee_id) AS employee_id, TRIM(employee_name) AS employee_name, TRIM(department) AS department,
       CAST(monthly_salary_usd AS REAL) AS monthly_salary_usd,
       CAST(monthly_salary_usd AS REAL) / 160 AS hourly_rate
FROM raw_employees WHERE employee_id IS NOT NULL AND TRIM(employee_id) <> '';

DROP TABLE IF EXISTS projects;
CREATE TABLE projects AS
SELECT TRIM(project_id) AS project_id,
       TRIM(project_name) AS project_name,
       TRIM(client) AS client,
       CAST(REPLACE(TRIM(monthly_revenue_usd), ',', '') AS REAL) AS monthly_revenue_usd,
       TRIM(project_status) AS project_status
FROM raw_projects WHERE project_id IS NOT NULL AND TRIM(project_id) <> '';

DROP TABLE IF EXISTS timesheets;
CREATE TABLE timesheets AS
SELECT TRIM(timesheet_id) AS timesheet_id, COALESCE(DATE(TRIM(work_date)), TRIM(work_date)) AS work_date,
       TRIM(employee_id) AS employee_id, TRIM(project_id) AS project_id,
       CAST(hours_worked AS REAL) AS hours_worked,
       'Approved' AS approval_status
FROM raw_timesheets
WHERE TRIM(timesheet_id) <> ''
  AND TRIM(hours_worked) <> ''
  AND CAST(hours_worked AS REAL) > 0
  AND LOWER(TRIM(approval_status)) = 'approved'
  AND TRIM(employee_id) IN (SELECT employee_id FROM employees)
  AND TRIM(project_id)  IN (SELECT project_id  FROM projects);

DROP TABLE IF EXISTS expenses;
CREATE TABLE expenses AS
SELECT TRIM(expense_id) AS expense_id, COALESCE(DATE(TRIM(expense_date)), TRIM(expense_date)) AS expense_date,
       TRIM(project_id) AS project_id, TRIM(expense_category) AS expense_category,
       CAST(REPLACE(TRIM(amount_usd), ',', '') AS REAL) AS amount_usd
FROM raw_expenses
WHERE TRIM(expense_id) <> ''
  AND TRIM(project_id) IN (SELECT project_id FROM projects);
