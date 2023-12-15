from abc import ABC, abstractmethod


class Package:
    pass


class ServiceStrategy(ABC):
    """
    The base class. Will contain the methods that the Client needs and
    the concrete classes will implement it.
    Maybe you have similar methods to every concrete strategy that you may
    define here.
    """

    @abstractmethod
    def create_package(self, package_data: dict) -> Package:
        """
        The Package creation will be different depending on the Package's service.
        """
        pass


class AtClientsHouseStrategy(ServiceStrategy):
    def create_package(self, package_data: dict) -> Package:
        """
        Apply all the logic related to deliver the Package at the
        Client's House.
        """
        contents = package_data.get("contents", "")
        delivery_location = "Client's House"
        contents = f"Special handling for home delivery: {contents}"
        return Package(contents, delivery_location)


class AtWithdrawalPointStrategy(ServiceStrategy):
    def create_package(self, package_data: dict) -> Package:
        """
        Apply all the logic related to deliver the Package at the
        WithDrawal Point.
        """
        contents = package_data.get("contents", "")
        delivery_location = "Withdrawal Point"
        contents = f"Standard handling for withdrawal point: {contents}"
        return Package(contents, delivery_location)


class ServiceContext:

    def __init__(self, strategy: ServiceStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> ServiceStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ServiceStrategy) -> None:
        self._strategy = strategy

    def create_package(self, package_data: dict) -> Package:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        print("Context: Creating a Package using the strategy (not sure how it'll do it)")
        return self._strategy.create_package(package_data)


if __name__ == "__main__":
    context = ServiceContext(AtClientsHouseStrategy())
    context.create_package({})
