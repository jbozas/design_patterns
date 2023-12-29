# Factory method
from abc import ABC, abstractmethod


class Loan(ABC):
    """
    Loan Abstraction. There are different types of Loans
    and every type should implement each one of the responsabilities
    this abstract class defines.
    """

    @abstractmethod
    def get_interest_rate(self):
        """
        Returns a interest rate, depends on the Loan type.
        """
        pass

    @abstractmethod
    def display(self):
        """
        Another responsability that the Concrete classes should define and
        implement regarding its type.
        """
        pass


class PersonalLoan(Loan):
    def get_interest_rate(self) -> float:
        return 0.1

    def display(self) -> str:
        return "Personal Loan"


class MortgageLoan(Loan):
    def get_interest_rate(self) -> float:
        return 0.05

    def display(self) -> str:
        return "Mortgage Loan"


class LoanFactory:
    def __init__(self):
        self._loans = {"PERSONAL": PersonalLoan, "MORTGAGE": MortgageLoan}

    def register_loan(self, type: str, loan: Loan):
        """
        This method allows the Loan's client to add a new Loan type to the
        already available.
        """
        self._loans[type] = loan

    def get_loan(self, type: str):
        """
        Obtains the concrete Loan depending on the Loan type requested.
        """
        loan_creator = self._loans.get(type)
        if not loan_creator:
            raise ValueError(type)
        return loan_creator()

    def create_loan(self, type: str = "PERSONAL") -> Loan:
        """
        Receives a Loan type and returns the instance already created.
        """
        return self.get_loan(type)


def loans_client():
    """
    This simulates a client that needs or use Loans.
    Just need to know which type of Loan it wants and request it
    to the LoanFactory.
    """
    loan_factory = LoanFactory()

    personal_loan = loan_factory.create_loan("PERSONAL")

    print(f"The type of object created: {type(personal_loan)}")
    print(
        f"The interests rate {personal_loan.__class__.__name__} is: {personal_loan.get_interest_rate()}"
    )


if __name__ == "__main__":
    loans_client()
