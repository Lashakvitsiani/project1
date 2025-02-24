from flask import render_template, redirect
from flask_login import login_user, logout_user, current_user, login_required
from forms import RegisterForm, LoginForm
from models import Product, User
from ext import app, db


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/registered_users.html")
def users():
    registered_users = User.query.all()
    return render_template("users.html", registered_users=registered_users)


@app.route('/register.html', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")

    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html', form=form)


@app.route("/login.html", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)


@app.route('/store.html')
@login_required
def store():
    products = Product.query.all()
    return render_template('store.html', products=products)


@app.route('/Album-AM.html')
@login_required
def album():
    return render_template('Album-AM.html')


@app.route('/News.html')
@login_required

def news():
    return render_template('News.html')


@app.route('/player.html')
@login_required

def player():
    return render_template('player.html')
