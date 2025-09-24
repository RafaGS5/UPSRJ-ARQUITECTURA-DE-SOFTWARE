# entity_server.py

class UserRepository:
    def get_all(self):
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bod"}]

    def find_by_id(self, user_id):
        return next((u for u in self.get_all() if u["id"] == user_id), None)

    def get_by_keyword(self, keyword):
        return [u for u in self.get_all() if keyword.lower() in u["name"].lower()]


class EntityService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    # Estos métodos deben existir para pasar los tests
    def get_all(self):
        return self.repository.get_all()

    def find_by_id(self, user_id):
        return self.repository.find_by_id(user_id)

    def get_by_keyword(self, keyword):
        return self.repository.get_by_keyword(keyword)