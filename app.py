from model_object import get_user_data


def add_password(username):
    from utils import get_password_details
    from model_object import insert_password_into_creds_model, get_user_data
    
    details = get_password_details(username)
    insert_status = insert_password_into_creds_model(details[0], details[1], details[2])
    return insert_status

def show_all_passwords(username):
    retrieved_data = get_user_data(username)
    for data in retrieved_data:
        print(f"URL: {data['url']}\t\t\tPASSWORD: {data['password']}")
    return True