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
	return render_template('electronics_mobile.html')

@app.route("/electronics/mobile_accessories")
def electronics_mobile_accessories():
	return render_template('electronics_mobile_accessories.html')

@app.route("/electronics/laptops")
def electronics_laptops():
	return render_template('electronics_laptops.html')

@app.route("/electronics/televisions")
def electronics_televisions():
	return render_template('electronics_televisions.html')

@app.route("/clothingPage")
def clothingPage():
	return render_template('clothingPage_men.html')

@app.route("/home_furniturePage")
def home_furniturePage():
	return render_template('home_furniturePage.html')

@app.route("/books_morePage")
def books_morePage():
	return render_template('books_morePage.html')




if __name__ == '__main__':
	app.run(debug=True)
