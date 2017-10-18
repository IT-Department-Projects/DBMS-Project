from flask import *
from flask_bootstrap import Bootstrap
import sqlite3, hashlib, os

app = Flask(__name__)
Bootstrap(app)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def root():
	return render_template('index.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/electronics/mobile")
def electronicsPage():
	return render_template('electronics_mobile.html')

@app.route("/clothingPage")
def clothingPage():
	return render_template('clothingPage.html')

@app.route("/home_furniturePage")
def home_furniturePage():
	return render_template('home_furniturePage.html')

@app.route("/books_morePage")
def books_morePage():
	return render_template('books_morePage.html')




if __name__ == '__main__':
    app.run(debug=True)
