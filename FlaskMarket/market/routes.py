from market import app, mysql
from flask import render_template, redirect, url_for, request, flash, send_file, send_from_directory
import threading
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from market.forms import RegisterForm, CarForm, ContractForm, PaymentForm, LoginForm
from market.models import Car, Login, Contract, Payment
from flask_login import login_user, logout_user, login_required, current_user, UserMixin, logout_user
from market import login_manager
import MySQLdb

mutex = threading.Lock()

#login user unig login_manager
@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM login WHERE id_login = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        user = Login(user[0], user[1], user[2], user[3])
        return user
    else:
        return None

#logout info
@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page'))

#login info; check if user is admin or not and redirect to the right page 
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        login = Login(1, 'sdf', 'sdf', 'sdf')
        admin = login.is_admin(form.username.data, form.password.data)
        user = login.check_password(form.username.data, form.password.data)
        
        if admin:
            login_user(admin)
            flash(f'Welcome {admin.username}! You are logged in with {admin.mail}', category='success')
            return redirect(url_for('market_page'))
        elif user:
            login_user(user)
            flash(f'Welcome {user.username}! You are logged in with {user.mail}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Username or password are not correct', category='danger')
    return render_template('login.html', form=form)

#register info and check if user is already in database
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        login = Login(1, 'sdf', 'sdf', 'sdf')
        login.add_login_db(form.username.data, form.mail.data, form.password1.data)
        return redirect(url_for('login_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('signUp.html', form=form)
    
#home page 
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#Admin market page, get all cars from database and display them
@app.route('/admin')
def market_page():
    car = Car(1, 'BMW', 2001, 'Diesel', 5, 'Automatique', 1000,  '123456', 'bmw.jpg')
    all_cars = car.get_cars()
    return render_template('market.html', dataItem=all_cars)

#user market page, get all available cars from database and display them
@app.route('/cars')
def cars_page():
    car = Car(1, 'BMW', 2001, 'Diesel', 5, 'Automatique', 1000,  '123456', 'bmw.jpg')
    available_cars = car.get_available_cars()
    return render_template('index.html', dataItem=available_cars)

#check if images are allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}


#Admin, add car to database and upload image to folder
@app.route('/add_car', methods=['POST', 'GET'])
def add_car():
    form = CarForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            car_image = request.files['car_image']
            filename = secure_filename(car_image.filename)
            # car_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            car = Car(1, 'BMW', 2001, 'Diesel', 5, 'Automatique', 1000,  '123456', 'bmw.jpg')
            car.add_car_db(form.marque.data, form.model.data, form.type_carburant.data, form.nombre_place.data, form.transmission.data, form.prix_location.data, form.matricule.data, filename)
            flash('Car has been added successfully', 'success')
            return redirect(url_for('market_page'))
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('addCar.html', form=form)



#Admin edit, delete car from database 
@app.route('/delete_car/<int:item_id>')
def delete_car(item_id):
    car = car = Car(1, 'BMW', 2001, 'Diesel', 5, 'Automatique', 1000,  '123456', 'bmw.jpg')
    deleted  = car.delete_car(item_id)
    if deleted:
        flash('Car has been deleted successfully', 'success')
    else:
        flash('Car has not been deleted', 'danger')
    return redirect(url_for('market_page'))

#Contrat page, check ContractForm and PaymentForm and add contract to database
@app.route('/payment', methods=['GET', 'POST'])
def contract_submit():
    form = ContractForm()
    form2 = PaymentForm()
    item_id = request.args.get('item_id')
    car = Car(1, 'BMW', 2001, 'Diesel', 4, 'Automatique', 1000, '123456', 'bmw.jpg')
    car_data = car.get_car_by_id(item_id)
    car_price = car.get_prix_location(item_id)
    
    if form.validate_on_submit() and form2.validate_on_submit():

        contrat = Contract(1, 'sdf', 'sdf', 1111, 1111, 'sdf@sdf.sdf', 'sdf', 'sdf', 'sdf',122,  1000)
        payment = Payment(1, 'card_name', 3434, 34, 334)
        
        contrat.add_contract_db(form.nom.data, form.prenom.data, form.start_date.data, form.finish_date.data, form.mail.data, form.adresse.data, form.pays.data, form.ville.data, form.zip.data, car_price)
        payment.add_payment_db(form2.nom_carte.data, form2.numero_carte.data, form2.expiration.data, form2.cvv.data)
        car.switch_availability(item_id, 0)
        flash('Contract added successfully', 'success')
        return redirect(url_for('home_page'))
        
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('payment.html', form=form, form2=form2, car_data=car_data)

#Switch 1 to 0 and 0 to 1 for availability of car
@app.route('/switch_availability/<item_id>/<availability>')
def switch_availability(item_id, availability):
    car = Car(id_car=None, marque=None, modele=None, type_carburant=None, nombre_place=None, transmission=None, prix_location=None, matricule=None, car_image=None)
    car.switch_availability(item_id, availability)
    return redirect(url_for('cars_page'))


#upload the image from the folder
@app.route('/image/<filename>')
def image(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory(app.config['UPLOAD_CSS'], path)

@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory(app.config['UPLOAD_JS'], path)
