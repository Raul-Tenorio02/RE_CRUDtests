from app import db

class Item(db.Model): #definindo a tabela item
    id = db.Column(db.Integer, primary_key=True)
    nome_item = db.Column(db.String(100), nullable=False )
    descricao = db.Column(db.String(255), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    icon = db.Column(db.String(100))

    def __repr__(self):
        return f"<Item {self.nome_item}>"
    
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    p1 = db.Column(db.String(50), nullable=False)
    p2 = db.Column(db.String(50), nullable=False)
    p3 = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'