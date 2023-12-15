class LegacyLoanRequestSystem:
    def get_client_scoring(self, client_id):
        return 'Some old but necessary function that retrieves value information.'


class NewLoanRequestSystem:
    def is_client_enabled_for_loan(self, loan_amount: int, client_id: int):
        """
        Given a specific amount and a client, it returns if the client
        is enabled to request a new Loan.
        """
        return 'A new function needed to know if the client is enabled to request it.'


class LegacyLoanRequestAdapter(NewLoanRequestSystem):
    def __init__(self):
        self.old_system = LegacyLoanRequestSystem

    def get_and_adapt_client_data(self, loan_amount, client_id):
        legacy_data = self.old_system().get_client_scoring(client_id)
        # some operation to define whether the client can or cannot
        # request the Loan with a new result expected by the system.
        return legacy_data

    def is_client_enabled_for_loan(self, loan_amount: int, client_id: int):
        return self.get_and_adapt_client_data(loan_amount, client_id)


if __name__ == "__main__":
    # The client needs both opinions to define if its enabled to request the loan
    loan_amount = 100_000
    client_id = 2
    for request_system in [NewLoanRequestSystem, LegacyLoanRequestAdapter]:
        print(request_system().is_client_enabled_for_loan(loan_amount, client_id))
