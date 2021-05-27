#  What is perfect number ? - In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
#  For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number. 

# These codes allow us to find the perfect numbers at intervals we set.

def Perfect(number):  # 1- Defining a function that takes a single number parameter.
    
    total = 0 

    for i in range(1, number): # 2- Then, thanks to the range function, we create a list between 1 and the parameter from the function and loop it.

        if (number % i == 0):  # 3- Next, we divide our parameter by each number in this list, and if the remainder is equal to 0, we add it to the variable sum.
            total += i 

    return total == number # 4- and if this equals the total number, we return it.


## In this part of the lines of code, we can create a loop at the interval we want and run the function at the interval we want ##
for i in range(1, 1000000):
    if (Perfect(i)):
        print("Perfect Number is :", i)
