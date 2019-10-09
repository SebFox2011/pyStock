from classes.article import Article
from classes.stockEntry import Stock_Entry
from classes.article import *
from classes.stockEntry import Stock_Entry
from app import db

class Stock:
    def entries(self):
        return Stock_Entry.query.all()

    def addArticleQte (self,article,qte):
        entry = Stock_Entry(article=article,qte=qte)
        db.session.add(entry)
        db.session.commit()

    def AjoutStock(self, Stock):
        db.session.add(Stock)
        db.session.commit()

    def deleteArticleById(self,id):
        entry = Stock_Entry.query.filter_by(article_id=id).first()
        article = Article.query.filter_by(id=id).first()
        db.session.delete(entry)
        db.session.delete(article)
        db.session.commit()

stock = Stock()