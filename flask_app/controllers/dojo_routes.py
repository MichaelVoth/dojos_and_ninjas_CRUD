from flask import render_template, redirect, request    #Imports flask functionalilty
from flask_app import app   #Imports flask app
from flask_app.models.dojo import Dojo #imports Dojo class


@app.route('/')             #quick redirect
def dojo_redirect():
    return redirect('/dojos')

@app.route('/dojos')
def show_all_dojos():       #slects all dojos
    all_dojos = Dojo.dojo_select_all()
    return render_template('dojos.html', dojos=all_dojos)

@app.route('/dojos/<int:id>')
def show_dojo(id):          #shows dojo with ninjas in that dojo
    dojo = Dojo.dojo_and_ninja_select({'id': id})
    return render_template('show_dojo.html', dojo=dojo)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():          #creates a dojo
    Dojo.dojo_create(request.form)
    return redirect('/dojos')

@app.route('/delete/<int:id>')
def delete_dojo(id):        #deletes a dojo
    Dojo.dojo_delete(id)
    return redirect('/dojos')

@app.route('/ninjas')
def ninja_redirect():       #redirect to add ninja
    dojos = Dojo.dojo_select_all()
    return render_template("ninjas.html", dojos=dojos)

