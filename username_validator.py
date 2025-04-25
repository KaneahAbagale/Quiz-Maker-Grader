# Create a variable to store Username

user_name = input("Please eneter your user name\n")

#check if user name meets criteria
if len(user_name) >= 10 and user_name[0].isalpha and user_name.isalnum():
    print("Congratulations your user name is valid")
else:
    print("Hey your user name is not valid")