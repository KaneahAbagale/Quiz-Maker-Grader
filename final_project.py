#Quiz Maker & Grader Project

# This system will allow users (Students and Admin) to:
# • Attempt a quiz with 10 multiple-choice Python questions

# • Admins should be able to add questions to the existing set of questions

# • Select answers by choosing A, B, C, or D

# • The user should be able to view immediate feedback for each question (Correct/Incorrect)

# • The user should be able to see their final score at the end of the quiz

# • The user's score should be saved to a .txt file for record-keeping


# A dictionary that already has 10 questions stored. The dictionary is required to have a total of 10 question.

#Quiz questions that students can answer, and it provides the correct answer

quiz_questions = {
    "What is the correct file extension for Python files?\n": {
        "options": ["A. .pt", "B. .pyth", "C. .py", "D. .python"],
        "answer": "B"
},

    "What is the output of: print(3 * 'Hi ')\n":{
        "options": ["A. Hi", "B. Hi Hi", "C. HiHiHi", "D. Hi Hi Hi"],
        "answer": "D"
    },

    "Which of the following is a valid variable name in Python?\n":{
        "options": ["A. user_name", "B. Name2", "C. user-name", "D. 2name"],
        "answer": "A"
    },

    "What data type is the result of: input('How old are you?\n')":{
        "options": ["A. boolean", "B. string", "C. integer", "D. float"],
        "answer": "B"
    },

    "How do you start a comment in Python?\n')":{
        "options": ["A. ||", "B. --", "C. #", "D. %"],
        "answer": "C"
    },

    "Which operator is used for exponentiation in Python?\n')":{
        "options": ["A. **", "B. --", "C. #", "D. !!"],
        "answer": "A"
    },

    "Which keyword is used to create a loop in Python?\n')":{
        "options": ["A. for", "B. if", "C. loop", "D. when"],
        "answer": "A"
    },

    "What will the following expression return: 5 == 5.0?\n')":{
        "options": ["A. True", "B. False", "C. None", "D. Error"],
        "answer": "A"
    },

    "The difference in writing a tuple and a list is":{
        "options": ["A. (),{}", "B. {},[]", "C. (),[]", "D. None of the above"],
        "answer": "C"
    },

    "What does the len() function do?":{
        "options": ["A. (Returns the size of a number", "B. Returns the length of an object", "C. Returns the largest number", "D. All of the above"],
        "answer": "B"
    }
}


# The system should allow the Admin to add more questions and options that can be added to the existing dictionary
#This function allows Admin to add custom questions, options and correct answer.
def add_custom_questions():
    print("\n📝 Add Your Own Questions (type 'done' to stop)\n")

    # This loop collects multiple-choice questions where the user is required to input four options and specify the correct answer. 
    while True:
        question = input("Enter your question (or type 'done' to finish): ")
        if question.lower() == "done":
            break
        options = [] 
        for i in ["A", "B", "C", "D"]:
            option = input(f" Enter option {i}: ")
            options.append(f"{i}. {option}")
        answer = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            quiz_questions[question] = {"options": options, "answer": answer}
            print("✅ Question added!\n")
        else:
            print("❌ Invalid answer. Please use A, B, C, or D.\n")


#The quiz function will loop through the questions and grade them based on the student's answer  

#This function allows a user to take a quiz, tells the user if the answer to a question is correct or not and show their final score
def run_quiz():
    print("\n🧠 Welcome to the Quiz!! Type A, B, C, or D to answer.")
    score = 0
    total = len(quiz_questions)

    #A loop to check the answer to questions in the dictionary
    for question, details in quiz_questions.items():
        print("\n" + question)
        for option in details["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()

        #A condition to check if the answer provided is correct
        if answer == details["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {details['answer']}.")

    print(f"\n 🏁 Quiz Complete! Your final score is {score}/{total}")
    return score, total    

#Save Quiz Results to a File  

#This function lets students save their name and score to a text file
def save_score(name, score, total):
    with open("quiz_scores.txt", "a") as file:
        file.write(f"{name}: {score}/{total}\n")
    print("📂 Your score has been saved!\n")
    
# Function for the main program.
# The function will prompt the student to enter their role and based on the input, decide if they can add questions to the dictionary.

#Function for main program

def main():
    print("🎉 Welcome to the Quiz Maker & Grader!")
    name = input("Enter your name: ")
    role = input("Enter your role (admin/student): ").lower()

    # condition to check the role of the person
    if role == "admin":
        print(f"\n🔐 Admin Access Granted. Hello, {name}!")
        add_q = input("Would you like to add your own questions? (yes/no): ").lower()
        if add_q == "yes":
            add_custom_questions()
        elif role == "student":
            print(f"\n 👋🏽 Hello, {name}! Let's begin your quiz.")
        else:
            print("❌ Invalid role. Exiting program.")
            return
            
        score, total = run_quiz()
        save_score(name, score, total)
        
