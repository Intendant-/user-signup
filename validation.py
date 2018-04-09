import re


## check if length is less than 3 or greater than 20 with no spaces
def main_validation(text):

    if len(text) < 3 or len(text) > 20:
        return "Must be between 3 and 20 characters"; 
    elif re.search('\s', text):
        return "Connot contain spaces";
    else:
        return '';

## check if passwords match
def password_validation(text, verify):
    if text != verify:
        return "Passwords do not match";
    else:
        return required_field(text)

## check if empty
def required_field(text):
    if text == '':
        return "Required field"
    else:
        return main_validation(text)

## check if email contains @ and .
def email_validation(text):
    if text == '':
        return '';
    elif not re.search('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)' , text):
        return "Please use a valid email address";
    else:
        return main_validation(text);