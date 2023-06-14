from flask import Blueprint, render_template, request, redirect, url_for
from .forms import RegisterForm, PokeForm
from ..models import User
from .pokemon import Pokemon

auth = Blueprint('auth', __name__, template_folder="auth_templates")

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    #request.method shows if the request made was GET or POST (or other?)
    print(request.method, "<-- this is the req method")
    if request.method == 'POST':
        if form.validate():
            print("validated")
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))

    return render_template("register.html", form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@auth.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    form = PokeForm()
    if request.method == "POST":
        if form.validate():
            pokemon_name = form.pokemon.data
            pokemon = Pokemon(pokemon_name)
            global poke_dict
            poke_dict = pokemon.pokedex()
            return redirect(url_for('auth.pokefacts'))

    return render_template("pokemon.html", form=form)

@auth.route('/pokefacts', methods=["GET", "POST"])
def pokefacts():
    return render_template("pokefacts.html", pokemon=poke_dict)