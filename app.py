from flask import Flask
from flask import render_template  # jinja2
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

from classes.article import Article
from classes.stock import stock
from classes.stockEntry import Stock_Entry


# @app.route('/')
# def hello_world():
#    return 'Hello World!'

@app.route('/user/<username>')  ## <str:username> ou <int:agev>
def hello_user(username):
    return 'Hello {}'.format(username)


@app.route('/')
def index():
    return render_template('index.html', liste=stock.entries())


@app.route('/article/delete/<id>')
def delete(id):
    stock.deleteArticleById(id)
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'GET':
        # show create form
        return render_template('form.html')
    else:
        # create article from post body
        nom = request.form['articleName']
        description = request.form['articleDescription']
        prix = request.form['articlePrix']
        qte = request.form['articleQte']
        # Création de l'article
        article = Article(nom=nom, description=description, prix=int(prix))
        # Association article et quantité
        stock.addArticleQte(article, 1)

        return redirect(url_for('index'))

@app.route('/article/edit/<id>', methods=['GET', 'POST'])
def edit_article(id):
    if request.method == 'GET':
        # show create form
        return render_template('form.html')
    else:
        # create article from post body
        nom = request.form['articleName']
        description = request.form['articleDescription']
        prix = request.form['articlePrix']
        qte = request.form['articleQte']
        # Création de l'article
        article = Article(nom=nom, description=description, prix=int(prix))
        # Association article et quantité
        stock.addArticleQte(article, 1)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
