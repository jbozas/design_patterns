from abc import ABC, abstractmethod


class Package:
    """
    The Package itself.
    Has a lot of responsability and some of them
    depend on its state so its being delegated to it.
    """

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


class Item:
    pass


class PackageState(ABC):
    """
    Every state should have each one of them
    and implement them if they need to.
    This provides a flexible way to ensure
    polimorfism depending on the Package state.
    """

    @abstractmethod
    def add_item(self, package: Package, item: Item):
        """
        Add a new Item to the Cart.
        """
        pass

    @abstractmethod
    def review_package(self, package: Package):
        pass

    @abstractmethod
    def enter_shipping_info(self, package: Package, info: str):
        """
        Enter a shipping address to be delivered.
        """
        pass

    @abstractmethod
    def process_payment(self, package: Package):
        """
        Stops blocking the Seller's payment.
        """
        pass

    @abstractmethod
    def delivered(self, package: Package, info: str):
        """
        Sets the Package as delivered.
        """
        pass


class ProcessingState(PackageState):
    """
    Processing state. When a Package its being created but not confirmed.
    Card can change, shipping address to, but its not confirmed so it cannot
    be delivered and the payment must be blocked.
    """

    def add_item(self, package: Package, item: Item):
        print(f"Package {package._package_id}: Adding item {item} to the package")

    def enter_shipping_info(self, package: Package, info: str):
        print(f"Package {package._package_id}: Entering shipping information: {info}")

    def process_payment(self, package: Package):
        print(f"Package {package._package_id}: Processing payment")

    def delivered(self, package: Package):
        print(
            f"Package {package._package_id}: cannot be mark as delivered due its not confirmed yet."
        )


class InTransitState(PackageState):
    """
    The Package already has been confirmed and its traveling to destiny.
    Card cannot be change but Package can be mark as delivered.
    """

    def add_item(self, package, item):
        print(
            f"Package {package._package_id}: Cannot add items while the package is in transit"
        )

    def enter_shipping_info(self, package, info):
        print(
            f"Package {package._package_id}: Cannot change shipping information while in transit"
        )

    def process_payment(self, package):
        print(f"Package {package._package_id}: Cannot process payment while in transit")

    def delivered(self, package):
        print(f"Package {package._package_id}: will be mark as delivered.")
