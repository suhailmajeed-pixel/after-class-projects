def shutdown(choice):
    if choice == "YES":
        print("!!!Shutting down!!!")

    elif choice == "NO":
        print("OK! abort the shutdown ")
   
    elif choice == "yes":
        print("PLEASE WRITE IN CAPITAL")

    elif choice == "no":
        print("PLEASE IN CAPITAL")

    else:
        print("ONLY WRITE YES OR NO")

user_choice = input("Do you want to shutdown the system? (Yes/No): ")

shutdown(user_choice)
