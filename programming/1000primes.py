num = 0
def x():
    enter = input('enter')
    num += 1
    if num > 1:
        for i in range (2,num):
            if (num%i) == 0:
                x()
            else:
                print (num)
                x()
    else:
        x()
               

x()
    
    
    
    
