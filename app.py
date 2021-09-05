from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
earnings = 2000


@app.route("/base")
def base():
    return render_template('base.html', earnings=earnings)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/fp")
def fp():
    return render_template('forgot-password.html')


@app.route("/blank")
def blank():
    return render_template('blank.html')


@app.route("/404")
def hoh():
    return render_template('404.html')


@app.route("/tables")
def tables():
    return render_template('tables.html')


@app.route("/charts")
def charts():
    return render_template('charts.html')


@app.route("/buttons")
def buttons():
    return render_template('buttons.html')


@app.route("/cards")
def cards():
    return render_template('cards.html')


if __name__ == '__main__':
    app.run(debug=True)
