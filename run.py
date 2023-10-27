print("Hello and welcome to the Irish Quiz")
score = 0

# QUESTION 1
answer1 = input("What is the Capital of Ireland? \na. Limerick \nb. Cork \
\nc. Dublin \nAnswer: ")
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
answer2 = input("What provence of Ireland is Dublin in? \na. Ulster \
 \nb. Leinster \nc. Munster  \nAnswer: ")
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
answer3 = input("What is the only county that doesn't touch another \
county which touches the sea? \na. Laois \nb. Offaly \nc. Kildare \nAnswer: ")
if answer3 == "a" or answer3 == "Laois":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Laois")
    print("Score: ", score)
    print("\n")

# QUESTION 4
answer4 = input("What is the most northerly county in Ireland \
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

# QUESTION 
answer = input(" \na.  \nb.  \nc.  \nAnswer: ")
if answer == "" or answer == "":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is ")
    print("Score: ", score)
    print("\n")