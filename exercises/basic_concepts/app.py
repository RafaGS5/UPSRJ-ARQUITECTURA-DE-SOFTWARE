from flask import Flask, jsonify
import sys, os
from logging import INFO, DEBUG

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from py_utils.logger import set_logging, plog

set_logging(log_file="application.log")

app = Flask(__name__)


class UserStorage:
    def all_users(self):
        plog("Retrieving all users", DEBUG)
        return [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Rafa"}
        ]


class UserLogic:
    def __init__(self, storage: UserStorage):
        plog("UserLogic ready", DEBUG)
        self.storage = storage

    def fetch_all(self):
        plog("Returning users", INFO)
        return self.storage.all_users()


logic = UserLogic(UserStorage())


@app.route("/users")
def list_users():
    return jsonify(logic.fetch_all())


if __name__ == "__main__":
    plog("Running Flask server", INFO)
    app.run(debug=True)
