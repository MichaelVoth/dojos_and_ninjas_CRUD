from flask import render_template, redirect, request    #Imports flask functionalilty
from flask_app import app   #Imports flask app
from flask_app.models.ninja import Ninja #imports Ninja class
from flask_app.models.dojo import Dojo #imports Dojo class

@app.route("/create_ninja", methods = ['POST'])
def create_ninja():             #Creates ninja from form data
    Ninja.ninja_create(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'dojos/{dojo_id}')

@app.route('/delete/ninja/<int:id>')
def delete_ninja(id):           #Deletes ninja at id
    ninja = Ninja.ninja_select_one({"id": id})
    dojo_id = ninja.dojo_id
    Ninja.ninja_delete(id)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/edit/<int:id>')
def edit_ninja(id):             #redirects to form with individual info displayed
    data = {'id':id}
    ninja = Ninja.ninja_select_one(data)
    dojos = Dojo.dojo_select_all()
    return render_template('edit.html',dojos = dojos, ninja = ninja)

@app.route('/update', methods=['POST'])
def update_ninja():             #Updates ninja info in DB
    Ninja.ninja_update(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")