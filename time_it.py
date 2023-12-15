from typing import Callable
from time import perf_counter
from functools import wraps


def time_it(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapped(*args, **kwargs):
        print('Timer init.')
        started = perf_counter()
        result = fn(*args, **kwargs)
        elapsed_time = round(perf_counter() - started, 5)
        print(f'Timer finalized with an amount of time {elapsed_time:.5f}')
        return result

    return wrapped


@time_it
def testing_time(a: int, b: int) -> int:
    return a ** b


if __name__ == '__main__':
    testing_time(4, 10000)
