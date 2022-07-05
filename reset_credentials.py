from model_object import question_one_model_object, question_two_model_object, login_model_id_object


first_question_list = list(question_one_model_object)
second_question_list = list(question_two_model_object)
login_model_id_list = list(login_model_id_object)

def change_username_confirmation():
    choice = input("reset username? y/n ➤  ")
    if choice.lower() == 'y':
        correct_answers_index = credentials_reset()
        set_new_username(correct_answers_index)
    else:
        exit()

def change_password_confirmation():
    choice = input("invalid password.\nreset? y/n ➤  ")
    if choice.lower() == 'y':
        correct_answers_index = credentials_reset()
        set_new_password(correct_answers_index)
    else:
        exit()
    
def credentials_reset():
    from utils import check_if_correct_answers, security_question_answers
    security_answers = security_question_answers()
    while security_answers[0] == "" or security_answers[1] == "":
        print("❌ please answer the questions")
        security_answers = security_question_answers()
    index_of_correct_answers = check_if_correct_answers(security_answers[0], security_answers[1])
    return index_of_correct_answers
    

def set_new_username(index):
    from model_object import login_model_username_update
    new_username = input("enter new username ➤  ")
    update_status = login_model_username_update(index, new_username)
    if update_status:
        print("✅ username updated")
        exit()
    else:
        print("❌ an unexpected error occured")
        
def set_new_password(index):
    import bcrypt
    from model_object import login_model_password_update
    str_pass = input("enter new password ➤  ")
    enc_pass = str_pass.encode('utf-8')
    new_password = bcrypt.hashpw(enc_pass, bcrypt.gensalt(10))
    update_status = login_model_password_update(index, new_password)
    if update_status:
        print("✅ password updated")
        exit()
    else:
        print("❌ an unexpected error occured")