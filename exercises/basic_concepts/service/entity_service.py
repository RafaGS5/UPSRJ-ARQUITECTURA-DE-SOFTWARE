from typing import Any
from exercises.basic_concepts.repository.interface import EntityRepository

class EntityService:
    """Servicio genérico que funciona con cualquier EntityRepository."""

    def __init__(self, repository: EntityRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_by_keyword(self, keyword):
        return self.repository.get_by_keyword(keyword)

    def get_users_for_group(self, group_id):
        return self.repository.get_users_for_group(group_id)

    def get_groups_for_user(self, user_id):
        return self.repository.get_groups_for_user(user_id)
