
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from wtforms.fields import DecimalField, IntegerField
from market.models import Login
from flask_wtf.file import FileField, FileAllowed
import datetime
import re
from datetime import datetime


class ContractForm(FlaskForm):
    #check if start date is today or after
    def validate_start_date(self, start_date_to_check):
        start_date = datetime.strptime(start_date_to_check.data, '%Y-%m-%d')
        if start_date < datetime.today():
            raise ValidationError('The start date should be today or after.')
    #check if finish date is after start date
    def validate_finish_date(self, finish_date_to_check):
        finish_date = datetime.strptime(finish_date_to_check.data, '%Y-%m-%d')
        start_date = datetime.strptime(self.start_date.data, '%Y-%m-%d')
        if finish_date < start_date:
            raise ValidationError('The finish date should be after the start date.')


    nom = StringField(label='Nom', validators=[DataRequired()])
    prenom = StringField(label='Prenom', validators=[DataRequired()])
    start_date = StringField(label='Date de debut', validators=[DataRequired()])
    finish_date = StringField(label='Date de fin', validators=[DataRequired()])
    mail = StringField(label='Email', validators=[Email(), DataRequired()])
    adresse = StringField(label='Adresse', validators=[DataRequired()])
    pays = StringField(label='Pays', validators=[DataRequired()])
    ville = StringField(label='Ville', validators=[DataRequired()])
    zip = IntegerField(label='Zip', validators=[ DataRequired()])
    

class PaymentForm(FlaskForm):

    nom_carte = StringField(label='Nom sur la carte')
    numero_carte = IntegerField(label='Numero de la carte')
    expiration = StringField(label='Expiration (MM/YY)')
    cvv = IntegerField(label='CVV')
    submit = SubmitField(label='Payer')
class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
    submit = SubmitField(label='Sign in')
class RegisterForm(FlaskForm):

    #check if username is already taken
    def validate_username(self, username_to_check):
        login = Login(1,'username', 'mail', 'password')
        user = login.get_username(username_to_check.data)
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    #check if mail is already taken
    def validate_mail(self, mail_to_check):
        login = Login(1,'username', 'mail', 'password')
        user = login.get_mail(mail_to_check.data)
        if user:
            raise ValidationError('Email already exists! Please try a different email.')

    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    mail = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
class CarForm(FlaskForm):
    #check if prix location > 100
    def validate_prix_location(self, prix_location_to_check):
        if prix_location_to_check.data < 100:
            raise ValidationError('The price should be strictly superior to 100')
    #check if nombre place > 0
    def validate_nombre_place(self, nombre_place_to_check):
        if nombre_place_to_check.data < 0:
            raise ValidationError('The number of seats should be strictly positive')
    #check if nombre porte > 0
    def validate_nombre_porte(self, nombre_porte_to_check):
        if nombre_porte_to_check.data < 0:
            raise ValidationError('The number of doors should be strictly positive')
    #check if matricule is in a format like 11111 A 11
    def validate_matricule(self, matricule_to_check):
        if not re.match(r'^[0-9]{5} [A-Z]{1} [0-9]{2}$', matricule_to_check.data):
            raise ValidationError('The registration number should be in the format 11111 A 11')
    #check if image was uploaded
    def validate_car_image(self, car_image_to_check):
        if not car_image_to_check.data:
            raise ValidationError('You should upload an image')

    car_image = FileField(label='Image', validators=[FileAllowed(['jpg', 'png'])])
    marque = StringField(label='Marque', validators=[DataRequired()])
    model = StringField(label='Model', validators=[DataRequired()])
    type_carburant = StringField(label='Type de carburant', validators=[DataRequired()])
    nombre_place = IntegerField(label='Nombre de place', validators=[DataRequired()])
    transmission = StringField(label='Transmission', validators=[DataRequired()])
    prix_location = DecimalField(label='Prix de location', validators=[DataRequired()])
    disponibilite = StringField(label='Disponibilite', validators=[DataRequired()])
    matricule = StringField(label='Matricule', validators=[DataRequired()])
    submit = SubmitField(label='Ajouter')
