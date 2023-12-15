a = None
print(id(a) == id(type(a)()))


class SingletonObject:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance

print(id(SingletonObject()) == id(SingletonObject()))
