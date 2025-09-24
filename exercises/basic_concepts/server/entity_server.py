class UserRepository:

    def fetch_users(self):
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Rafa"}
        ]

    def get_user(self, user_id: int):
  
        for u in self.fetch_users():
            if u["id"] == user_id:
                return u
        return None

    def search_by_name(self, keyword: str):

        keyword = keyword.lower()
        return [u for u in self.fetch_users() if keyword in u["name"].lower()]


class EntityService:
    
    def __init__(self, repository: UserRepository):
        self.repo = repository

    def get_all(self):
        return self.repo.fetch_users()

    def find_by_id(self, user_id):
        return self.repo.get_user(user_id)

    def get_by_keyword(self, keyword):
        return self.repo.search_by_name(keyword)