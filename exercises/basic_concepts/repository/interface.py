from abc import ABC, abstractmethod
from typing import Optional, List, Dict

class EntityRepository(ABC):
    """Interfaz base que debe implementar cualquier repositorio de entidad."""

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_by_keyword(self, keyword: str) -> Optional[Dict]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Dict]:
        pass

    @abstractmethod
    def get_users_for_group(self, group_id: int) -> List[Dict]:
        pass

    @abstractmethod
    def get_groups_for_user(self, user_id: int) -> List[Dict]:
        pass
