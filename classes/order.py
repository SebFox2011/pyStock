from app import db
from datetime import datetime


class Order(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, primary_key=True)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(20), nullable=False)# ongoing, completed, error
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def printInfos(self):
        print('[{}] Order {} - {} € : \n{}'.format(self.id, self.nom, self.prix, self.description))

    @classmethod
    def createOrder(self):
        nom = input("Quel est le nom de la commande: ")
        description = input("Quel est la description de l'article: ")
        prix = int(input("Quel est le prix: "))
        order = Order(nom, description, prix)
        return order  # retourné pour pouvoir gérer le stock