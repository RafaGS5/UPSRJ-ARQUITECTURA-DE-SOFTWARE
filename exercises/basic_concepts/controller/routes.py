from flask import Flask, jsonify, request, render_template
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

from exercises.basic_concepts.repository.user_repository import UserRepository
from exercises.basic_concepts.repository.group_repository import GroupRepository

from flask import Blueprint, render_template, request
from exercises.basic_concepts.service.entity_service import EntityService
from flask import jsonify
from exercises.basic_concepts.repository.user_repository import UserRepository

bp = Blueprint("routes", __name__)
routes = Blueprint("routes", __name__)

app = Flask(__name__, template_folder="../templates")
user_repository = UserRepository()
group_repository = GroupRepository()

user_service = EntityService(user_repository)
group_service = EntityService(group_repository)


@routes.route("/users", methods=["GET"])
def get_users():
    users = UserRepository().get_all()
    return jsonify(users), 200



@bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    search_type = request.args.get("type", "user")   # user o group
    mode = request.args.get("mode", "keyword")       # keyword o id

    if not query:
        return render_template("search.html")

    if search_type == "user":
        if mode == "id":
            try:
                user = user_service.get_by_id(int(query))
            except ValueError:
                user = None
        else:
            user = user_service.get_by_keyword(query)

        if not user:
            return render_template("error.html", message="No se encontró ningún usuario con ese criterio.")

        groups = GroupRepository().get_groups_for_user(user["id"])
        return render_template("result.html", user=user, groups=groups)

    elif search_type == "group":
        if mode == "id":
            try:
                group = group_service.get_by_id(int(query))
            except ValueError:
                group = None
        else:
            group = group_service.get_by_keyword(query)

        members = []
        if group:
            members = UserRepository().get_users_for_group(group["id"])
        return render_template("group.html", group=group, members=members)

    return render_template("error.html", message="Tipo de búsqueda no válido")