from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('welcome.html')


@app.route("/signup", methods=['POST'])
def signup():
    if {{'username'}} < 3 or {{'username'}} >20:
        error1 = "Please enter a valid username."
        return redirect("/?error=" + error1)

    if {{'password'}} < 3 or {{'password'}}>20:
        error2 = "Please enter a valid username."
        return redirect("/?error=" + error2)

    if {{'verify_password'}} != {{'password'}}:
        error3 = "Password does not match."
        return redirect("/?error=" + error3)

    if (request.form['email']) < 3 or (request.form['email'])>20:
        error4 = "Please enter a valid email address."
        return redirect("/?error=" + error4)

    if "@" not in {{'email'}} or if "." not in {{'email'}}:
        error4 = "Please enter a valid email address."
        return redirect("/?error=" + error4)
    return render_template('signup.html')

app.run()
