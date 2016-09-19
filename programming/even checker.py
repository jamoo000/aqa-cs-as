def even():
    number = int(input('enter number'))
    if number % 2 == 0:
        print ('even number')
        even()
    else:
        print ('odd number')
        even()

even()
