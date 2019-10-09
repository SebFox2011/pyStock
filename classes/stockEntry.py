class Stock_Entry:
    def __init__(self,Article,qte):
        self.Article = Article
        self.qte = qte

    def price(self):
        return self.Article.prix*self.qte

    def printInfos(self):    
        print ('la quantité de l article ' + str(self.Article.id) + ' est de '+ str(self.qte) )