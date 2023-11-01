def intro():
    print(
        """
    ██╗██████╗ ██╗███████╗██╗  ██╗     ██████╗ ██╗   ██╗██╗███████╗
    ██║██╔══██╗██║██╔════╝██║  ██║    ██╔═══██╗██║   ██║██║╚══███╔╝
    ██║██████╔╝██║███████╗███████║    ██║   ██║██║   ██║██║  ███╔╝
    ██║██╔══██╗██║╚════██║██╔══██║    ██║▄▄ ██║██║   ██║██║ ███╔╝
    ██║██║  ██║██║███████║██║  ██║    ╚██████╔╝╚██████╔╝██║███████╗
    ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
        """
    )
    print("Welcome to the Irish Quiz!")
    input("Press Enter to start the quiz") # wait for user to press enter
    print("Hello and welcome to the Irish Quiz")
    print("Good luck!")
    question_one()

def question_one():
    score = 0
    # QUESTION 1
    answer1 = input("What is the Capital of Ireland? \n1. Limerick \n2. Cork \n3. Dublin \nAnswer: ").lower()
    if answer1 == "3" or answer1 == "dublin":
        score = correct_answer(score)
    else:
        wrong_answer("Dublin", score)
    
    question_two(score)

def wrong_answer(correct_answer, score):
    print("Incorrect! The answer is " + correct_answer)
    print("Score: ", score)
    print("\n")

def correct_answer(score):
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
    return score
intro()