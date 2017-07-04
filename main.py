from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST','GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    if username < 3 or username >20 or " " in username:
        error = "Please enter a valid username."
        return render_template('signup.html', error1 = error)

    if password < 3 or password>20 or " " in password:
        error = "Please enter a valid username."
        return render_template('signup.html', error2 = error)

    if verify_password != password:
        error = "Password does not match."
        return render_template('signup.html', error3 = error)

    if email < 3 or email>20 or " " in email or "@" not in email or "." not in email:
        error = "Please enter a valid email address."
        return render_template('signup.html', error4 = error)

    else:
        return render_template('welcome.html')

@app.route("/", methods=['post', 'get'])
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html'), encoded_error and cgi.escape(encoded_error, quote=True)

app.run()
