#Write a function to count the number of words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)
print(count_words("This is a simple sentence"))
#----------------------
#Write a function to return the length of a string without using len().
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
print(string_length("Hello"))
#--------------------
#Write a function to return the square and cube of a number.
def square_and_cube(n):
    return n**2, n**3
sq, cb = square_and_cube(2)
print("Square:", sq)
print("Cube:", cb)
#-------------------
#Write a function to find the smallest digit in a number.
def smallest_digit(num):
    digits = [int(d) for d in str(num)]
    return min(digits)
print(smallest_digit(7532))
#----------------
# Write a function to return True if a number is divisible by both 3 and 5.
def divisible_by_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0
print(divisible_by_3_and_5(5))  
print(divisible_by_3_and_5(30)) 
#-----------------
#Write a program to add two numbers.
def add(a, b):
    return a + b
print(add(5, 3))
#-----------------
#Write a program to subtract two numbers.
def add(a, b):
    return a - b
print(add(10,4))
#---------------
# Write a program to multiply two numbers.
def add(a, b):
    return a * b
print(add(2,4))
#-------------
#Write a program to divide two numbers.
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Example
print(divide(20, 4))
#-----------------
#Write a program to calculate the square of a number.
def square(n):
    return n * n
print(square(9))
#------------------------------------------------------------

