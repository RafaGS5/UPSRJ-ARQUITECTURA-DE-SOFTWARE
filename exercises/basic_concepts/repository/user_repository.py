import json
import os
from typing import Optional, List, Dict
from exercises.basic_concepts.repository.interface import EntityRepository

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class UserRepository(EntityRepository):
    """Repositorio para usuarios (implementa EntityRepository)."""

    def _users_path(self):
        return os.path.join(BASE_DIR, 'repository', 'users.json') if False else os.path.join(os.path.dirname(__file__), 'users.json')

    def _groups_path(self):
        return os.path.join(os.path.dirname(__file__), 'groups.json')

    def get_all(self) -> List[Dict]:
        path = os.path.join(os.path.dirname(__file__), 'users.json')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_by_keyword(self, keyword: str) -> Optional[Dict]:
        users = self.get_all()
        key = keyword.strip().lower()
        for u in users:
            if str(u.get('id')) == key or u.get('name', '').lower() == key:
                return u
        return None

    def get_by_id(self, id: int) -> Optional[Dict]:
        users = self.get_all()
        for u in users:
            if int(u.get('id')) == int(id):
                return u
        return None

    def get_users_for_group(self, group_id: int) -> List[Dict]:
        # Not primary responsibility of UserRepository, but implement safe fallback
        users = self.get_all()
        gid = int(group_id)
        return [u for u in users if gid in u.get('groups', [])]

    def get_groups_for_user(self, user_id: int) -> List[Dict]:
        # Read groups.json and return groups that contain this user id
        path = os.path.join(os.path.dirname(__file__), 'groups.json')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                groups = json.load(f)
        except FileNotFoundError:
            return []
        uid = int(user_id)
        return [g for g in groups if uid in g.get('members', [])]
