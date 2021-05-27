# What is Armstrong number? - In number theory, a narcissistic number (also known as a pluperfect digital invariant (PPDI), an Armstrong number (after Michael F. Armstrong)
# or a plus perfect number) in a given number base. is a number that is the sum of its own digits each raised to the power of the number of digits.

# In these lines of code we will search for Armstrong numbers in the range we want.


for i in range(1,500): # 1- We create a loop in the interval we want.
    
    i=str(i) # 2- We define the numbers in the list as a sequence.
    
    number_of_digits=len(i) # 3- We determine the length of the number of digits.
    
    i=int(i) # 4- After this determination, we convert our number back to a whole number.
    
    step=0
            #  We define 2 variables, number and sum and equal to 0.
    total=0
    
    temporary_number=i # 5- And we define a temporary number variable to use the number in the list and equalize it for the number.

    while temporary_number>0: # As long as the temporary number is greater than 0, we will do the following.
        
        step=temporary_number%10 # 6- We define the number remaining after dividing the temporary number by 10 to the digit variable.(So we determined one digit of the number.)
        
        total=total+step**number_of_digits # 7- we did "step" to the power of "number of the digits". And We add this to the sum variable.
        
        temporary_number=temporary_number//10 # 8- to reach each digit of the temporary number.

    if total==i: # And if total == i we print it on the screen.
        print(i)
