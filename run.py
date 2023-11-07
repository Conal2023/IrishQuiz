def intro():
    """
    Displays the introduction message, starts the game
    and asks the player if they want to play again.
    """

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
    input("Press Enter to start the quiz")
    print("Hello and welcome to the Irish Quiz")
    print("Good luck!")
    question_one()

    while True:
        play_again_response = input(
            "Do you want to play again? (yes/no): "
            ).lower()
        if play_again_response == "yes":
            question_one()
        elif play_again_response == "no":
            intro()
            break
        else:
            print("Please enter yes or no")


def question_one():
    """
    Displays the first question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    score = 0
    # QUESTION 1
    answer1 = input("Q1: What is the Capital of Ireland? \
    \n1. Limerick \n2. Cork \n3. Dublin \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer1) < 4 and int(answer1) > 0:
            if answer1 == "3":
                score = correct_answer(score)
            else:
                wrong_answer("Dublin", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_one()

    question_two(score)


def question_two(score):
    """
    Displays the second question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 2
    answer2 = input("Q2: What province of Ireland is Dublin in? \
    \n1. Ulster \n2. Leinster \n3. Munster \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer2) < 4 and int(answer2) > 0:
            if answer2 == "2":
                score = correct_answer(score)
            else:
                wrong_answer("Leinster", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_two(score)

    question_three(score)


def question_three(score):
    """
    Displays the third question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 3
    answer3 = input("Q3: What is the largest county in Ireland? \
    \n1. Cork \n2. Limerick \n3. Kerry \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer3) < 4 and int(answer3) > 0:
            if answer3 == "1":
                score = correct_answer(score)
            else:
                wrong_answer("Cork", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_three(score)

    question_four(score)


def question_four(score):
    """
    Displays the fourth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 4
    answer4 = input("Q4: What is the most northerly county in Ireland? \
    \n1. Derry \n2. Donegal \n3. Antrim \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer4) < 4 and int(answer4) > 0:
            if answer4 == "2":
                score = correct_answer(score)
            else:
                wrong_answer("Donegal", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_four(score)

    question_five(score)


def question_five(score):
    """
    Displays the fifth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 5
    answer5 = input("Q5: Which famous river flows through Dublin \
    \n1. Shannon \n2. Liffey \n3. Lee \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer5) < 4 and int(answer5) > 0:
            if answer5 == "2":
                score = correct_answer(score)
            else:
                wrong_answer("Liffey", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_five(score)

    question_six(score)


def question_six(score):
    """
    Displays the sixth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 6
    answer6 = input("Q6: Which County K has the Nore and the Barrow? \
    \n1. Kildare \n2. Kerry \n3. Kilkenny \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer6) < 4 and int(answer6) > 0:
            if answer6 == "3":
                score = correct_answer(score)
            else:
                wrong_answer("Kilkenny", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_six(score)

    question_seven(score)


def question_seven(score):
    """
    Displays the seventh question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 7
    answer7 = input("Q7: Athlone is situated at the \
southern end of which lake? \
    \n1. Lough Ree \n2. Lough Leane \n3. Lough Neagh \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer7) < 4 and int(answer7) > 0:
            if answer7 == "1":
                score = correct_answer(score)
            else:
                wrong_answer("Lough Ree", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_seven(score)

    question_eight(score)


def question_eight(score):
    """
    Displays the eighth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 8
    answer8 = input("Q8: Name the county town of Leitrim? \
    \n1. Leitrim \n2. Carrick-On-Shannon \n3. Cloone \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer8) < 4 and int(answer8) > 0:
            if answer8 == "2":
                score = correct_answer(score)
            else:
                wrong_answer("Carrick-On-Shannon", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_eight(score)

    question_nine(score)


def question_nine(score):
    """
    Displays the nineth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 9
    answer9 = input("Q9: What is the largest park in Dublin? \
    \n1. Phoenix Park \n2. Iveagh Gardens \n3. St Stephen's Green \
    \n Enter 1-3: \nAnswer: ")
    try:
        if int(answer9) < 4 and int(answer9) > 0:
            if answer9 == "1":
                score = correct_answer(score)
            else:
                wrong_answer("Phoenix Park", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_nine(score)

    question_ten(score)


def question_ten(score):
    """
    Displays the tenth question of the quiz,
    Prompts the player to answer the question
    and gives a score.
    """
    # QUESTION 10
    answer10 = input("Q10: What is the smallest County in Ireland? \
    \n1. Carlow \n2. Leitrim \n3. Louth \n Enter 1-3: \
    \nAnswer: ")
    try:
        if int(answer10) < 4 and int(answer10) > 0:
            if answer10 == "3":
                score = correct_answer(score)
            else:
                wrong_answer("Louth", score)
    except ValueError:
        print("Please enter a number between 1 and 3")
        question_ten(score)


def wrong_answer(correct_answer, score):
    """
    Displays the incorrect answer message and the correct answer,
    displays the same score as the previous result.
    """
    print("Incorrect! The answer is " + correct_answer)
    print("Score: ", score)
    print("\n")


def correct_answer(score):
    """
    Displays the correct answer message and adds
    1 to the score.
    """
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
    return score


intro()
