# Grade calculator

score = int(input("Enter a score from 0-100.\n"))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("F")
else:
    print("Invalid score. Please enter a value between 0 and 100.")
    