def shutdown(choice):
    if choice == "YES":
        print("Shutting down")
    elif choice == "NO":
        print("Abort shutdown")
    else:
        print("Sorry write in capital")

shutdown(input("Shutdown? (Yes/No): "))