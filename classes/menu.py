class Menu:
    def displayMenu(self):
        print("***********************")
        print("** Gestion du Stock  **")
        print("***********************")
        print("1. Afficher l'état du stock")
        print("2. Ajouter un nouvel article")
        print("3. Modifier la quantité d'un article")
        print("4. Supprimer un article")
        print("5. Quitter")
        print("***********************")
        print("\n\n")

    def readUserNumber(self):
        intNumber = -1
        actionMin = 1
        actionMax = 5
    
        while intNumber < actionMin or intNumber > actionMax:
            userInput = input('Que souhaitez-vous faire ?')
            try:
                intNumber = int(userInput)
                if intNumber < actionMin or intNumber > actionMax:
                    print("Cette action n'est pas disponible")
            except:
                print('Ce n\'est pas un nombre')
        return intNumber