from flask import Flask, jsonify

import sys
import os
from logging import DEBUG, INFO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Configuración de logging
set_logging(log_file='app.log')

class UserRepository:
    """Repository component that handles user data access."""

    def get_all(self):
        """Returns a static list of user dictionaries."""
        plog("Fetching users from repository", DEBUG)
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bod"}
        ]


class UserService:
    """Service component that contains business logic."""

    def __init__(self, repository: UserRepository):
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        plog("Listing users from service", INFO)
        return self.repository.get_all()


# ✅ Aquí ya están en el ámbito global, no dentro de la clase
app = Flask(__name__)
user_service = UserService(UserRepository())

@app.route("/users")
def get_users():
    """HTTP endpoint that returns a JSON list of users."""
    plog("Received request for /users endpoint", INFO)
    users = user_service.list_users()
    return jsonify(users)


if __name__ == "__main__":

    plog("Starting Flask app", INFO)
    app.run(debug=True)