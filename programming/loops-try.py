
number = input("Give me a whole number below 45 ")

valid = False

while valid != True:
    try:
        number = int(number)
        valid = True
    except:
        number = input("Give me a whole number below 45 ")
        
number2 = number
    
while number2 >= 0:
    print(str(number) + "x" + str(number2) + "=" + str(number * number2))
    number2 -= 1

  
