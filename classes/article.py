class Article:
    currentId=0
    def __init__(self,nom,description,prix):
        Article.currentId += 1
        self.id = Article.currentId
        self.nom = nom
        self.description=description
        self.prix = prix
    
    def printInfos(self):    
        '''print('identifiant : '+ str(self.id) + '\n')
        print('nom : '+ self.nom + '\n')
        print('description : ' + self.description + '\n')
        print('prix : '+ str(self.prix) + '\n') '''  
        print ('[{}] Article {} - {} € : \n{}'.format(self.id,self.nom,self.prix,self.description))

    @classmethod
    def createArticle(self):
        nom = input("Quel est le nom de l'article: ")
        description = input("Quel est la description de l'article: ")
        prix = int(input("Quel est le prix: "))
        article = Article(nom,description,prix)
        return article # retourné pour pouvoir gérer le stock