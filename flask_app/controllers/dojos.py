from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import ninja


@app.route('/dojos')
def get_all():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos=dojos)

@app.route('/dojos/<id>')
def get_ninjas(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_ninjas(data)
    return render_template('ninjas.html', dojo=dojo)

@app.route('/ninjas/new')
def get_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('new.html', all_dojos=dojos)

@app.route('/ninjas/new', methods=["POST"])
def submit():
    data = {
        "dojo_id" : request.form["dojo"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    ninja.save(data)
    return redirect('/dojos/'+ request.form['dojo'])

@app.route('/newdojo', methods=["POST"])
def newDojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.new(data)
    return redirect('/dojos')