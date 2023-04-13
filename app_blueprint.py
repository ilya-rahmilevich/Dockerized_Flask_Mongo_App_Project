from flask import Blueprint, jsonify, render_template, request
from Movie_db import Movie_db

app_blueprint = Blueprint('app_blueprint',__name__)

@app_blueprint.route('/')
def index():
    try:
        similar = Movie_db.search_movie(query=request.args.get('query'))
        dictionary = { "poster_path" : stu.poster_path for stu in similar }
        if Movie_db.search_value(dictionary):
            Movie_db.insert_data(dictionary)
            temp = dictionary
        else:
            temp = dictionary

        return render_template("index.html",image="https://image.tmdb.org/t/p/original/" + str(temp["poster_path"]))
    except:
        return render_template("index.html")

@app_blueprint.route('/remove')
def remove():
    try:
        similar = request.args.get('query')
        Movie_db.remove_data(similar)

        return render_template("index.html")
    except:
        return render_template("index.html")

@app_blueprint.route('/update')
def update_data():
        try:
            similar = request.args.get('query')
            value = request.args.get('value')
            Movie_db.update_data(similar,value)
            
            return render_template("index.html")
        except:
            return render_template("index.html") 

    
    


