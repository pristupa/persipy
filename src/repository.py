from abc import abstractmethod
from typing import Generic
from typing import TypeVar

T = TypeVar('T')
K = TypeVar('K')


class Repository(Generic[T, K]):
    @abstractmethod
    def get(self, id_: K) -> T:
        pass
