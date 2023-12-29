from abc import ABC, abstractmethod
from decimal import Decimal


class Loan:
    pass


class Client:
    pass


class LoanBuilder(ABC):
    """
    Abstraction that defines every method that a Concrete Builder
    should have. Each one of the mentioned classes must implement them.

    They are a sequence of methods that depend on the Loan type and need to
    be settled as the Loan are being created.
    Maybe some of them do not depend on the Loan type and you can define them right here,
    an avoid a huge amount of code duplication.
    """

    @abstractmethod
    def build_amount(self):
        pass

    @abstractmethod
    def build_term(self):
        pass

    @abstractmethod
    def build_rate(self):
        pass

    @abstractmethod
    def build_customer(self):
        pass

    @abstractmethod
    def build_status(self):
        pass

    @abstractmethod
    def get_loan(self):
        pass


class PersonalLoanBuilder(LoanBuilder):
    """
    A specific type of Loan that justify the implementation
    of an abstract class LoanBuilder because its variables.
    """

    def build_amount(self, amount: Decimal):
        self.loan.amount = amount

    def build_term(self, term: int):
        self.loan.term = term

    def build_rate(self, rate: Decimal):
        self.loan.rate = rate

    def build_customer(self, customer: Client):
        self.loan.customer = customer

    def build_status(self):
        self.loan.status = "Pending"

    def get_loan(self) -> Loan:
        return self.loan


class MortgageLoanBuilder(LoanBuilder):
    """
    Another type of Loan associated with Mortgage Loans.
    They are different than Personal Loans, they have another
    rules to create themseleves such as a specific state, term
    or amount.
    """

    def build_amount(self, amount: Decimal):
        self.loan.amount = amount * 1000

    def build_term(self, term: int):
        self.loan.term = term * 12

    def build_rate(self, rate: Decimal):
        self.loan.rate = rate * 1.5

    def build_customer(self, customer: Client):
        self.loan.customer = customer

    def build_status(self):
        self.loan.status = "Approved"

    def get_loan(self) -> Loan:
        return self.loan


class LoanDirector:
    """
    Class in charge of every Loan creation step orchestation.
    They know exactly what a Loan needs to be created.
    """
    def __init__(self, builder: LoanBuilder):
        self.builder = builder

    def construct_loan(self, amount, term, rate) -> Loan:
        self.builder.build_amount(amount)
        self.builder.build_term(term)
        self.builder.build_rate(rate)
        self.builder.build_status()
        return self.builder.get_loan()


def loans_client():
    """
    This simulates a client that needs or use Loans.
    It just needs to create a concrete LoanBuilder and pass it
    to a LoanDirector to return a concrete Loan object.
    """
    personal_loan_builder = PersonalLoanBuilder()
    mortgage_loan_builder = MortgageLoanBuilder()

    loan_director = LoanDirector(personal_loan_builder)
    personal_loan = loan_director.construct_loan(5000, 12, 8, "John Doe", 60000)

    loan_director = LoanDirector(mortgage_loan_builder)
    mortgage_loan = loan_director.construct_loan(300, 30, 5, "Jane Smith", 80000)


if __name__ == "__main__":
    loans_client()
