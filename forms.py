from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired,FileAllowed
from werkzeug.utils import secure_filename

class LoginForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired()])
	submit=SubmitField('Sign In')
	abc = StringField('abc', render_kw={"placeholder": "test"})

class SignupForm(FlaskForm):
	username=StringField('username',validators=[DataRequired()])
	password=StringField('password',validators=[DataRequired()])
	submit=SubmitField('Sign Up')
	abc = StringField('abc', render_kw={"placeholder": "test"})
