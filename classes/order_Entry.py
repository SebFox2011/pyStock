from classes.article import Article
from app import db


class Order_Entry(db.Model):
    article_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete='CASCADE'), primary_key=True)
    article = db.relationship('Article')

    order_id=db.Column(db.Integer, db.ForeignKey('order.id', ondelete='CASCADE'), primary_key=True)
    order = db.relationship('Order',backref=db.backref('entries'))

    qte = db.Column(db.Integer, default=0)

    def price(self):
        return self.Article.prix * self.qte

    def printInfos(self):
        print('la quantité de l article ' + str(self.article.id) + ' est de ' + str(self.qte))
