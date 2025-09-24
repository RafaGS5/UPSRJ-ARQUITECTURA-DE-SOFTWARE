class LocalUserRepository:
    """
    Capa de acceso a datos.
    Aquí simulamos una base de datos con una lista en memoria.
    """
    def get_all_users(self):
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]

    def find_user_by_id(self, user_id):
        return next((u for u in self.get_all_users() if u["id"] == user_id), None)

    def search_users(self, keyword):
        return [u for u in self.get_all_users() if keyword.lower() in u["name"].lower()]


class UserService:
    """
    Capa de negocio.
    Usa el repositorio y expone métodos que serán utilizados por los controladores (routes).
    """
    def __init__(self, repository: LocalUserRepository):
        self.repository = repository

    def list_users(self):
        return self.repository.get_all_users()

    def get_user(self, user_id):
        return self.repository.find_user_by_id(user_id)

    def filter_users(self, keyword):
        return self.repository.search_users(keyword)