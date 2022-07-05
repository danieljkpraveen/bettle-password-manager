import bcrypt


def get_login_credentials():
    username = input("enter username ➤  ")
    str_pass = input("enter password ➤  ")
    password = str_pass.encode('utf-8')
    # password = bcrypt.hashpw(enc_pass, bcrypt.gensalt(10))
    return username, password

def security_question_answers():
    question_one = input("what is your date of birth ➤  ")
    question_two = input("what is your favorite food ➤  ")
    return question_one, question_two

def username_validation():
    choice = int(input("invalid username\n1.reset\n2.register\nenter choice ➤  "))
    return choice

def registration_details():
    username = input("enter username ➤  ")
    str_pass = input("enter password ➤  ")
    question_one = input("what is your date of birth (e.g. september 24 2000) ➤  ")
    question_two = input("what is your favorite food (e.g. noodles) ➤  ")
    enc_pass = str_pass.encode('utf-8')
    password = bcrypt.hashpw(enc_pass, bcrypt.gensalt(10))
    return username, password, question_one, question_two

def check_if_correct_answers(question_one, question_two):
    from model_object import question_one_model_object, question_two_model_object, login_model_id_object, get_id
    
    #converting objects containing answers to lists
    first_question_list = list(question_one_model_object)
    second_question_list = list(question_two_model_object)
    login_model_id = list(login_model_id_object)
    
    #converting answers list to lowercase
    answer_list_one = [item.lower() for item in first_question_list]
    answer_list_two = [item.lower() for item in second_question_list]
    
    try:
        index_one = answer_list_one.index(question_one.lower()) + 1
        index_two = answer_list_two.index(question_two.lower()) + 1
        # print(f"INDEX_ONE: {index_one}\tINDEX_TWO: {index_two}")
        if index_one == index_two:
            for index, question in enumerate(answer_list_one):
                if question.lower() == question_one.lower() and second_question_list[index].lower() == question_two.lower():
                    row_id = get_id(question_one)
                    return row_id
        else:
            print("❌ security questions answered incorrectly")
            exit()    
    except:
        print("❌ security questions answered incorrectly")
        exit()

def home_options():
    choice = int(input("1. add new password\n2. view saved passwords\n3. logout\nenter choice ➤  "))
    return choice

def get_password_details(username):
    url = input("enter url ➤  ")
    uname = username
    password = generate_password()
    return url, password, uname

def generate_password():
    import random
    
    ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    smb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    letters = int(input("Number of letters in password: ")) 
    symbols = int(input(f"Number of symbols in password: "))
    numbers = int(input(f"Number of integers in password: "))
    passwd = list()
    for char in range(1, letters + 1):
        passwd.append(random.choice(ltr))
    for char in range(1, symbols + 1):
        passwd.append(random.choice(smb))
    for char in range(1, numbers + 1):
        passwd.append(random.choice(num))
    random.shuffle(passwd)
    password = ""
    for p in passwd:
        password += p
    return password

