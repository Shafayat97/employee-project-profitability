# Management Report: Employee & Project Profitability (Jul–Sep 2026)

Oct 27, 2026 · @Muhammad Shafayat Hossain

## Executive summary

All five projects are profitable: $142,500 revenue and $36,431 cost gave **$106,069 profit (74.4% margin)** over July–September 2026. The real risk is how people are used, not which projects are taken on.

- **Briclab earns the most** ($27,488 profit); **ShopEase earns the least per hour worked** ($33 vs $55 for MediCore).
- **Two engineers are overloaded:** Amina Rahman (131%) and Tanvir Hasan (125%) staff both Briclab and LearnLoop alone.
- **Six people have spare capacity:** about **$8,450 of salary (23% of payroll)** paid for hours not logged on any project.
- Labor is 85% of all cost, so staffing decisions move profit far more than cutting expenses.

## 1. Which projects generate the most profit?

Briclab and MediCore lead on profit; ShopEase has the lowest margin and the lowest revenue per hour, despite using the most hours.

| Project | Client | Revenue ($) | Labor cost ($) | Other cost ($) | Profit ($) | Margin | Hours | Revenue per hour ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Briclab | Northstar Ltd | 36,000 | 7,172 | 1,340 | 27,488 | 76.4% | 690 | 52.2 |
| MediCore | HealthBridge | 33,000 | 5,967 | 1,520 | 25,513 | 77.3% | 600 | 55.0 |
| FinTrack | Delta Finance | 28,500 | 5,766 | 810 | 21,924 | 76.9% | 630 | 45.2 |
| ShopEase | RetailWorks | 24,000 | 6,666 | 990 | 16,344 | 68.1% | 720 | 33.3 |
| LearnLoop | EduSpark | 21,000 | 5,541 | 660 | 14,799 | 70.5% | 540 | 38.9 |
| **Total** |  | **142,500** | **31,111** | **5,320** | **106,069** | **74.4%** | **3,180** | **44.8** |

Revenue per hour shows how well a project's price matches the effort it takes. ShopEase earns $33 per hour of work, 40% less than MediCore.

## 2. Which projects have the highest utilization and cost?

ShopEase uses the most hours (720) and Briclab has the highest labor cost ($7,172). Team utilization averages 82.8%, but it is very uneven between people.

| Employee | Department | Projects | Hours (3 months) | Utilization |
| --- | --- | --- | --- | --- |
| Amina Rahman | Engineering | Briclab, LearnLoop | 630 | 131% |
| Tanvir Hasan | Engineering | Briclab, LearnLoop | 600 | 125% |
| Sajid Karim | Engineering | ShopEase | 405 | 84% |
| Rakib Ahmed | Engineering | FinTrack | 345 | 72% |
| Farhana Akter | QA | ShopEase | 315 | 66% |
| Mehedi Chowdhury | Project Management | MediCore | 315 | 66% |
| Nadia Islam | Design | FinTrack | 285 | 59% |
| Jannat Sultana | QA | MediCore | 285 | 59% |

Utilization = hours logged ÷ 480 standard hours (160 per month × 3).

- Briclab and LearnLoop are run by the same two engineers, with no QA or design support. Amina and Tanvir worked 270 hours above standard capacity, a burnout and delivery risk for the most profitable project.
- Every other project has two people, and most of them have spare hours.

## Where money is being wasted

The biggest loss is paid time not spent on client work: about $8,450 over three months, more than all software and hosting costs combined ($5,320).

| Employee | Spare hours | Salary paid for spare hours ($) |
| --- | --- | --- |
| Mehedi Chowdhury | 165 | 1,959 |
| Nadia Islam | 195 | 1,584 |
| Jannat Sultana | 195 | 1,523 |
| Rakib Ahmed | 135 | 1,350 |
| Farhana Akter | 165 | 1,238 |
| Sajid Karim | 75 | 797 |
| **Total** | **930** | **8,452** |

- **ShopEase is under-priced for its effort.** It takes the most hours but earns the least per hour ($33).
- **Software subscriptions cost $2,550.** MediCore alone spends $1,010 (40% of the total), more than any other project.
- Some spare hours may be work that was done but not logged: Mehedi, the only project manager, records time on MediCore only.

## 3. Recommendations for management

Most of the gain comes from moving existing people, which costs nothing extra because staff are salaried.

1. **Rebalance engineering work.** Move about 210 hours of LearnLoop engineering from Amina and Tanvir to Rakib (135 spare hours) and Sajid (75 spare hours). This brings both overloaded engineers close to 100% and protects Briclab, the top earner.
2. **Add QA and design to Briclab and LearnLoop.** Assign Jannat and Farhana (QA) and Nadia (design) to these projects. This takes testing and design off the engineers and puts about $4,300 of idle salary to use.
3. **Reprice or rescope ShopEase at renewal.** Matching the team average of $44.8 per hour would mean about $10,750 per month instead of $8,000. If the client will not pay more, reduce the hours spent.
4. **Audit software subscriptions, starting with MediCore.** Cancel unused licences and share tools across projects.
5. **Tighten timesheets.** Allow only valid project codes, block negative or blank hours, approve entries before month end, and ask the project manager to log time on every project he supports.

## Data and method notes

- **Sources:** employees, projects, timesheets and expenses files for July–September 2026 (8 employees, 5 projects).
- **Revenue** = monthly contract revenue × 3 months. **Labor cost** = hours logged × hourly rate, where hourly rate = monthly salary ÷ 160.
- **Excluded records:** 5 timesheet entries (negative hours, a blank entry, an unknown employee with pending approval, an unknown project) and 1 expense charged to an unknown project.
- **Name fix:** the project list said “Bricly” while timesheets and expenses said “Briclab”; “Briclab” is used throughout.
- **Limitation:** overtime is valued at the normal hourly rate. Using the full payroll of $36,750 instead, profit is $100,430 (70.5% margin); the conclusions do not change.
- Analysis built with SQL (SQLite), Excel, Python (pandas) and Power BI. Code and data: [GitHub repository](https://github.com/Shafayat97/employee-project-profitability).
