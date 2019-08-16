from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv
import fuzzy




dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/static/data/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

"""
class Objetivo1 (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Iniciativa_11 = db.Column(db.Integer, nullable=False)
    Iniciativa_12 = db.Column(db.Integer, nullable=False)
"""


@app.route("/")
@app.route("/home")
def index():
    titulo = "Home"
    lista = ["user1", "user2", "user3"]
    return render_template("index.html", titulo=titulo, lista=lista)



@app.route("/obj_form", methods=["GET", "POST"])
@app.route("/obj_form/<string:url_obj>", methods=["GET", "POST"])
def obj_form(url_obj="nav-obj1"):
    if url_obj == "nav-obj1" and request.method == "POST":
        
        #save values iniciativa 1 iniciativa 2        
        inic1 = request.form["iniciativa_1_1"]
        inic2 = request.form["iniciativa_1_2"]
        inic1 = int(inic1)
        inic2 = int(inic2)
        #calculate fuzzy objetivo 1
        fuzzy.calculate_obj1(inic1, inic2)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj2" and request.method == "POST":
        
        #save values iniciativa 1 iniciativa 2 iniciativa 3       
        inic1 = request.form["iniciativa_2_1"]
        inic2 = request.form["iniciativa_2_2"]
        inic3 = request.form["iniciativa_2_3"]
        inic1 = int(inic1)
        inic2 = int(inic2)
        inic3 = int(inic3)
        #calculate fuzzy objetivo 2
        fuzzy.calculate_obj2(inic1, inic2, inic3)
        print(inic3)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj3" and request.method == "POST":
        inic1 = request.form["iniciativa_3_1"]
        inic1 = int(inic1)
        #calculate fuzzy objetivo 3
        fuzzy.calculate_obj3(inic1)
        print(inic1)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj4" and request.method == "POST":
        inic1 = request.form["inicitiva_4_1"]

    return render_template("obj_form.html", url_obj=url_obj)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)