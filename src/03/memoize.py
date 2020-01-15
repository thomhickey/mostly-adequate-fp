from typing import Callable, Any
import json


def memoize(f: Callable[..., Any]) -> Callable[..., Any]:
    cache = {}

    def ret(*args) -> Callable[..., Any]:
        arg_str = json.dumps(args)
        cache[arg_str] = cache[arg_str] if arg_str in cache else f(*args)
        return cache[arg_str]

    return ret


squareNumber = memoize(lambda x: x * x)
print(squareNumber(4))
print(squareNumber(4))
print(squareNumber(5))
print(squareNumber(5))
