from flask import render_template, url_for, flash, redirect
from pitch import app, db, bcrypt
from pitch.forms import RegistrationForm, LoginForm
from pitch.models import User, Post


posts = [
    {
        'author': 'Ahmed mukhtar',
        'title': 'pitch Post 1',
        'content': 'First post content',
        'date_posted': 'October 10, 2010'
    },
    {
        'author': 'Hajia Enow',
        'title': 'pitch Post 2',
        'content': 'Second post content',
        'date_posted': 'October 10, 2010'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
