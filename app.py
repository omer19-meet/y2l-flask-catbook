from flask import Flask, render_template, request, url_for, redirect
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def get_cat_route(id):
    cat_1 = get_cat_by_id(id)
    return render_template('cat.html', cat= cat_1)

@app.route('/vote/<int:id>')
def vote_for_cat(id):
	count_votes(id=id)
	return redirect(url_for("get_cat_route", id=id))

    # Get cat with id from database
    # return render_template('cat.html', cat_1 )

@app.route('/create', methods=['GET', 'POST'])
def create_new_cat():
	if request.method == 'GET':
		return render_template('create_cat.html')
	else: 
		name = request.form['name']
		votes=0
		create_cat(name=name)
		print("new cat added")
		return render_template('respond.html')


if __name__ == '__main__':
   app.run(debug = True)