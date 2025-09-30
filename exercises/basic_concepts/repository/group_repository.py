import json
import os
from typing import Optional, List, Dict
from exercises.basic_concepts.repository.interface import EntityRepository

class GroupRepository(EntityRepository):
    """Repositorio para grupos (implementa EntityRepository)."""

    def get_all(self) -> List[Dict]:
        path = os.path.join(os.path.dirname(__file__), 'groups.json')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_by_keyword(self, keyword: str) -> Optional[Dict]:
        groups = self.get_all()
        key = keyword.strip().lower()
        for g in groups:
            if str(g.get('id')) == key or g.get('name', '').lower() == key:
                return g
        return None

    def get_by_id(self, id: int) -> Optional[Dict]:
        groups = self.get_all()
        for g in groups:
            if int(g.get('id')) == int(id):
                return g
        return None

    def get_users_for_group(self, group_id: int) -> List[Dict]:
        # Return users who belong to the group (read users.json)
        users_path = os.path.join(os.path.dirname(__file__), 'users.json')
        try:
            with open(users_path, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except FileNotFoundError:
            return []
        gid = int(group_id)
        return [u for u in users if gid in u.get('groups', [])]

    def get_groups_for_user(self, user_id: int) -> List[Dict]:
        # Not primary for GroupRepository; return empty
        return []
