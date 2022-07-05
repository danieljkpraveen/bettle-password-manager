from model_object import username_model_object, password_model_object, login_model_id_object
import bcrypt


username_list = list(username_model_object)
password_list = list(password_model_object)
login_model_id_list = list(login_model_id_object)
check_status = None

def login_user(username, password):
    from reset_credentials import change_password_confirmation
    for index, uname in enumerate(username_list):
        db_pass = password_list[index].split("'")
        db_pass = db_pass[1].encode('utf-8')
        if uname.casefold() == username.casefold() and bcrypt.checkpw(password, db_pass):
            check_status = True
            return check_status, username
        else:
            continue
    if username not in username_list:
        try:
            uname_index = username_list.index(username)
            psswd_index = password_list.index(password.decode('utf-8'))
            if uname_index == psswd_index:
                handle_invalid_username()
        except:
            handle_invalid_username()
    else:
        pass
        # print("✅ correct username")
    for item in password_list:
        item = item.split("'")
        item = item[1].encode('utf-8')
        if bcrypt.checkpw(password, item):
            # print("✅ correct password")
            pass
        else:
            try:
                uname_index = username_list.index(username)
                psswd_index = password_list.index(password.decode('utf-8'))
                if uname_index == psswd_index:
                    change_password_confirmation()
                else:
                    continue
            except:
                change_password_confirmation()

def handle_invalid_username():
    from reset_credentials import change_username_confirmation
    from utils import username_validation, registration_details
    
    choice = username_validation()
    if choice == 1:
        change_username_confirmation()
    elif choice == 2:
        user_details = registration_details()
        register_status = register_user(user_details[0].lower(), user_details[1], user_details[2], user_details[3])
        if register_status:
            print("✅ registered successfully")
            exit()
    else:
        print("invalid choice")
        exit()         

def register_user(username, password, question_one, question_two):
    from model_object import insert_into_login_model
    for index, uname in enumerate(username_list):
        if uname.casefold() == username and password_list[index] == password:
            print("❌ user already exists")
            exit()
    insert_status = insert_into_login_model(username, password, question_one, question_two)
    return insert_status

