from flask import Flask, request, redirect, render_template
from validation import main_validation, password_validation, required_field, email_validation
import re



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    username = ''
    email = ''
    password = ''
    verify_password = ''
    username_error = ''
    password_error = ''
    email_error = ''
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']
        username_error = required_field(username)
        password_error = password_validation(password, verify_password)
        email_error = email_validation(email)

        if username_error == '' and password_error == '' and email_error == '':
            return redirect('/confirmation?username={0}'.format(username))

    return render_template('form.html', username= username, email = email, password = password, verify_password = verify_password, username_error = username_error, password_error = password_error, email_error = email_error)

@app.route('/confirmation')
def confirmation():
    username = request.args.get('username')
    return render_template('confirmation.html', username=username)

app.run()
