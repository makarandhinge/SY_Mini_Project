from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages,request
from market.models import Item, User,Bill
from market.forms import RegisterForm, LoginForm , billForm
from market import db
from flask_login import login_user, logout_user, login_required,current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/menu', methods=['GET', 'POST'])
@login_required
def Menu_page():
    items = Item.query.all()
    return render_template('Menu.html', items=items) 


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              PRN=form.PRN.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f'Account Created Successfully! You are logged in as: {user_to_create.username}', category='success')

        return redirect(url_for('Menu_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html',form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_passward=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('Menu_page'))
        else:
            flash('Username and password are not match! Please try again',
                  category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged Out", category='info')
    return redirect(url_for('home_page'))


@app.route('/bill', methods=['POST','GET'])
def bill_page():
    
      if request.method=='POST':
         Quantity=request.form['Qunatity']
         Price=request.form['price']
         Name=request.form['name']
         Bill_update = Bill(quantity=Quantity,price=Price,name=Name)

         try:
             db.session.add(Bill_update)
             db.session.commit()
             return redirect('/bill')
         except:
             return 'there was an issue please try again!'
      else:
          order=Bill.query.order_by(Bill.name).all()
          return render_template('Menu.html',order=order)


      

          


        