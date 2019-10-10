from app import db
from datetime import datetime


class Order(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, primary_key=True)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(20), nullable=False)# ongoing, completed, error
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def update(self, values):
        self.name = values['orderName']
        db.session.commit()
