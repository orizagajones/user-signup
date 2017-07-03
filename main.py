from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('welcome.html')


@app.route("/signup")
def signup():
    if (request.form['username']) < 3 and (request.form['username'])>20:
        error1 = "Please enter a valid username."
        return redirect("/?error=" + error1)
    if (request.form['password']) < 3 and (request.form['password'])>20:
        error2 = "Please enter a valid username."
        return redirect("/?error=" + error2)
    if (request.form['verify_password']) != (request.form['password']):
        error3 = "Password does not match."
        return redirect("/?error=" + error3)
    if (request.form['email']) < 3 and (request.form['email'])>20:
        error4 = "Please enter a valid email address."
        return redirect("/?error=" + error4)
    if "@" not in (request.form['email']) or if "." not in (request.form['email']):
        error4 = "Please enter a valid email address."
        return redirect("/?error=" + error4)
    return render_template('signup.html')

app.run()
