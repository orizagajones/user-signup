from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST','GET'])
def signup():
    if check_username == False:
        error_message = "Please enter a valid username."
        return (render_template('signup.html'), error_message)
    elif check_password == False:
        error_message = "Please enter a valid password."
        return (render_template('signup.html'), error_message)
    elif dblcheck_password == False:
        error_message = "Password does not match."
        return (render_template('signup.html'), error_message)
    elif check_email == False:
        error_message = "Please enter a valid email address."
        return (render_template('signup.html'), error_message)
    else: 
        return (render_template('welcome.html'))


def check_username():
    username = request.form['username']
    if len(username) < 3 or len(username) >20 or ' ' in username:
        return False
    else: 
        return True

def check_password():
    password = request.form['password']
    if len(password) < 3 or len(password) > 20 or " " in password:
        return False
    else:
        return True

def dblcheck_password():
    verify_password = request.form['verify_password']
    if verify_password != password:
        return False
    else:
        return True

def check_email():
    email = request.form['email']
    if email != "" and len(email) < 3 or len(email) > 20 or " " in email or "@" not in email or "." not in email:
        return False
    else:
        return True


@app.route("/", methods=['post', 'get'])
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html'), encoded_error and cgi.escape(encoded_error, quote=True)

app.run()
