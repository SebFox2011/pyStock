from classes.article import Article
from app import db


class Stock_Entry(db.Model):
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True, nullable=False)
    article = db.relationship('Article')

    qte = db.Column(db.Integer, default=0)

    def price(self):
        return self.Article.prix * self.qte

    def printInfos(self):
        print('la quantité de l article ' + str(self.article.id) + ' est de ' + str(self.qte))
