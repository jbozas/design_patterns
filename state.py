from abc import ABC, abstractmethod


class PackageState(ABC):
    @abstractmethod
    def add_item(self, package, item):
        pass

    @abstractmethod
    def review_package(self, package):
        pass

    @abstractmethod
    def enter_shipping_info(self, package, info):
        pass

    @abstractmethod
    def process_payment(self, package):
        pass

    @abstractmethod
    def delivered(self, package, info):
        pass


class ProcessingState(PackageState):
    def add_item(self, package, item):
        print(
            f"Package {package._package_id}: Adding item {item} to the package")

    def enter_shipping_info(self, package, info):
        print(
            f"Package {package._package_id}: Entering shipping information: {info}")

    def process_payment(self, package):
        print(f"Package {package._package_id}: Processing payment")

    def delivered(self, package):
        print(
            f"Package {package._package_id}: cannot be mark as delivered due its not confirmed yet.")


class InTransitState(PackageState):
    def add_item(self, package, item):
        print(
            f"Package {package._package_id}: Cannot add items while the package is in transit")

    def enter_shipping_info(self, package, info):
        print(
            f"Package {package._package_id}: Cannot change shipping information while in transit")

    def process_payment(self, package):
        print(
            f"Package {package._package_id}: Cannot process payment while in transit")

    def delivered(self, package):
        print(
            f"Package {package._package_id}: will be mark as delivered.")


class Package:
    def __init__(self, package_id):
        self._package_id = package_id
        self._state = ProcessingState()

    def set_state(self, state: PackageState):
        self._state = state

    def add_item(self, item):
        self._state.add_item(self, item)

    def enter_shipping_info(self, info):
        self._state.enter_shipping_info(self, info)

    def process_payment(self):
        self._state.process_payment(self)

    def delivered(self):
        self._state.delivered(self)
