def start_app():
    from user_authentication import login_args, register_args

    SESSION_STATUS = None
    option = input("1. login\n2.register\nenter choice ➤  ")
    if option == '1':
        status = login_args()
        SESSION_STATUS = status[0]
        if SESSION_STATUS:
            print(f"✅ {status[1]} logged in successfully")
        while SESSION_STATUS:
            from utils import home_options
            from app import add_password, show_all_passwords
            
            home_choice = home_options()
            while home_choice > 0:
                if home_choice == 1:
                    print("adding new password")
                    check_status = add_password(status[1])
                    if check_status:
                        print("✅ password added")
                        SESSION_STATUS = check_status
                        break
                    else:
                        print("❌ an unexpected error occured")
                elif home_choice == 2:
                    print("getting all saved credentials")
                    check_status = show_all_passwords(status[1])
                    if check_status:
                        print("✅ retrived all passwords")
                        SESSION_STATUS = check_status
                        break
                    else:
                        print("❌ an unexpected error occured")
                elif home_choice == 3:
                    print("logging out")
                    SESSION_STATUS = False
                    break
                else:
                    print("❌ invalid option")
                    home_choice = home_options()
    elif option == '2':
        status = register_args()
        if status:
            print("✅ user added successfully")
            exit()
    elif option == "":
        print('❗ please select an option ❗')
    else:
        print('❗ invalid option ❗')

if __name__ == '__main__':
    start_app()

