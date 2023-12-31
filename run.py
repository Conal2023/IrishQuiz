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
    \na. Limerick \nb. Cork \nc. Dublin \nAnswer: ")
    if answer1 in ['a', 'b', 'c']:
        if answer1 == "c":
            score = correct_answer(score)
        else:
            wrong_answer("Dublin", score)
    elif answer1 in ['1', '2', '3']:
        if int(answer1) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("Dublin", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Ulster \nb. Leinster \nc. Munster \nAnswer: ")
    if answer2 in ['a', 'b', 'c']:
        if answer2 == "b":
            score = correct_answer(score)
        else:
            wrong_answer("Leinster", score)
    elif answer2 in ['1', '2', '3']:
        if int(answer2) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Leinster", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Cork \nb. Limerick \nc. Kerry \nAnswer: ")
    if answer3 in ['a', 'b', 'c']:
        if answer3 == "a":
            score = correct_answer(score)
        else:
            wrong_answer("Cork", score)
    elif answer3 in ['1', '2', '3']:
        if int(answer3) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("Cork", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Derry \nb. Donegal \nc. Antrim \nAnswer: ")
    if answer4 in ['a', 'b', 'c']:
        if answer4 == "b":
            score = correct_answer(score)
        else:
            wrong_answer("Donegal", score)
    elif answer4 in ['1', '2', '3']:
        if int(answer4) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Donegal", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Shannon \nb. Liffey \nc. Lee \nAnswer: ")
    if answer5 in ['a', 'b', 'c']:
        if answer5 == "b":
            score = correct_answer(score)
        else:
            wrong_answer("Liffey", score)
    elif answer5 in ['1', '2', '3']:
        if int(answer5) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Liffey", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Kildare \nb. Kerry \nc. Kilkenny \nAnswer: ")
    if answer6 in ['a', 'b', 'c']:
        if answer6 == "c":
            score = correct_answer(score)
        else:
            wrong_answer("Kilkenny", score)
    elif answer6 in ['1', '2', '3']:
        if int(answer6) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("Kilkenny", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Lough Ree \nb. Lough Leane \nc. Lough Neagh \nAnswer: ")
    if answer7 in ['a', 'b', 'c']:
        if answer7 == "a":
            score = correct_answer(score)
        else:
            wrong_answer("Lough Ree", score)
    elif answer7 in ['1', '2', '3']:
        if int(answer7) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("Lough Ree", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Leitrim \nb. Carrick-On-Shannon \nc. Cloone \nAnswer: ")
    if answer8 in ['a', 'b', 'c']:
        if answer8 == "b":
            score = correct_answer(score)
        else:
            wrong_answer("Carrick-On-Shannon", score)
    elif answer8 in ['1', '2', '3']:
        if int(answer8) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Carrick-On-Shannon", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Phoenix Park \nb. Iveagh Gardens \nc. St Stephen's Green \
    \nAnswer: ")
    if answer9 in ['a', 'b', 'c']:
        if answer9 == "a":
            score = correct_answer(score)
        else:
            wrong_answer("Phoenix Park", score)
    elif answer9 in ['1', '2', '3']:
        if int(answer9) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("Phoenix Park", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
    \na. Carlow \nb. Leitrim \nc. Louth \nAnswer: ")
    if answer10 in ['a', 'b', 'c']:
        if answer10 == "c":
            score = correct_answer(score)
        else:
            wrong_answer("Louth", score)
    elif answer10 in ['1', '2', '3']:
        if int(answer10) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("Louth", score)
    else:
        print("Please enter 'a', 'b','c' or '1', '2', '3'")
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
