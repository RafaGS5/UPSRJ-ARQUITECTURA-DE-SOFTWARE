import json
import os
from logging import DEBUG
try:
    from py_utils.logger import plog
except Exception:
    def plog(msg, level=DEBUG):
        print(msg)

class UserRepository:
    def __init__(self):
        base = os.path.dirname(__file__)
        self.users_file = os.path.join(base, "users.json")
        self.groups_file = os.path.join(base, "groups.json")
        self.memberships_file = os.path.join(base, "memberships.json")

    def _read_json(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            plog(f"File not found: {path}", DEBUG)
            return []
        except Exception as e:
            plog(f"Error reading {path}: {e}", DEBUG)
            return []

    def get_all(self):
        return self._read_json(self.users_file)

    def get_by_id(self, id):
        try:
            id_int = int(id)
        except Exception:
            return None
        for u in self.get_all():
            try:
                if int(u.get("id")) == id_int:
                    return u
            except Exception:
                continue
        return None

    def get_by_keyword(self, keyword: str):
        if not keyword:
            return None
        kw = keyword.lower()
        for u in self.get_all():
            name = str(u.get("name", "")).lower()
            email = str(u.get("email", "")).lower()
            if kw in name or kw in email:
                return u
        return None

    # 🔹 devuelve todos los usuarios de un grupo
    def get_users_for_group(self, group_id):
        users = self.get_all()
        groups = self._read_json(self.groups_file)
        memberships = self._read_json(self.memberships_file)

        gid = int(group_id)
        result = []

        # Caso 1: revisar memberships.json
        if memberships:
            user_ids = [int(m["user_id"]) for m in memberships if int(m["group_id"]) == gid]
            result = [u for u in users if int(u.get("id")) in user_ids]
            if result:
                return result

        # Caso 2: revisar groups.json con campo members
        for g in groups:
            if int(g.get("id")) == gid:
                members = g.get("members") or g.get("user_ids") or []
                try:
                    member_ids = [int(x) for x in members]
                except Exception:
                    member_ids = [int(x) for x in members if str(x).isdigit()]
                result = [u for u in users if int(u.get("id")) in member_ids]
                return result

        # Caso 3: revisar users.json con campo groups
        for u in users:
            ug = u.get("groups") or []
            try:
                if any(int(gid) == int(x) for x in ug):
                    result.append(u)
            except Exception:
                continue
        return result

    # 🔹 devuelve todos los grupos de un usuario
    def get_groups_for_user(self, user_id):
        groups = self._read_json(self.groups_file)
        memberships = self._read_json(self.memberships_file)
        user = self.get_by_id(user_id)
        if not user:
            return []

        uid = int(user_id)

        # Caso 1: revisar campo "groups" en el usuario
        if user.get("groups"):
            try:
                gids = [int(x) for x in user["groups"]]
            except Exception:
                gids = [int(x) for x in user["groups"] if str(x).isdigit()]
            return [g for g in groups if int(g.get("id")) in gids]

        # Caso 2: revisar memberships.json
        if memberships:
            try:
                gids = [int(m["group_id"]) for m in memberships if int(m["user_id"]) == uid]
                return [g for g in groups if int(g.get("id")) in gids]
            except Exception:
                pass

        # Caso 3: revisar campo members en cada grupo
        result = []
        for g in groups:
            members = g.get("members") or g.get("user_ids") or []
            try:
                if any(int(x) == uid for x in members):
                    result.append(g)
            except Exception:
                continue
        return result

