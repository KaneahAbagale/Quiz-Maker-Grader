# Movie Ticket Pricing


age = int(input("How old are you?\n"))
is_student = (input("Are you a student? Type 1 for yes and 2 for no\n")) == "1"
is_matinee = (input("Do you want the movie matinee? Type 1 for yes and 2 for no\n")) == "1"

# Ticket pricing criteria
if age < 12:
    print("The ticket price is $5")
elif is_student or is_matinee:
    print("The ticket price is $8")
else:
    print("The ticket price is $12") 
    




