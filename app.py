from flask import Flask
from flask import render_template  # jinja2
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##pour flask-migrate
migrate = Migrate(app,db)

from classes.article import Article
from classes.stock import stock
from classes.order import Order
from classes.order_Entry import Order_Entry

@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('index.html', liste=stock.entries(),orders=orders)


@app.route('/article/delete/<id>')
def delete(id):
    stock.deleteArticleById(id)
    return redirect(url_for('index'))

@app.route('/order/delete/<id>')
def deleteOrder(id):
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'GET':
        # show create form
        return render_template('addForm.html')
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

@app.route('/order/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'GET':
        # show create form
        return render_template('addOrderForm.html')
    else:
        nom = request.form['orderName']
        order=Order(name=nom, status='ongoing')
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/article/edit/<id>', methods=['GET','POST'])
def edit_article(id):
    # Récupération de l'article
    article = Article.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('editForm.html',article=article)
    else:
        # Récupération de l'article
        article.update(request.form)

        return redirect(url_for('index'))

@app.route('/order/edit/<id>', methods=['GET','POST'])
def edit_order(id):
    # Récupération de l'article
    order = Order.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('editOrderForm.html',order=order)
    else:
        # Récupération de l'article
        order.update(request.form)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
