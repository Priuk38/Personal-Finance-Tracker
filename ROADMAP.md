# Project Roadmap — Personal Finance Tracker

**Target deadline:** 23 November 2026  
**Team size:** 3 members  
**Language:** Python  
**Interface:** Terminal / console  
**Workflow:** feature branches → `dev` → `main`

This roadmap follows the lecturer's **Panduan Proyek Akhir — Simple Personal Finance Tracker**. The guide's required scope takes priority over optional improvements.

## Required scope (assignment checklist)

### 1. Transaction management
- Add an income or expense transaction.
- Each transaction contains date, type (`pemasukan` / `pengeluaran`), category, short description, and amount.

### 2. Display and filtering
- Display all transactions.
- Provide filters for income only and expenses only.
- Filtering must not mix transaction types.

### 3. Monthly financial report
For a selected month, display:
- Total income.
- Total expenses.
- Balance.
- Expense breakdown by category.
- The category with the largest expense.
- Saving rate: `(income - expenses) / income * 100%`.
- If income is zero, show an appropriate message; never divide by zero.
- Only include transactions from the selected month.

### 4. CSV storage and export
- Save transactions to a CSV file.
- Load saved transactions when the application starts again.
- Export transaction data to CSV.
- Export the monthly summary/report to CSV.
- Use relative paths so the project can run from its project folder.

### 5. Simple dashboard
- Show the current balance.
- Show several recent transactions on the main menu or a terminal summary screen.

### 6. Validation and exception handling
- Amount must be a valid number greater than zero.
- Invalid input must show a clear message and must not immediately terminate the program.
- Handle the first run when the transaction CSV does not exist (for example, `FileNotFoundError`).
- Validate dates using the date format adopted by the program.
- Handling Ctrl+C, corrupted CSV files, and custom exceptions are optional extensions, not requirements.

## Scope boundaries

- The application runs in the terminal / console.
- No GUI, website, database, or login system is required.
- One or multiple well-organized Python files are allowed.
- Use CSV for financial data and exported files.
- Keep the menu understandable and divide program responsibilities into clearly purposed functions.

## Shared transaction format

All modules must use the same keys and value types:

```python
{
    "tanggal": "2026-11-19",       # YYYY-MM-DD
    "jenis": "pemasukan",          # or "pengeluaran"
    "kategori": "Uang saku",
    "keterangan": "Mingguan",
    "nominal": 200000              # positive number
}
```

Suggested CSV columns:

```text
tanggal,jenis,kategori,keterangan,nominal
```

The example values are illustrative; they are not required data.

## Project structure

```text
Personal-Finance-Tracker/
├── main.py
├── transactions.py
├── reports.py
├── storage.py
├── data/
│   └── transactions.csv
├── exports/
│   ├── transactions_export.csv
│   └── monthly_report.csv
├── README.md
└── ROADMAP.md
```

The CSV files may be created by the program during use. The application must still work on first launch if `data/transactions.csv` is not present.

## Team responsibilities

| Member | Main responsibility | Files |
|---|---|---|
| Member 1 (integration) | Main menu, dashboard, transaction flow, connect modules, integration testing | `main.py`, `transactions.py` |
| Member 2 | Monthly calculations, saving rate, expense breakdown, largest expense category | `reports.py` |
| Member 3 | CSV loading, saving, transaction export, monthly report export | `storage.py` |

The division above is a team implementation plan, not a restriction in the lecturer's guide. The report must include each member's actual task / functions / code contribution. **Every member must understand the important parts of the complete program**, because the individual oral examination can cover code written by other members too.

## Four-day execution plan

### Day 1 — 19 Nov: Confirm design and build modules
- Confirm this checklist against the lecturer's guide.
- Agree on the shared transaction format and function contracts.
- Member 1: implement menu, dashboard skeleton, add/list/filter transaction flow.
- Member 2: implement monthly totals, balance, saving rate, expense breakdown, and largest expense category using sample data.
- Member 3: implement CSV load/save and both export paths using sample records.
- Checkpoint: each module can be tested independently.

### Day 2 — 20 Nov: Integrate modules
- Connect `main.py`, `transactions.py`, `reports.py`, and `storage.py`.
- Test add → save → close/reopen → load → display.
- Test the first-run case when the CSV file is missing.
- Fix import errors, mismatched function arguments, and data type issues.
- Checkpoint: the main user flow works from the menu.

