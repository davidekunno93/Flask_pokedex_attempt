from flask import Flask
from flask import render_template
from app import app

@app.route('/')
def index():
    fake_logins = [{"username": "rollarskates44", "password": "wheelsRus"}, {"username": "soccermom1982", "password": "goalgoalgoal123"}, {"username": "scienceperson17", "password": "nitric-acid-KNO3"}]
    authors = "Flask"
    return render_template("index.html", logs=fake_logins, author=authors)

@app.route('/fav')
def fav():
    favorites = [{"actor": "Ryan Reynolds", "athlete": "Tom Brady", "artist": "Ariana Grande", "tv_person": "Joey", "movie": "Legally Blonde"}, {"actor": "Jason Bateman", "athlete": "Kevin De Bruyne", "artist": "Drake", "tv_person": "David Mitchell", "movie": "Bourne Ultimatum"}]
    return render_template("fav_5.html", fav=favorites)

# @app.route('/games')
# def games():
#     return 'The Games page'

# if __name__ == '__main__':
#     app.run()