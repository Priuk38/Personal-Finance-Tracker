# Project Roadmap — Personal Finance Tracker

**Target deadline:** 23 November 2026  
**Team size:** 3 members  
**Language:** Python  
**Workflow:** feature branches → `dev` → `main`

## Scope (MVP)

1. Add income and expense transactions.
2. View and filter transactions.
3. Calculate total income, total expenses, and current balance.
4. Show a monthly summary and expense totals by category.
5. Save and load transaction data using CSV.
6. Export transaction data or a monthly report to CSV.
7. Validate user input and handle missing/invalid data gracefully.

Keep the first version focused. Only add optional features after the required features work reliably.

## Team responsibilities

| Member | Main responsibility | Files |
|---|---|---|
| Member 1 (integration) | Main menu, transaction flow, connect modules, final testing | `main.py`, `transactions.py` |
| Member 2 | Financial calculations and monthly/category reports | `reports.py` |
| Member 3 | CSV loading, saving, and export | `storage.py` |

All members should understand the complete program because each may be asked to explain it.

## Four-day execution plan

### Day 1 — 19 Nov: Agree on design and build the core
- Confirm required features against the lecturer's instructions.
- Agree on one transaction data format and function names.
- Member 1: implement menu and add/list/filter transaction flow.
- Member 2: implement income, expense, balance, and category calculations using sample data.
- Member 3: implement CSV load/save with sample records.
- End-of-day checkpoint: each module can be tested independently.

### Day 2 — 20 Nov: Integrate the modules
- Connect `main.py`, `transactions.py`, `reports.py`, and `storage.py`.
- Make sure all modules use the same transaction structure.
- Test add → save → reload → display.
- Fix import errors, mismatched function arguments, and data type issues.
- End-of-day checkpoint: the main user flow works from the menu.

### Day 3 — 21 Nov: Reports, validation, and testing
- Complete monthly summary and category totals.
- Add validation for transaction type, date, category, and positive numeric amount.
- Test empty data, invalid input, missing CSV file, and normal transactions.
- Verify calculations manually with a small known dataset.
- End-of-day checkpoint: no known blocker in the MVP features.

### Day 4 — 22 Nov: Stabilize and prepare submission
- Run a full test from a clean start.
- Fix high-priority bugs; avoid adding new optional features.
- Prepare README instructions, screenshots if required, and a short demo scenario.
- Each member practices explaining their own module and the overall program.
- Merge the tested `dev` branch into `main`.

### Deadline — 23 Nov
- Final review against the assignment rubric.
- Confirm the submitted GitHub link/files and presentation/demo materials.
- Do not make risky last-minute changes unless they fix a critical issue.

## Shared transaction format

Use the same keys and value types in every module:

```python
{
    "tanggal": "2026-11-19",       # ISO date: YYYY-MM-DD
    "jenis": "pemasukan",          # or "pengeluaran"
    "kategori": "Uang saku",
    "keterangan": "Mingguan",
    "nominal": 200000              # integer, positive
}
```

## Git workflow

- `main`: stable version for submission.
- `dev`: integration branch.
- `feature/transactions`: Member 1.
- `feature/reports`: Member 2.
- `feature/storage`: Member 3.

Each member commits to their own feature branch, then opens a pull request into `dev`. Test the integrated version before merging `dev` into `main`.

## Definition of done

- [ ] All MVP features work.
- [ ] Data persists after closing and reopening the program.
- [ ] Invalid input does not crash the program.
- [ ] Report totals match manually checked sample data.
- [ ] README explains how to run the program.
- [ ] All three members can explain the overall flow and their own code.
- [ ] `main` contains the tested submission version.
