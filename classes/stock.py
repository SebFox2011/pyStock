from classes.article import Article
from classes.stockEntry import Stock_Entry

class Stock:
    def __init__(self):
        self.Stock_Entry=[]
    
    def AjoutStock(self,Stock):
        self.Stock_Entry.append(Stock)

    def printInfos(self):
        totalPrice =0  
        print ('le stock est : ')   
        for item in self.Stock_Entry:
            item.printInfos()
            totalPrice += item.price()
        print ('Le prix total du panier est ' + str(totalPrice) + ' €' + '\n')
    
    def addArticle(self):
        article = Article.createArticle()
        quantity = int(input("Quantité de l'article: "))
        entry = Stock_Entry(article,quantity)
        self.AjoutStock(entry)