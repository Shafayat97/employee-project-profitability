"""
Employee & Project Profitability Analysis (Jul-Sep 2026)

What this script does:
  1. Reads the 4 raw CSV files from data/raw/
  2. Cleans them (same rules as sql/01_data_cleaning.sql)
  3. Calculates project profit (P&L) and employee utilization
  4. Saves cleaned data, results and charts

Run from the project folder:  python python/analysis.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------------
# 0. Settings and folders
# ---------------------------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parent.parent   # main project folder
RAW_DIR = PROJECT_DIR / "data" / "raw"
CLEAN_DIR = PROJECT_DIR / "data" / "cleaned"
OUTPUT_DIR = PROJECT_DIR / "python" / "outputs"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MONTHS = 3                # Jul, Aug, Sep 2026
HOURS_PER_MONTH = 160     # standard working hours per employee per month


def read_raw(name):
    """Read a raw CSV and remove spaces around column names."""
    df = pd.read_csv(RAW_DIR / f"{name}.csv", encoding="utf-8-sig")
    df.columns = df.columns.str.strip()
    return df


def to_number(series):
    """Turn text like ' 12,000.00 ' into the number 12000.0."""
    return pd.to_numeric(
        series.astype(str).str.strip().str.replace(",", "", regex=False),
        errors="coerce",
    )


# ---------------------------------------------------------------
# 1. Load raw data
# ---------------------------------------------------------------
employees_raw = read_raw("employees")
projects_raw = read_raw("projects")
timesheets_raw = read_raw("timesheets")
expenses_raw = read_raw("expenses")

# ---------------------------------------------------------------
# 2. Clean data
# ---------------------------------------------------------------
# Employees: drop blank/total rows, recalculate hourly rate
employees = employees_raw.dropna(subset=["employee_id"]).copy()
employees["monthly_salary_usd"] = to_number(employees["monthly_salary_usd"])
employees["hourly_rate"] = employees["monthly_salary_usd"] / HOURS_PER_MONTH
employees = employees[["employee_id", "employee_name", "department",
                       "monthly_salary_usd", "hourly_rate"]]

# Projects: drop blank/total rows, convert revenue text to number
projects = projects_raw.dropna(subset=["project_id"]).copy()
projects["monthly_revenue_usd"] = to_number(projects["monthly_revenue_usd"])

valid_employees = set(employees["employee_id"])
valid_projects = set(projects["project_id"])

# Timesheets: keep only valid, approved, positive-hour entries
ts = timesheets_raw.dropna(subset=["timesheet_id"]).copy()
ts["hours_worked"] = to_number(ts["hours_worked"])
ts["approval_status"] = ts["approval_status"].astype(str).str.strip().str.title()
ts["work_date"] = pd.to_datetime(ts["work_date"].astype(str).str.strip(), errors="coerce")

is_valid = (
    (ts["hours_worked"] > 0)
    & (ts["approval_status"] == "Approved")
    & ts["employee_id"].isin(valid_employees)
    & ts["project_id"].isin(valid_projects)
)
timesheets = ts[is_valid][["timesheet_id", "work_date", "employee_id",
                           "project_id", "hours_worked", "approval_status"]]
excluded_timesheets = ts[~is_valid]

# Expenses: drop blank/total rows and unknown projects
ex = expenses_raw.dropna(subset=["expense_id"]).copy()
ex["amount_usd"] = to_number(ex["amount_usd"])
ex["expense_date"] = pd.to_datetime(ex["expense_date"].astype(str).str.strip(), errors="coerce")
expenses = ex[ex["project_id"].isin(valid_projects)][
    ["expense_id", "expense_date", "project_id", "expense_category", "amount_usd"]]
excluded_expenses = ex[~ex["project_id"].isin(valid_projects)]

# Save cleaned data
employees.to_csv(CLEAN_DIR / "employees.csv", index=False)
projects.to_csv(CLEAN_DIR / "projects.csv", index=False)
timesheets.to_csv(CLEAN_DIR / "timesheets.csv", index=False)
expenses.to_csv(CLEAN_DIR / "expenses.csv", index=False)

print("=== DATA CLEANING ===")
print(f"Timesheets kept: {len(timesheets)}, excluded: {len(excluded_timesheets)}")
print(excluded_timesheets[["timesheet_id", "employee_id", "project_id",
                           "hours_worked", "approval_status"]].to_string(index=False))
print(f"Expenses kept: {len(expenses)}, excluded: {len(excluded_expenses)}\n")

# ---------------------------------------------------------------
# 3. Question 1 & 2: Project P&L
# ---------------------------------------------------------------
# Add each employee's hourly rate to every timesheet row (like SQL JOIN)
ts_cost = timesheets.merge(employees[["employee_id", "employee_name", "hourly_rate"]],
                           on="employee_id")
ts_cost["labor_cost"] = ts_cost["hours_worked"] * ts_cost["hourly_rate"]

labor = ts_cost.groupby("project_id").agg(hours=("hours_worked", "sum"),
                                          labor_cost=("labor_cost", "sum"))
other = expenses.groupby("project_id").agg(other_cost=("amount_usd", "sum"))

pnl = projects.set_index("project_id")[["project_name", "monthly_revenue_usd"]]
pnl["revenue"] = pnl["monthly_revenue_usd"] * MONTHS
pnl = pnl.join(labor).join(other).fillna(0)
pnl["total_cost"] = pnl["labor_cost"] + pnl["other_cost"]
pnl["profit"] = pnl["revenue"] - pnl["total_cost"]
pnl["margin_pct"] = pnl["profit"] / pnl["revenue"] * 100
pnl["cost_per_hour"] = pnl["total_cost"] / pnl["hours"]
pnl = pnl.drop(columns="monthly_revenue_usd").sort_values("profit", ascending=False)

print("=== PROJECT P&L (Jul-Sep 2026) ===")
print(pnl.round(2).to_string())
print(f"\nTotal profit: ${pnl['profit'].sum():,.2f}\n")

# ---------------------------------------------------------------
# 4. Question 2: Employee utilization
# ---------------------------------------------------------------
util = ts_cost.groupby("employee_name").agg(total_hours=("hours_worked", "sum"))
util["utilization_pct"] = util["total_hours"] / (HOURS_PER_MONTH * MONTHS) * 100
util["status"] = pd.cut(util["utilization_pct"], bins=[0, 70, 100, 1000],
                        labels=["Under-used (<70%)", "Healthy", "Overloaded (>100%)"])
util = util.sort_values("utilization_pct", ascending=False)

print("=== EMPLOYEE UTILIZATION (3 months, 480 h = 100%) ===")
print(util.round(1).to_string())

# Save results
pnl.round(2).to_csv(OUTPUT_DIR / "project_pnl.csv")
util.round(1).to_csv(OUTPUT_DIR / "employee_utilization.csv")

# ---------------------------------------------------------------
# 5. Charts
# ---------------------------------------------------------------
# Chart 1: Profit by project
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(pnl["project_name"], pnl["profit"], color="#2E86AB")
ax.set_title("Profit by Project (Jul-Sep 2026)")
ax.set_ylabel("Profit (USD)")
for i, value in enumerate(pnl["profit"]):
    ax.text(i, value, f"${value:,.0f}", ha="center", va="bottom")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_project.png", dpi=150)
plt.close()

# Chart 2: Revenue vs cost
fig, ax = plt.subplots(figsize=(8, 5))
x = range(len(pnl))
ax.bar([i - 0.2 for i in x], pnl["revenue"], width=0.4, label="Revenue", color="#2E86AB")
ax.bar([i + 0.2 for i in x], pnl["total_cost"], width=0.4, label="Total cost", color="#E07A5F")
ax.set_xticks(list(x))
ax.set_xticklabels(pnl["project_name"])
ax.set_title("Revenue vs Cost by Project (Jul-Sep 2026)")
ax.set_ylabel("USD")
ax.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_vs_cost.png", dpi=150)
plt.close()

# Chart 3: Employee utilization with 100% line
colors = ["#D62828" if v > 100 else "#F4A261" if v < 70 else "#2A9D8F"
          for v in util["utilization_pct"]]
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(util.index, util["utilization_pct"], color=colors)
ax.axvline(100, color="black", linestyle="--", label="100% capacity")
ax.invert_yaxis()
ax.set_title("Employee Utilization (Jul-Sep 2026)")
ax.set_xlabel("Utilization (%)")
ax.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "employee_utilization.png", dpi=150)
plt.close()

print(f"\nDone! Results and charts saved in: {OUTPUT_DIR}")
