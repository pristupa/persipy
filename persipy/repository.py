from abc import abstractmethod
from typing import Generic
from typing import Iterable
from typing import Optional
from typing import TypeVar

T = TypeVar('T')
K = TypeVar('K')


class Repository(Generic[T, K]):
    pass


class CRUDRepository(Repository, Generic[T, K]):
    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def delete(self, entity: T):
        pass

    @abstractmethod
    def delete_many(self, entities: Iterable[T]):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id_: K):
        pass

    @abstractmethod
    def exists_by_id(self, id_: K) -> bool:
        pass

    @abstractmethod
    def find_all(self) -> Iterable[T]:
        pass

    @abstractmethod
    def find_all_by_id(self, ids: Iterable[K]) -> Iterable[T]:
        pass

    @abstractmethod
    def find_by_id(self, id_: K) -> Optional[T]:
        pass

    @abstractmethod
    def save(self, entity: T) -> T:
        pass

    @abstractmethod
    def save_many(self, entities: Iterable[T]) -> Iterable[T]:
        pass
