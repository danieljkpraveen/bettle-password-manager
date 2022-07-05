from user_verfication import login_user, register_user
from utils import get_login_credentials, registration_details


def login_args():
    user_credentials = get_login_credentials()
    while user_credentials[0] == "" or user_credentials[1] == "":
        print("❌ Do not leave fields empty")
        user_credentials = get_login_credentials()
    login_status = login_user(user_credentials[0], user_credentials[1])
    return login_status

def register_args():
    user_details = registration_details()
    register_status = register_user(user_details[0].lower(), user_details[1], user_details[2], user_details[3])
    return register_status

