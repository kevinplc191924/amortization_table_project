# 📊 Loan Amortization Table Generator
A simple Python module to generate amortization tables for fixed-rate loans. This tool calculates periodic payments,
interest, principal amortization, and remaining balance over the life of a loan.

## 🔧 Features
- Calculates equivalent periodic interest rate from annual rate
- Computes fixed payment per period (monthly, quarterly, etc.)
- Generates a detailed amortization schedule using pandas
- Supports payments at the beginning or end of each period

## 📦 Requirements
- `Python 3.11+`
- `pandas`
- `numpy`

## 🚀 Usage
```python
from amortization_table import LoanAmortization

loan = LoanAmortization(
    loan_amount=100000,
    annual_rate=0.05,
    periods_per_year=12,
    years=30
)

table = loan.get_table()
print(table.head())
```

## 🧠 Behind the Scenes
The class uses the formula for fixed-rate loan payments and iteratively computes interest and principal breakdowns for
each period. It supports both end-of-period and beginning-of-period payments.
