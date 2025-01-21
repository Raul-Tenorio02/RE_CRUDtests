import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for
from app import db  # Apenas importa o banco de dados
from app.models import Item, Usuario  # Importa os modelos necessários

# Configuração do upload
UPLOAD_FOLDER = 'app/static/images/item_icons'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define o Blueprint
blueprint = Blueprint('main', __name__)

# Página inicial
@blueprint.route('/')
def index():
    return render_template('index.html')  # Renderiza a página inicial

# Página do formulário
@blueprint.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form["nome"]
        email = request.form["email"]
        p1 = request.form["p1"]
        p2 = request.form["p2"]
        p3 = request.form["p3"]


        novo_usuario = Usuario(nome=nome, email=email, p1=p1, p2=p2, p3=p3)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for('main.index', success=True))  # Redireciona para a página inicial
    return render_template('form.html')

@blueprint.route('/form_respostas')
def form_respostas():
    usuarios = Usuario.query.all()
    return render_template('form_respostas.html', usuarios=usuarios)

# Página para adicionar um item
@blueprint.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        nome_item = request.form["nome_item"]
        descricao = request.form["descricao"]
        quantidade = int(request.form["quantidade"])
        icon = None

        # Upload do ícone
        if 'icone' in request.files:
            file = request.files['icone']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                icon = f'images/item_icons/{filename}'  # Caminho relativo

        # Adiciona o item ao banco
        novo_item = Item(nome_item=nome_item, descricao=descricao, quantidade=quantidade, icon=icon)
        db.session.add(novo_item)
        db.session.commit()

        return redirect(url_for('main.list_items'))

    return render_template("add_item.html")

# Página para listar itens
@blueprint.route("/items")
def list_items():
    itens = Item.query.all()
    return render_template("list_items.html", itens=itens)

# Função para deletar um item
@blueprint.route("/delete_item/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)  # Busca o item pelo id
    db.session.delete(item)
    db.session.commit()  # Confirma a exclusão
    return redirect(url_for('main.list_items'))  # Redireciona para a página de listagem

# Função para editar um item
@blueprint.route("/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == "POST":
        item.nome_item = request.form["nome_item"]
        item.descricao = request.form["descricao"]
        item.quantidade = int(request.form["quantidade"])

        # Tratamento do upload do ícone
        if 'icone' in request.files:
            file = request.files['icone']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                item.icon = f'images/item_icons/{filename}'  # Caminho relativo ao ícone

        db.session.commit()
        return redirect(url_for('main.list_items'))

    return render_template("edit_item.html", item=item)