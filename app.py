from flask import Flask
from flask import render_template # jinja2
from classes.dataInit import stock
from flask import request
from flask import redirect,url_for
from classes.article import Article
from classes.stockEntry import Stock_Entry
from classes.stock import Stock

app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route('/user/<username>') ## <str:username> ou <int:agev>
def hello_user(username):
    return 'Hello {}'.format(username)

@app.route('/')
def index():
    return render_template('index.html',liste=stock.Stock_Entry)

@app.route('/add',methods=['GET','POST'])
def add_article():
    if request.method =='GET':
        #show create form
        return render_template('form.html')
    else:
        #create article from post body
        nom=request.form['articleName']
        description=request.form['articleDescription']
        prix=request.form['articlePrix']
        qte=request.form['articleQte']
        # Création de l'article
        article = Article(nom,description,prix)
        # Association article et quantité
        stockE = Stock_Entry(article,qte)
        # Ajout au stock de l'article + la quantité
        stock.AjoutStock(stockE)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
