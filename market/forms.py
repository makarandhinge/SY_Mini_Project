from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,ValidationError,TextAreaField
from wtforms.validators import Length,EqualTo,Email,DataRequired
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        
           user=User.query.filter_by(username=username_to_check.data).first()
           if user:
               raise ValidationError("username already Exits! please try a different username")

    def validate_PRN(self,PRN_to_check):

           PRN=User.query.filter_by(PRN=PRN_to_check.data).first()
           if PRN:
               raise ValidationError("PRN is alredy registered!! ")
    
    
    username=StringField(label='User Name',validators=[Length(min=2, max=20),DataRequired()])
    PRN=StringField(label="PRN",validators=[Length(min=10,max=10),DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit= SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class billForm(FlaskForm):
     name=StringField(label='name:')

    