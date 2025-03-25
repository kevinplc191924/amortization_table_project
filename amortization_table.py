import pandas as pd
import numpy as np

class LoanAmortization:
    """
    A class to calculate and generate an amortization table for a loan.

    Attributes:
        loan_amount (float): The total amount of the loan.
        annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
        periods_per_year (int): The number of payment periods per year (e.g., 12 for monthly payments).
        years (int): The total duration of the loan in years.
        nper (int): The total number of payment periods (calculated as years * periods_per_year).
        periodic_rate (float): The interest rate per payment period.
        payment (float): The fixed payment amount per period.
    """

    def __init__(self, loan_amount, annual_rate, periods_per_year, years):
        """
        Initialize the LoanAmortization class with loan details.

        Args:
            loan_amount (float): The total amount of the loan.
            annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
            periods_per_year (int): The number of payment periods per year.
            years (int): The total duration of the loan in years.
        """
        self.loan_amount = loan_amount
        self.annual_rate = annual_rate
        self.periods_per_year = periods_per_year
        self.years = years
        self.nper = years * periods_per_year
        self.periodic_rate = self.equivalent_rate()
        self.payment = self.calculate_payment()

    def equivalent_rate(self):
        """
        Calculate the equivalent periodic interest rate from the annual rate.

        Returns:
            float: The interest rate per payment period.
        """
        return (1 + self.annual_rate) ** (1 / self.periods_per_year) - 1

    def calculate_payment(self, when="end"):
        """
        Calculate the fixed payment amount per period.

        Args:
            when (str): Specifies whether payments are made at the 'end' or 'begin' of the period.
                        Defaults to 'end'.

        Returns:
            float: The fixed payment amount per period.
        """
        if self.periodic_rate == 0:
            return self.payment / self.nper
        if when == "end":
            return (
                self.periodic_rate
                * (self.loan_amount * (1 + self.periodic_rate) ** self.nper)
            ) / ((1 + self.periodic_rate) ** self.nper - 1)
        elif when == "begin":
            return (
                self.periodic_rate
                * (self.loan_amount * (1 + self.periodic_rate) ** self.nper)
            ) / (((1 + self.periodic_rate) ** self.nper - 1) * (1 + self.periodic_rate))

    def get_table(self):
        """
        Generate the amortization table for the loan.

        The table includes the following columns:
            - Period: The payment period number.
            - Payment: The fixed payment amount for each period.
            - Interest: The interest portion of the payment for each period.
            - Amortization: The principal portion of the payment for each period.
            - Principal: The remaining loan balance after each payment.

        Returns:
            pandas.DataFrame: A DataFrame containing the amortization table.
        """
        table = pd.DataFrame()

        principal = np.empty(self.nper + 1)
        principal[0] = self.loan_amount
        interest = np.empty(self.nper + 1)
        amortization = np.empty(self.nper + 1)

        for i in range(self.nper):
            interest[i] = principal[i] * self.periodic_rate
            amortization[i] = self.payment - interest[i]
            principal[i + 1] = principal[i] - amortization[i]

        table["Period"] = np.arange(self.nper + 1)
        table["Payment"] = np.repeat(self.payment, self.nper + 1)
        table["Interest"] = interest
        table["Amortization"] = amortization
        table["Principal"] = principal

        return table.iloc[: self.nper].round(2)
