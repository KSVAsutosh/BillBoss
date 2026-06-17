# Bill Boss

Bill Boss is a modern personal finance and expense management web application built using Django. It helps users track expenses, monitor income, manage budgets, handle recurring transactions, analyze spending habits, and generate financial reports.

## Features

### User Authentication

* User Registration
* User Login
* User Logout
* Profile Management

### Dashboard

* Total Balance Overview
* Income Summary
* Expense Summary
* Recent Transactions
* Financial Insights

### Expense Management

* Add Expenses
* Edit Expenses
* Delete Expenses
* Expense Categories

### Income Management

* Add Income Sources
* Track Earnings
* Income Analytics

### Account Management

* Cash Account
* Bank Account
* Wallet Account
* Multiple Account Support

### Budget Tracking

* Monthly Budgets
* Category-wise Budgets
* Budget Progress Monitoring
* Budget Alerts

### Recurring Transactions

* Daily Transactions
* Weekly Transactions
* Monthly Transactions
* Yearly Transactions

### Debt Management

* Borrowed Money Tracking
* Lent Money Tracking
* Payment Records
* Due Date Tracking

### Reports & Analytics

* Income vs Expense Reports
* Category Reports
* Monthly Reports
* Yearly Reports
* Visual Charts and Graphs

### Settings

* Currency Selection
* Theme Preferences
* Notification Settings

---

## Technology Stack

### Backend

* Python 3.11+
* Django 5
* SQLite (Development)
* PostgreSQL (Production)

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Additional Libraries

* Pillow
* Pandas
* Matplotlib
* Crispy Forms

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/billboss.git
cd billboss
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

Application URL:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Project Structure

```text
BillBoss/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── billboss/
├── accounts/
├── dashboard/
├── categories/
├── accounts_wallet/
├── transactions/
├── budgets/
├── recurring/
├── debts/
├── reports/
├── settings_app/
│
├── templates/
├── static/
├── media/
│
└── db.sqlite3
```

---

## Future Enhancements

* OCR Receipt Scanning
* AI Expense Prediction
* Smart Budget Recommendations
* Bank API Integration
* UPI Integration
* Mobile Application
* Multi-Currency Support
* Cloud Synchronization

---

## Author

K.S.V. Asutosh

B.Tech CSE (Data Science)

Malla Reddy University

---

## License

This project is developed for educational and portfolio purposes.
