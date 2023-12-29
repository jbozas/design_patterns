from abc import ABC, abstractmethod
from typing import List


class Package:
    pass


class Observer(ABC):
    """
    An observer must provide a method to be called by the Subject whenever
    something happen.
    """

    @abstractmethod
    def update(self, package: Package) -> None:
        pass


class Subject(ABC):
    """
    A subject has objects looking for it. Must provide a mechanism
    to add, remove or notify observers.
    """

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)


class Package(Subject):
    """
    Concrete Subject. It has various objects that depend on its state.
    """

    def __init__(self, package_id: str) -> None:
        self._package_id = package_id
        self._state = "Created"
        self._observers: List[Observer] = []

    def get_state(self) -> str:
        return self._state

    def set_state(self, state: str) -> None:
        self._state = state
        self.notify_observers()


class PaymentProcessor(Observer):
    """
    One of the concrete observers
    """

    def update(self, package: Package) -> None:
        if package.get_state() == "Delivered_and_Confirmed":
            self.finalize_payment(package)

    def finalize_payment(self, package: Package) -> None:
        print(f"Payment finalized for package {package._package_id}")


# Client code
if __name__ == "__main__":
    # Creating package and observer instances
    package1 = Package("123")
    payment_processor = PaymentProcessor()

    # Adding the observer to the package
    package1.add_observer(payment_processor)

    # Simulating state changes of the package
    package1.set_state("In Transit")
    package1.set_state("Delivered")
