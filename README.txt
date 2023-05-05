Car Rental Website : Luxe Drive

This web application is built using Flask and Python, with MySQL as the database management system. It is a PFA project for 3IIR class, assigned by Mr. AMEKSA, which aims to teach us how to manipulate databases using Python.

Features

There are two types of users: simple users and admins.
Admins can sign in using the following credentials: 

- username: admin
- password: admin

Simple users can access the home page, cars page, and checkout form.
Admins can add, delete, or modify cars in the database.

Please import the database location_voiture, lunch XAMPP or WAMPServer to launch your localhost.

__init__.py sets up various configurations for the application. It sets up the path for storing images, connects to a MySQL database, sets up SQLAlchemy for database management. It also sets up a Login Manager for user authentication.

There are four classes defined in models.py: Login, Car, Contract, and Payment, each with its own methods for connecting to the location_voiture database.
Form input validation is handled in forms.py. There are five form classes defined: LoginForm, RegisterForm, ContractForm, PaymentForm, and CarForm.
The function Validate_On_Submit() checks if all inputs are in a Correct form. Then the data is added to the database.
The app uses Jinja syntax to render nine HTML templates: base.html, index.html, cars.html, checkout.html, login.html, register.html, admin.html, add_car.html, and edit_car.html. 
The routes.py page is responsable for rederecting users to pages using functions from models.py and forms.py.



Installation

To run this app, you will need to install the following Python packages:

Flask
Flask-MySQLdb
Flask-WTF
Flask-login
flask-werkzug


You can install them using pip:

pip install Flask Flask-MySQLdb Flask-WTF

After installing the dependencies, you can run the app using the following command:

python run.py

Credits

This project was developed by :

- Larbi OUADEIH
- Zakaria MESSOUS
- Chaimae OUKHOUY

License
This project is licensed under the EMSI License.
