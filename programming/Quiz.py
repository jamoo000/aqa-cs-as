#Exercise 1- Quiz

def start ():
    print ("please answer these questions")
    questions()
    endgame()
    
def questions():
    score = 0
    userchoice = input("1)what is the capital of France?").upper()
    if userchoice == 'PARIS':
        score = score + 1
        print ("correct")
    else:
        print ("incorrect")

    userchoice = input("2)What is the sum of 5674 + 9880 ?")
    if int(userchoice) == (5674 + 9880):
        print ("correct")
        score = score + 1
    else:
        print ("incorrect")

    userchoice = input("3)What is 5674 - 9880?")
    if userchoice.isnumeric() == True:
        if int(userchoice) == (5674 - 9880):
            print ("correct")
            score = score + 1
    else:
        print ("incorrect")

    userchoice = input("4)what is 5674 x 9880?")
    if userchoice.isnumeric() == True:
        if int(userchoice) == (5674 * 9880):
            print ("correct")
            score = score + 1
    else:
        
        print ("incorrect")

    userchoice = input("5)what is the result of 5674 divided by 9 to 5 significant figures?")
    if int(userchoice) == (630.45):
        print ("correct")
        score = score + 1
    else:
        print ("incorrect")

    userchoice = input("6)what is the remainder of 5674 divided by 9?")
    if userchoice.isnumeric() == True:
        if int(userchoice) == (5674 % 9):
            print ("correct")
            score = score + 1
    else:
        print ("incorrect")


    userchoice = input("6)what is the year the first episode of Doctor Who was aired on TV?")
    if userchoice.isnumeric() == True:
        if int(userchoice) == '1963':
            print ("correct")
            score = score + 1
    else:
        print ("incorrect")

    print("You scored: " + str(score))

def endgame():
    userchoice = input("do you want to try again?").upper()
    if userchoice == 'YES':
        questions()
    else:
        print ("goodbye") 
start()
