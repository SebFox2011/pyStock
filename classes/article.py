from app import db


class Article(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, primary_key=True)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    nom = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    prix = db.Column(db.Integer, nullable=False)

    def printInfos(self):
        print('[{}] Article {} - {} € : \n{}'.format(self.id, self.nom, self.prix, self.description))

    @classmethod
    def createArticle(self):
        nom = input("Quel est le nom de l'article: ")
        description = input("Quel est la description de l'article: ")
        prix = int(input("Quel est le prix: "))
        article = Article(nom, description, prix)
        return article  # retourné pour pouvoir gérer le stock

    def update(self, values):
        self.nom = values['articleName']
        self.description = values['articleDescription']
        self.prix = values['articlePrix']
        db.session.commit()