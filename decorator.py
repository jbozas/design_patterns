from abc import ABC, abstractmethod
from decimal import Decimal


class LoanCalculator(ABC):
    """
    Every Loan or interest Class has the same responsability, calculating
    the loan amount. This class exists because of that.
    """

    @abstractmethod
    def calculate_loan_amount(self, loan_amount: Decimal) -> Decimal:
        pass


class BasicLoanCalculator(LoanCalculator):
    """
    Basic Loans dont apply any extra charge.
    """

    def calculate_loan_amount(self, loan_amount: Decimal) -> Decimal:
        return loan_amount


class LoanDecorator(LoanCalculator):
    def __init__(self, component):
        self.loan_calculator = component

    def calculate_loan_amount(self, loan_amount: int) -> int:
        return self.loan_calculator.calculate_loan_amount(loan_amount)


class InsuranceDecorator(LoanDecorator):
    """
    Insurance loans apply an extra constant charge.
    """

    def calculate_loan_amount(self, loan_amount: int) -> int:
        base_amount = super().calculate_loan_amount(loan_amount)
        insurance_cost = 500
        return base_amount + insurance_cost


class SpecialInterestDecorator(LoanDecorator):
    """
    Special interests apply an extra percentage to the Loan's amount.
    """

    def calculate_loan_amount(self, loan_amount: int) -> int:
        base_amount = super().calculate_loan_amount(loan_amount)
        special_interest_rate = 0.1
        return round(base_amount * (1 + special_interest_rate), 2)


if __name__ == "__main__":
    loan_amount = 100_000

    print(
        f"Basic loan amount: {BasicLoanCalculator().calculate_loan_amount(loan_amount)}"
    )
    print(
        f"Basic loan amount + insurance: {InsuranceDecorator(BasicLoanCalculator()).calculate_loan_amount(loan_amount)}"
    )
    print(
        f"Basic loan amount + special interest: {SpecialInterestDecorator(BasicLoanCalculator()).calculate_loan_amount(loan_amount)}"
    )
    print(
        f"All three interests together: {InsuranceDecorator(SpecialInterestDecorator(BasicLoanCalculator())).calculate_loan_amount(loan_amount)}"
    )
