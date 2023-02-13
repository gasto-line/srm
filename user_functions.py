# The simplest function to get the user email (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Write down your email: ")

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    return input("Create your user name: ")

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")