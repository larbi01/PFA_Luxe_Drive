from flask import current_app
from market import app, mysql
from datetime import datetime
from flask_login import UserMixin


class Login(UserMixin):
    def __init__(self, id_login, username, mail, password):
        self.id_login = id_login
        self.username = username
        self.mail = mail
        self.password = password
        self.mysql = mysql
    
    def is_active(self):
        return True
    
    #add user to database
    def add_login_db(self, username, mail, password):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("INSERT INTO login (username, mail, password) VALUES (%s, %s, %s)", (username, mail, password))
        conn.commit()
        cur.close()
        return True
    #get id
    def get_id(self):
        return str(self.id_login)
    
    #get user by username
    def get_username(self, username):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        return user

    #get user by id
    def get_user_by_id(self, id_login):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM login WHERE id_login = %s", (id_login,))
        user = cur.fetchone()
        cur.close()
        return user

    #get user by mail
    def get_mail(self, mail):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM login WHERE mail = %s", (mail,))
        user = cur.fetchone()
        cur.close()
        return user
    #check if username is the admin
    def is_admin(self, username, password):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        if user and user[3] == password and user[1] == 'admin':
            user = Login(user[0], user[1], user[2], user[3])
            return user
        else:
            return None

    #check if password of the user is correct from a user given
    def check_password(self, username, password):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        
        if user and user[3] == password and user[1] != 'admin':
            user = Login(user[0], user[1], user[2], user[3]) #create a user instance
            return user
        else:
            return None

class Car:
    def __init__(self, id_car, marque, modele, type_carburant, nombre_place, transmission, prix_location, matricule, car_image):
        self.id_car = id_car
        self.marque = marque
        self.modele = modele
        self.type_carburant = type_carburant
        self.nombre_place = nombre_place
        self.transmission = transmission
        self.prix_location = prix_location
        self.matricule = matricule
        self.car_image = car_image
        self.mysql = mysql

    #add car to database
    def add_car_db(self, marque, modele, type_carburant, nombre_place, transmission, prix_location, matricule, car_image):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("INSERT INTO car (marque, model, type_carburant, nombre_place, transmission, prix_location, disponibilite, matricule, car_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (marque, modele, type_carburant, nombre_place, transmission, prix_location, 1, matricule, car_image))
        conn.commit()
        cur.close()
        return True

    #get all cars
    def get_cars(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM car")
        all_cars = cur.fetchall()
        cur.close()
        return all_cars
    
    #get car by id
    def get_car_by_id(self, item_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM car WHERE id_car = %s", (item_id,))
        car = cur.fetchone()
        cur.close()
        if car is not None:
            car = Car(car[0], car[1], car[2], car[3], car[4], car[5], car[6], car[7], car[8])
        return car

    #get prix_location from a id_car
    def get_prix_location(self, item_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT prix_location FROM car WHERE id_car = %s", (item_id,))
        prix_location = cur.fetchone()
        cur.close()
        return prix_location
    
    #get disponibilite from a id_car
    def switch_availability(self, item_id, availability):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE car SET disponibilite = %s WHERE id_car = %s", (availability, item_id))
        self.mysql.connection.commit()
        cur.close()
        return True

    #get all available cars
    def get_available_cars(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM car WHERE disponibilite = 1")
        all_cars = cur.fetchall()
        cur.close()
        return all_cars

    #delete car from database
    def delete_car(self, item_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM car WHERE id_car = %s", (item_id,))
        self.mysql.connection.commit()
        cur.close()
        return True


class Contract:
    def __init__(self, id_paiment, nom, prenom, start_date, finish_date, mail, adresse, pays, ville, zip, rental_charge):
        self.id_paiment = id_paiment
        self.nom = nom
        self.prenom = prenom
        self.start_date = start_date
        self.finish_date = finish_date
        self.mail = mail
        self.adresse = adresse
        self.pays = pays
        self.ville = ville
        self.zip = zip
        self.rental_charge = rental_charge
        self.mysql = mysql

    #add contract to database
    def add_contract_db(self, nom, prenom, start_date, finish_date, mail, adresse, pays, ville, zip, rental_charge):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("INSERT INTO contrat (nom, prenom, start_date, finish_date, mail, adresse, pays, ville, zip, rental_charge) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (nom, prenom, start_date, finish_date, mail, adresse, pays, ville, zip, rental_charge))
        conn.commit()
        cur.close()
        return True
    # Calculate rental charge, price from car model * days
    def days_rented(self, item_id):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("SELECT start_date, finish_date FROM contrat WHERE id_paiment = %s", (item_id,))
        dates = cur.fetchone()
        cur.close()
        start_date = dates[0]
        finish_date = dates[1]
        delta = finish_date - start_date
        return delta

    # calculate the rental charge
    def calculate_rental_charge(self, prix_location):
        return self.days_rented() * prix_location

class Payment:
    def __init__(self, id, nom_carte, numero_carte, expiration, cvv):
        self.id = id
        self.nom_carte = nom_carte
        self.numero_carte = numero_carte
        self.expiration = expiration
        self.cvv = cvv
        self.mysql = mysql

    #add payment to database
    def add_payment_db(self, nom_carte, numero_carte, expiration, cvv):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("INSERT INTO payment (nom_carte, numero_carte, expiration, cvv) VALUES (%s, %s, %s, %s)",
                    (nom_carte, numero_carte, expiration, cvv))
        conn.commit()
        cur.close()
        return True
