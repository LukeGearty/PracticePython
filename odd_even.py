# Write a program that takes in a user number and prints out if it is odd or even

# the function that takes in the number

def user_num():
    num = int(input("Give me a number: "))
    return num
def odd_or_even():
    num = user_num()
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd!")


odd_or_even()
