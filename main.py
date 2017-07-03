from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

username = request.form['username']
password = request.form['password']
verify_password = request.form['verify_password']
email = request.form['email']


@app.route("/")
def index():
    return render_template('welcome.html')


@app.route("/signup", methods=['POST'])
def signup():
    if username < 3 or username >20:
        error1 = "Please enter a valid username."
        return render_template('signup.html'), error1

    if password < 3 or password>20:
        error2 = "Please enter a valid username."
        return render_template('signup.html'), error2

    if verify_password != password:
        error3 = "Password does not match."
        return render_template('signup.html'), error3

    if email < 3 or email>20:
        error4 = "Please enter a valid email address."
        return render_template('signup.html'), error4

    if "@" not in email or if "." not in email:
        error4 = "Please enter a valid email address."
        return render_template('signup.html'), error4


app.run()
