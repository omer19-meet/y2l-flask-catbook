from flask import Flask
from flask import render_template
from database import get_all_cats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def get_cat_route(id):
    catsp = get_all_cats()
    for cat in catsp :
        if cat.id == id :
            obj = cat
            # return render_template('cat.html', obj= cat)

    # Get cat with id from database
    return render_template('cat.html', cat=obj )

if __name__ == '__main__':
   app.run(debug = True)
