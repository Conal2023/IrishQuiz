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
    input("Press Enter to start the quiz")
    print("Hello and welcome to the Irish Quiz")
    print("Good luck!")
    question_one()


def question_one():
    score = 0
    # QUESTION 1
    answer1 = input("What is the Capital of Ireland? \
    \n1. Limerick \n2. Cork \n3. Dublin \nAnswer: ").lower()
    if answer1 == "3" or answer1 == "dublin":
        score = correct_answer(score)
    else:
        wrong_answer("Dublin", score)

    question_two(score)


def question_two(score):

    # QUESTION 2
    answer2 = input("What province of Ireland is Dublin in? \
    \n1. Ulster \n2. Leinster \n3. Munster \nAnswer: ").lower()
    if answer2 == "2" or answer2 == "leinster":
        score = correct_answer(score)
    else:
        wrong_answer("Leinster", score)

    question_three(score)


def question_three(score):

    # QUESTION 3
    answer3 = input("What is the largest county in Ireland? \
    \n1. Cork \n2. Limerick \n3. Kerry \nAnswer: ").lower()
    if answer3 == "1" or answer3 == "cork":
        score = correct_answer(score)
    else:
        wrong_answer("Cork", score)

    question_four(score)


def question_four(score):

    # QUESTION 4
    answer4 = input("What is the most northerly county in Ireland? \
    \n1. Derry \n2. Donegal \n3. Antrim \nAnswer: ").lower()
    if answer4 == "2" or answer4 == "donegal":
        score = correct_answer(score)
    else:
        wrong_answer("Donegal", score)

    question_five(score)


def question_five(score):

    # QUESTION 5
    answer5 = input("Which famous river flows through Dublin \
    \n1. Shannon \n2. Liffey \n3. Lee \nAnswer: ").lower()
    if answer5 == "2" or answer5 == "liffey":
        score = correct_answer(score)
    else:
        wrong_answer("Liffey", score)

    question_six(score)


def question_six(score):

    # QUESTION 6
    answer6 = input("Which County K has the Nore and the Barrow? \
    \n1. Kildare \n2. Kerry \n3. Kilkenny \nAnswer: ").lower()
    if answer6 == "3" or answer6 == "kilkenny":
        score = correct_answer(score)
    else:
        wrong_answer("Kilkenny", score)

    question_seven(score)


def question_seven(score):

    # QUESTION 7
    answer7 = input("Athlone is situated at the southern end of which lake? \
    \n1. Lough Ree \n2. Lough Leane \n3. Lough Neagh \nAnswer: ").lower()
    if answer7 == "1" or answer7 == "lough ree":
        score = correct_answer(score)
    else:
        wrong_answer("Lough Ree", score)

    question_eight(score)


def question_eight(score):

    # QUESTION 8
    answer8 = input("Name the county town of Leitrim? \
    \n1. Leitrim \n2. Carrick-On-Shannon \n3. Cloone \nAnswer: ").lower()
    if answer8 == "2" or answer8 == "carrick-on-shannon":
        score = correct_answer(score)
    else:
        wrong_answer("Carrick-On-Shannon", score)

    question_nine(score)


def question_nine(score):

    # QUESTION 9
    answer9 = input("What is the largest park in Dublin? \
    \n1. Phoenix Park \n2. Iveagh Gardens \n3. St Stephen's Green \
    \nAnswer:").lower()
    if answer9 == "1" or answer9 == "phoenix park":
        score = correct_answer(score)
    else:
        wrong_answer("Phoenix Park", score)

    question_ten(score)


def question_ten(score):

    # QUESTION 10
    answer10 = input("What is the smallest County in Ireland? \
    \n1. Carlow \n2. Leitrim \n3. Louth \nAnswer: ").lower()
    if answer10 == "3" or answer10 == "louth":
        score = correct_answer(score)
    else:
        wrong_answer("Louth", score)


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
