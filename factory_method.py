
# Factory method
from abc import ABC, abstractmethod


class Loan(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

    @abstractmethod
    def display(self):
        pass


class PersonalLoan(Loan):
    def get_interest_rate(self):
        return 0.1

    def display(self):
        return "Personal Loan"


class MortgageLoan(Loan):
    def get_interest_rate(self):
        return 0.05

    def display(self):
        return "Mortgage Loan"


class LoanFactory:

    def __init__(self):
        self._loans = {
            "PERSONAL": PersonalLoan,
            "MORTGAGE": MortgageLoan
        }

    def register_loan(self, type, loan):
        self._loans[type] = loan

    def get_loan(self, type):
        loan_creator = self._loans.get(type)
        if not loan_creator:
            raise ValueError(type)
        return loan_creator()

    def create_loan(self, type="PERSONAL"):
        return self.get_loan(type)


def loans_client():
    loan_factory = LoanFactory()

    personal_loan = loan_factory.create_loan("PERSONAL")

    print(f"The type of object created: {type(personal_loan)}")
    print(
        f"The interests rate {personal_loan.__class__.__name__} is: {personal_loan.get_interest_rate()}")


if __name__ == '__main__':
    loans_client()
