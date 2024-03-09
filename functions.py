import functools
import re
from typing import Tuple


def __format__(func, arg: dict):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = args[0]
        if not re.match(arg["regex"], s):
            raise ValueError(f'String {s} does not match format {arg}')
        numbers = [int(x) for x in s.split('.')]
        if not arg.get("is_port", False):
            if not all(0 <= n <= 255 for n in numbers):
                raise ValueError(f'String {s} contains invalid numbers')
        return func(*args, **kwargs)

    return wrapper


def _get_local_address() -> tuple[str | int, ...]:
    """Returns the local IP address and port of this device."""
    import socket

    # Get the local address
    local_address: str = socket.gethostbyname(socket.gethostname())

    # Get a random free port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((local_address, 0))
    random_free_port: int = sock.getsockname()[1]
    sock.close()

    return tuple([local_address, random_free_port])
