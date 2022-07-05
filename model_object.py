from model_config.models import LoginModel, UserCredentialsModel

# Login Model Objects
login_model_id_object = LoginModel.objects.values_list('id', flat=True)
username_model_object = LoginModel.objects.values_list('username', flat=True)
password_model_object = LoginModel.objects.values_list('password', flat=True)
question_one_model_object = LoginModel.objects.values_list('security_question_one', flat=True)
question_two_model_object = LoginModel.objects.values_list('security_question_two', flat=True)

# User Credentials Model Objects


def insert_into_login_model(username, password, question_one, question_two):
    insert_data_item = LoginModel(username=username, password=password, security_question_one=question_one, security_question_two=question_two)
    insert_data_item.save()
    return True

def login_model_username_update(row_id, new_username):
    update_data_item = LoginModel.objects.get(id=row_id)
    update_data_item.username = new_username
    update_data_item.save()
    return True

def login_model_password_update(row_id, new_password):
    update_data_item = LoginModel.objects.get(id=row_id)
    update_data_item.password = new_password
    update_data_item.save()
    return True

def get_id(security_question):
    data_object = LoginModel.objects.filter(security_question_one=security_question).values().first()
    return data_object['id']

def insert_password_into_creds_model(url, password, username):
    data_object = UserCredentialsModel(url=url, password=password, username=username)
    data_object.save()
    return True

uname = 'daniel'
def get_user_data(uname):
    data_object = UserCredentialsModel.objects.filter(username=uname).only('url', 'password').values()
    return data_object
get_user_data(uname)