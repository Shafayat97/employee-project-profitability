-- 02_analysis.sql
-- Q1: Project profit (3 months: Jul-Sep 2026)
WITH revenue AS (SELECT project_id, project_name, monthly_revenue_usd*3 AS revenue FROM projects),
labor AS (SELECT t.project_id, SUM(t.hours_worked) AS hours, SUM(t.hours_worked*e.hourly_rate) AS labor_cost
          FROM timesheets t JOIN employees e ON t.employee_id=e.employee_id GROUP BY t.project_id),
exp AS (SELECT project_id, SUM(amount_usd) AS other_cost FROM expenses GROUP BY project_id)
SELECT r.project_name, r.revenue, l.hours, ROUND(l.labor_cost,2) AS labor_cost, x.other_cost,
       ROUND(r.revenue-l.labor_cost-x.other_cost,2) AS profit,
       ROUND(100.0*(r.revenue-l.labor_cost-x.other_cost)/r.revenue,1) AS margin_pct
FROM revenue r LEFT JOIN labor l ON r.project_id=l.project_id LEFT JOIN exp x ON r.project_id=x.project_id
ORDER BY profit DESC;

-- Q2: Employee utilization per month (160 hours = 100%)
SELECT e.employee_name, SUBSTR(t.work_date,1,7) AS month, SUM(t.hours_worked) AS hours,
       ROUND(100.0*SUM(t.hours_worked)/160,1) AS utilization_pct
FROM timesheets t JOIN employees e ON t.employee_id=e.employee_id
GROUP BY e.employee_name, month ORDER BY utilization_pct DESC;