### Day 3 — 21 Nov: Complete reports, validation, and tests
- Complete the selected-month report and both CSV exports.
- Add date, transaction-type, and positive-amount validation.
- Test income-only and expense-only filters.
- Test empty data, invalid input, missing CSV, zero income, and normal transactions.
- Verify monthly calculations manually with a small known dataset.
- Checkpoint: all required features work without known blockers.

### Day 4 — 22 Nov: Stabilize and prepare submission
- Run a full test from a clean start.
- Fix high-priority bugs; avoid optional features.
- Prepare README run instructions and evidence of program execution.
- Prepare the group PDF report and functional test table using actual results.
- Each member practices explaining the overall flow and important code.
- Merge the tested `dev` branch into `main`.

### Deadline — 23 Nov
- Final check against the assignment guide.
- Confirm source code, sample transaction CSV, exported CSV files, PDF report, and README are ready.
- Compress the deliverables into one ZIP.
- One group representative uploads the ZIP to the LMS.

## Report requirements (group PDF)

Follow the guide's structure and explain the program that was actually implemented.

- **Cover:** project title, course, class, member names, student IDs, and group identity.
- **Chapter I — Introduction**
  - 1.1 Background: practical problem addressed, in the group's own words.
  - 1.2 Program objectives: objectives that can be demonstrated by working features.
- **Chapter II — Program Design**
  - 2.1 One main flowchart matching the actual menu and code flow, with a short explanation.
  - 2.2 CSV structure: file names, columns, data shape, and sample data generated by the program.
- **Chapter III — Implementation and Testing**
  - 3.1 Implemented features and Python functions used.
  - 3.2 Important code excerpts with explanations of flow and logic.
  - 3.3 Execution evidence: menu, transactions, monthly report, and CSV export.
  - 3.4 Functional test table: scenario, expected result, actual result, and status.
- **Chapter IV — Closing**
  - 4.1 Conclusion based on features that were actually completed and tested.
  - 4.2 Real obstacles and limitations encountered.
- **Appendix:** actual task division for each member, especially functions or code sections completed.

Avoid repetitive flow descriptions, unrelated long theory sections, and printing the entire source code in the report. The Python source files are submitted separately.

## Submission deliverables

- Runnable Python source files (`.py`).
- Example transaction CSV.
- CSV files generated by transaction and monthly-report exports.
- Group report in PDF.
- Short run instructions in `README.md` or `README.txt`.
- All deliverables compressed into one ZIP for LMS upload by one group representative.

## Presentation and individual oral examination

The group demonstrates the main features, then each member is examined individually using the group's program. Possible topics include:
- Explaining a function.
- Tracing variable values in a loop.
- Predicting the CSV contents after an operation.
- Explaining the effect of changing file mode `"a"` to `"w"`.
- Explaining calculation results.
- Locating input validation and error handling.

Questions may differ by student but are intended to assess comparable competencies. Practice explaining the entire codebase, not only your assigned module.

## Assessment weights

| Assessment aspect | Weight |
|---|---:|
| Program functionality | 30% |
| Logic and calculation accuracy | 10% |
| Report and testing | 20% |
| Code understanding in oral examination | 40% |

## Git workflow

- `main`: stable version for submission.
- `dev`: integration branch.
- `feature/transactions`: Member 1.
- `feature/reports`: Member 2.
- `feature/storage`: Member 3.

Each member works on their feature branch and merges through a pull request into `dev`. Test the integrated version before merging `dev` into `main`.

## Definition of done

- [ ] All five required feature groups are implemented and demonstrable.
- [ ] Dashboard shows balance and several recent transactions.
- [ ] Monthly report includes totals, balance, expense breakdown, largest expense category, and saving rate.
- [ ] Zero-income report does not divide by zero.
- [ ] Transaction CSV persists after closing and reopening the program.
- [ ] First launch works when the transaction CSV is missing.
- [ ] Transaction and monthly-report CSV exports contain correct data.
- [ ] Filters show the selected transaction type only.
- [ ] Invalid amount and date inputs are handled clearly.
- [ ] Monthly calculations include only the selected month.
- [ ] Functional tests include expected and actual results.
- [ ] PDF report follows the required structure and records actual member contributions.
- [ ] README explains how to run the program.
- [ ] Every member can explain important parts of the complete code.
- [ ] Source, sample CSV, exported CSVs, PDF report, and README are included in one ZIP.
- [ ] `main` contains the tested submission version.
