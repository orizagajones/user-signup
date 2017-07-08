from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods= ['post'])
# this tries to validate the info, generating any new 
# error messages in the process.
# if no errors, it renders the welcome template

def signup():
    #error = "This is a test"
    #error1 = 'Please enter a username between 3-20 characters without spaces.'
    #return redirect("/?error=" + error + "&error1=" + error1)


    u_name = request.form['username']
    p_word = request.form['password']
    v_word = request.form['verify_password']
    email = request.form['email']

    error1 = ""
    error2 = ""
    error3 = ""
    error4 = ""
    verified = True

    if len(u_name) < 3 or len(u_name) > 20 or ' ' in u_name or u_name=='':
        error1 = 'Please enter a username between 3-20 characters without spaces.'
        verified = False

    if len(p_word) <3 or len(p_word) > 20 or ' ' in p_word:
        error2 = 'Please enter a password between 3-20 characters without spaces.'
        verified = False

    if v_word != p_word:
        error3 = 'Password does not match.'
        verified = False

    if email != "":
        if ' ' in email or '@' not in email or '.' not in email:
            error4 = 'Please enter a valid email address.'
            verified = False
    
    if not verified:
        return redirect("/?error1=" + error1 + "&error2=" + error2 + "&error3=" + error3 + "&error4=" + error4)

    else: 
        return render_template ('welcome.html', username=u_name)



@app.route("/", methods=['post', 'get'])
#this function gets error messages, username and email info 
# from the form with GET requests, and renders a form displaying 
# errors and populating the username and email forms. 

def index():

    encoded_error1 = request.args.get('error1')
    encoded_error2 = request.args.get('error2')
    encoded_error3 = request.args.get('error3')
    encoded_error4 = request.args.get('error4')
    return render_template('signup.html', error1=encoded_error1 and cgi.escape(encoded_error1, quote=True), error2=encoded_error2 and cgi.escape(encoded_error2, quote=True), error3=encoded_error3 and cgi.escape(encoded_error3, quote=True),error4=encoded_error4 and cgi.escape(encoded_error4, quote=True))
app.run()
