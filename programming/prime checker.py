'''write a prime checker for any given numbers
use function(s)  (we will go through this in lessons. you can wait or you can do some research yourself.)
can check any given numbers
extra: print out all primes that are larger than the given number'''

def number():
    num = int(input('input number'))
    if num >1:
        for i in range (2,num):
            if (num%i) == 0:
                print(num,'is not prime')
            else:
                print('It is prime')
                number()

number()
