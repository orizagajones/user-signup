from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods= ['post', 'get'])
# this tries to validate the info, generating any new error messages in teh process.
# if no errors, it renders the welcome template
def signup():
    error1 = 'Please enter a username between 3-20 characters without spaces.'
    error2 = 'Please enter a password between 3-2- characters without spaces.'
    error3 = 'Please reenter your password.'
    error4 = 'Please enter a valid email address.'

    u_name = request.form('username')
    p_word = request.form('password')
    v_word = request.form('verify_password')
    email = request.form('email') 

    if len(u_name) < 3 or len(u_name) > 20 or ' ' in u_name:
        return redirect("/?error=" + error1)
    if len(p_word) <3 or len(p_word) > 20 or ' ' in p_word:
        return redirect("/?error=" + error2)
    if v_word != p_word:
        return redirect("/?error=" + error3)
    if ' ' in email or '@' not in email or '.' not in email:
        return redirect("/?error=") + error4)
    else: 
        return render_template ('welcome.html')


@app.route("/", methods=['post', 'get'])
#this function gets error messages, username and email info from the form with GET requests, and renders a form displaying errors and populating the username and email forms. 
def index():
    return render_template('signup.html')

app.run()
