
# Personal Finance Manager (CLI)

A Python command-line application to help you **track income & expenses**, **set budgets**, and **generate monthly/yearly reports**. Built with a focus on simplicity, reliability, and maintainable code.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
  - [User Registration & Login](#user-registration--login)  
  - [Income & Expense Tracking](#income--expense-tracking)  
  - [Budgets](#budgets)  
  - [Reports](#reports)  
  - [Backup & Restore](#backup--restore)  
- [Project Output & Screenshots](#project-output--screenshots)  
- [Testing](#testing)  
- [Guidelines & Best Practices](#guidelines--best-practices)  
- [Suggested 25‑Day Timeline](#suggested-25-day-timeline)  
- [Contributing](#contributing)  
- [License](#license)  
- [Submission / Contact](#submission--contact)

---

## Overview

**Goal:** Create a CLI tool that lets users register/login, record transactions with categories (e.g., Food, Rent, Salary), set monthly category budgets, and generate monthly/yearly reports showing totals and savings. Data is stored locally (e.g., SQLite).

---

## Features

- **User Registration & Authentication**
- **Income & Expense Tracking**
- **Financial Reports**
- **Budgeting**
- **Data Persistence**
- **Testing & Documentation**

---

## Tech Stack

- **Language:** Python  
- **Database:** SQLite  
- **Interface:** Command Line (CLI)

---

## Project Structure

```txt
personal-finance-manager/
├─ pfm/
│  ├─ cli.py
│  ├─ auth.py
│  ├─ models.py
│  ├─ services/
│  ├─ db.py
│  └─ utils.py
├─ tests/
├─ assets/screenshots/
├─ requirements.txt
├─ README.md
└─ LICENSE
```

---

## Getting Started

```bash
git clone https://github.com/your-username/personal-finance-manager.git
cd personal-finance-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pfm.cli init-db
```

---

## Usage

### User Registration & Login

```bash
python -m pfm.cli register --username alice --password "StrongPass!23"
python -m pfm.cli login --username alice --password "StrongPass!23"
```

### Income & Expense Tracking

```bash
python -m pfm.cli add-income --amount 50000 --category Salary --note "July salary" --date 2025-07-01
python -m pfm.cli add-expense --amount 1200 --category Food --note "Groceries" --date 2025-07-02
python -m pfm.cli list-tx --month 2025-07
```

### Budgets

```bash
python -m pfm.cli set-budget --category Food --amount 5000 --month 2025-07
python -m pfm.cli view-budgets --month 2025-07
```

### Reports

```bash
python -m pfm.cli report --month 2025-07
python -m pfm.cli report --year 2025
```

### Backup & Restore

```bash
python -m pfm.cli backup --out backups/
python -m pfm.cli restore --file backups/backup-2025-07-30.db
```

---

## Project Output & Screenshots

Add screenshots to `assets/screenshots/` folder and reference them like below:

```md
### Sample Demo

**Login and Add Transactions**
![Login](assets/screenshots/login-and-add.png)

**Monthly Report**
![Report](assets/screenshots/report-july-2025.png)

**Budget Alert**
![Budget](assets/screenshots/budget-alert.png)
```

---

## Testing

```bash
pytest -q
```

Test modules for:
- Registration & login  
- Transaction operations  
- Budget checks  
- Reports

---

## Guidelines & Best Practices

- Use Python and SQLite  
- Keep code modular and clean  
- Provide CLI error messages and usage guides

---

## Suggested 25‑Day Timeline

- **Days 1–5:** Authentication  
- **Days 6–10:** CRUD transactions  
- **Days 11–15:** Reports  
- **Days 16–20:** Budgets  
- **Days 21–23:** Backup/restore  
- **Days 24–25:** Testing & Docs

---

## Contributing

1. Fork the repo  
2. Create a branch: `git checkout -b feat/feature-name`  
3. Push and PR

---

## License

MIT License

---

## Submission / Contact

- Submit at: https://forms.gle/KBqjYVUqG8zXX9zy8  
- Contact: internship.innobyteservices@gmail.com
