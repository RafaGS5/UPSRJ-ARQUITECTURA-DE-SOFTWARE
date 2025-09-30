import os
from flask import Flask, render_template, request, redirect, url_for
from exercises.basic_concepts.repository.user_repository import UserRepository
from exercises.basic_concepts.repository.group_repository import GroupRepository
from exercises.basic_concepts.service.entity_service import EntityService

# --- Ajuste crítico: calcular la ruta absoluta a la carpeta templates dentro de basic_concepts
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # .. => basic_concepts
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Comprobación temprana para dar un error claro si la carpeta no existe
if not os.path.isdir(TEMPLATE_DIR):
    raise RuntimeError(f"Templates folder not found at: {TEMPLATE_DIR!r}")

# Crear la app indicando la carpeta de templates absoluta
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# --- resto del archivo (servicios, rutas, etc.)
user_repo = UserRepository()
group_repo = GroupRepository()

user_service = EntityService(user_repo)
group_service = EntityService(group_repo)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        q = request.form.get('q', '').strip()
        tipo = request.form.get('type', 'user')
    else:
        q = request.args.get('q', '').strip()
        tipo = request.args.get('type', 'user')

    if not q:
        return render_template('search.html', message=None)

    if tipo == 'user':
        user = user_service.get_by_keyword(q)
        if not user:
            return render_template('error.html', message=f'Usuario \"{q}\" no encontrado.')
        groups = user_service.get_groups_for_user(user.get('id'))
        return render_template('result.html', result={'user': user, 'groups': groups})

    elif tipo == 'group':
        group = group_service.get_by_keyword(q)
        if not group:
            return render_template('error.html', message=f'Grupo \"{q}\" no encontrado.')
        users = group_service.get_users_for_group(group.get('id'))
        return render_template('result.html', result={'group': group, 'users': users})

    else:
        return render_template('error.html', message='Tipo inválido.')
