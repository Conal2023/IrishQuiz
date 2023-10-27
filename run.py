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
if answer2 == "b" or answer1 == "Leinster":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is Leinster")
    print("Score: ", score)
    print("\n")