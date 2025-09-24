from flask import Blueprint, render_template, request
from logging import INFO
from py_utils.logger import plog

# Importamos la lógica de negocio
from ..server.user_service import UserService, LocalUserRepository

# Definimos un Blueprint en lugar de una app completa
bp = Blueprint("routes", __name__)

# Instanciamos el servicio real
user_service = UserService(LocalUserRepository())

@bp.route("/")
def index():
    return render_template("search.html")

@bp.route("/users")
def get_users():
    plog("Fetching all users", INFO)
    users = user_service.list_users()
    return render_template("result.html", users=users)

@bp.route("/users/<int:user_id>")
def get_user(user_id):
    plog(f"Fetching user with ID {user_id}", INFO)
    user = user_service.get_user(user_id)
    if not user:
        return render_template("error.html", message="Usuario no encontrado"), 404
    return render_template("result.html", users=[user])

@bp.route("/search")
def search():
    keyword = request.args.get("q", "")
    plog(f"Searching users with keyword: {keyword}", INFO)
    results = user_service.filter_users(keyword)
    return render_template("result.html", users=results)
