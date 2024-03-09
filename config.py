from mtypes import char

HOST_PATTERN: str | list[char] \
    = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

PORT_PATTERN: str | list[char] \
    = r'^\d{1,5}$'
