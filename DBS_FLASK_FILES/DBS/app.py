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



@app.route("/login",methods=['GET','POST'])
def login():
	return render_template('login.html')
	


@app.route("/loginForm")
def loginForm():
	return render_template('login.html')


@app.route("/register",methods=['GET','POST'])
def register():
	if request.method == 'POST':
		#Parse form data    
		password = request.form['password']
		email = request.form['email']
		firstName = request.form['firstName']
		lastName = request.form['lastName']
		address1 = request.form['address1']
		zipcode = request.form['zipcode']
		city = request.form['city']
		state = request.form['state']
		country = request.form['country']
		phone = request.form['phone']

		with sqlite3.connect('database.db') as con:
			try:
				cur = con.cursor()
				cur.execute('INSERT INTO users (password, email, firstName, lastName, address1, zipcode, city, state, country, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, address1, zipcode, city, state, country, phone))

				con.commit()

				msg = "Registered Successfully"
			except:
				con.rollback()
				msg = "Error occured"
		con.close()
		return render_template("login.html", error=msg)

@app.route("/registerForm")
def registrationForm():
	return render_template("register.html")


	
	

@app.route("/electronics/mobile")
def electronics_mobile():
	return render_template('mobile.html')

@app.route("/electronics/mobile_accessories")
def electronics_mobile_accessories():
	return render_template('mobile_accessories.html')

@app.route("/electronics/laptops")
def electronics_laptops():
	return render_template('laptops.html')

@app.route("/electronics/televisions")
def electronics_televisions():
	return render_template('televisions.html')

@app.route("/clothingPage/men")
def men():
	return render_template('men.html')

@app.route("/clothingPage/women")
def women():
	return render_template('women.html')

@app.route("/clothingPage/baby&kids")
def baby_kids():
	return render_template('baby_kids.html')

@app.route("/home_furniture/kitchen&dining")
def kitchen_dining():
	return render_template('kitchen_dining.html')

@app.route("/home_furniture/furniture")
def furniture():
	return render_template('furniture.html')

@app.route("/home_furniture/home_decor")
def home_decor():
	return render_template('home_decor.html')

@app.route("/books_morePage/books")
def books():
	return render_template('books.html')

@app.route("/books_morePage/stationary")
def stationary():
	return render_template('stationary.html')

@app.route("/books_morePage/gaming&accessories")

def gaming_accessories():
	return render_template('gaming_accessories.html')



if __name__ == '__main__':
	app.run(debug=True)
