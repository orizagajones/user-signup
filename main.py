from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif:
                    border-radius: 15px;
                }}
            </style>
        </head>
    <body>
        <form action="/" method = 'POST'>
            <label>Username:
                <input type="text" name="username">
            </label>
            <label>
                <input type="password" name="password">
            </label>
            <label>
                <input type="password" name="pswd_verify">
            </label>
            <label>
                <input type="text" name="email">
            </label>
            <label>
                <input type="submit">
            </label>
        </form>        
    </body>
</html>
"""

@app.route("/")
def main():
    return signup_form 

app.run()
