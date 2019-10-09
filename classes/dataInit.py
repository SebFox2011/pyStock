from classes.menu import Menu
from classes.article import Article
from classes.stock import Stock
from classes.stockEntry import Stock_Entry


article1 = Article("Apple","Mcboock Pro",3400)
article2 = Article("Windows","XP Pro",34)
article3 = Article("Linux","Ubuntu",65)

stockArticle1 = Stock_Entry(article1,10)
stockArticle2 = Stock_Entry(article2,200)
stockArticle3 = Stock_Entry(article3,65)

stock = Stock()
stock.AjoutStock(stockArticle1)
stock.AjoutStock(stockArticle2)
stock.AjoutStock(stockArticle3)