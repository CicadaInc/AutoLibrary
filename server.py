from flask import Flask, render_template, url_for, session, redirect
from Forms import SingInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Супер секретный мод на майнкрафт'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tetropentada.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
@app.route("/index")
def index():
    pass


@app.route("/login")
def login():
    form = SingInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).filter_by(password=password).first()
        if user:
            session['username'] = username
            session['user_id'] = user.id
            return redirect("/main")
        return render_template("wrong_sign_in.html", title='Tetropentada', form=form,
                               style=url_for('static', filename='cover.css'),
                               bootstrap=url_for('static', filename='bootstrap.min.css'),
                               icon=url_for('static', filename='images/icon.png'), User=User)
    return render_template("sign_in.html", title='Tetropentada', form=form,
                           style=url_for('static', filename='cover.css'),
                           bootstrap=url_for('static', filename='bootstrap.min.css'),
                           icon=url_for('static', filename='images/icon.png'), User=User)


app.run(port=8081, host='127.0.0.1')
