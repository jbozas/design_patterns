# Builder

class LoanBuilder:
    def build_amount(self):
        pass

    def build_term(self):
        pass

    def build_rate(self):
        pass

    def build_customer(self):
        pass

    def build_status(self):
        pass

    def get_loan(self):
        pass


class PersonalLoanBuilder(LoanBuilder):

    def build_amount(self, amount):
        self.loan.amount = amount

    def build_term(self, term):
        self.loan.term = term

    def build_rate(self, rate):
        self.loan.rate = rate

    def build_customer(self, customer):
        self.loan.customer = customer

    def build_status(self):
        self.loan.status = "Pending"

    def get_loan(self):
        return self.loan


class MortgageLoanBuilder(LoanBuilder):

    def build_amount(self, amount):
        self.loan.amount = amount * 1000

    def build_term(self, term):
        self.loan.term = term * 12

    def build_rate(self, rate):
        self.loan.rate = rate * 1.5

    def build_customer(self, customer):
        self.loan.customer = customer

    def build_status(self):
        self.loan.status = 'Approved'

    def get_loan(self):
        return self.loan


class LoanDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_loan(self, amount, term, rate):
        self.builder.build_amount(amount)
        self.builder.build_term(term)
        self.builder.build_rate(rate)
        self.builder.build_status()
        return self.builder.get_loan()


def loans_client():
    personal_loan_builder = PersonalLoanBuilder()
    mortgage_loan_builder = MortgageLoanBuilder()

    loan_director = LoanDirector(personal_loan_builder)
    personal_loan = loan_director.construct_loan(
        5000, 12, 8, "John Doe", 60000)

    loan_director = LoanDirector(mortgage_loan_builder)
    mortgage_loan = loan_director.construct_loan(
        300, 30, 5, "Jane Smith", 80000)


if __name__ == '__main__':
    loans_client()
