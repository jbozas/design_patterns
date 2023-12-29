a = None
print(id(a) == id(type(a)()))


class SingletonObject:
    _instance = None

    def __new__(self):
        """
        Redefine the SingletonObject creation to ensure that
        one and just one instance of this class can be created.
        """
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance


print(id(SingletonObject()) == id(SingletonObject()))
