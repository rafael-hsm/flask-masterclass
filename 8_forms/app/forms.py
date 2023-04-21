from flask_wtf import FlaskForm
from wtforms.fields import EmailField
from wtforms.fields import PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email

class LoginForm(FlaskForm):
    email = EmailField('E-mail' validators=[Email()])
    password = PasswordField('Senha', validators=[
        Length(3, 6, 'O campo deve conter entre 3 a 6 carecteres.')
        ])
    remember = BooleanField('Permanecer Conectado')
    submit = SubmitField('Login')
    