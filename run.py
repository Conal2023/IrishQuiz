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

print("Hello and welcome to the Irish Quiz")
score = 0

# QUESTION 1
answer1 = input("What is the Capital of Ireland? \
    \na. Limerick \nb. Cork \nc. Dublin \nAnswer: ")
if answer1 == "c" or answer1 == "Dublin":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Dublin")
    print("Score: ", score)
    print("\n")

# QUESTION 2
answer2 = input("What provence of Ireland is Dublin in? \
    \na. Ulster \nb. Leinster \nc. Munster  \nAnswer: ")
if answer2 == "b" or answer2 == "Leinster":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Leinster")
    print("Score: ", score)
    print("\n")

# QUESTION 3
answer3 = input("What is largest county in Ireland? \
    \na. Cork \nb. Limerick \nc. Kerry \nAnswer: ")
if answer3 == "a" or answer3 == "Cork":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Cork")
    print("Score: ", score)
    print("\n")

# QUESTION 4
answer4 = input("What is the most northerly county in Ireland? \
 \na. Derry \nb. Donegal \nc. Antrim \nAnswer: ")
if answer4 == "b" or answer4 == "Donegal":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Donegal")
    print("Score: ", score)
    print("\n")

# QUESTION 5
answer5 = input("Which famous river runs through Dublin? \
     \na. Shannon  \nb. Liffey \nc. Lee \nAnswer: ")
if answer5 == "b" or answer5 == "Liffey":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Liffey")
    print("Score: ", score)
    print("\n")

# QUESTION 6
answer6 = input("Which County K has the Nore and the Barrow? \
 \na. Kildare \nb. Kerry \nc. Kilkenny \nAnswer: ")
if answer6 == "c" or answer6 == "Kilkenny":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is ")
    print("Score: ", score)
    print("\n")

# QUESTION 7
answer7 = input("Athlone is situated at the southern end of which lake? \
     \na. Lough Ree \nb. Lough Leane \nc. Lough Neagh \nAnswer: ")
if answer7 == "a" or answer7 == "Lough Ree":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is ")
    print("Score: ", score)
    print("\n")

# QUESTION 8
answer8 = input("Name the county town of Leitrim? \
     \na. Leitrim \nb. Carrick-On-Shannon \nc. Cloone \nAnswer: ")
if answer8 == "b" or answer8 == "Carrick-On-Shannon":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Carrick-On-Shannon")
    print("Score: ", score)
    print("\n")

# QUESTION 9
answer9 = input("What is the largest park in Dublin? \
    \na. Phoenix Park \nb. Iveagh Gardens \nc. St Stephen's Green \nAnswer: ")
if answer9 == "a" or answer9 == "Phoenix Park":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Phoenix Park")
    print("Score: ", score)
    print("\n")

# QUESTION 10
answer10 = input("What is the smallest County in Ireland? \
     \na. Carlow \nb. Leitrim \nc. Louth \nAnswer: ")
if answer10 == "c" or answer10 == "Louth":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Louth")
    print("Score: ", score)
    print("\n")

# FINAL MESSAGE
if score <= 3:
    print("Your total score is:", score, "- Your not Irish!")
elif score <= 7:
    print("Your total score is:", score, "- Your getting there!")
else:
    print("Your total score is:", score, "- Your Irish!")


