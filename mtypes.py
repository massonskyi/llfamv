from typing import NewType, Any, TypeVar, Generic, Type, Union, List

char = NewType('char', str)

T = TypeVar('T')


class Result(Generic[T]):
    def __init__(self, *args):
        self._items = tuple(args)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __contains__(self, value):
        return value in self._items

    def add_result(self, value: T):
        self._items += (value,)
        return self

    def get_results(self):
        return self._items

    def count(self, value):
        return self._items.count(value)

    def index(self, value, start=None, stop=None):
        return self._items.index(value, start, stop)

    @classmethod
    def of(cls, item_type: Type[T]):
        return cls[item_type](*tuple(item_type() for _ in range(0)))

    def __class_getitem__(cls, item_type: Type[T]):
        return cls(item_type())
