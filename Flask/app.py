from flask import Flask,render_template
from config import Config
from apps.forms import LoginForm

app= Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    user={"name":"Ritu"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",user=user,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__=="__main__":
    app.run(debug=True)