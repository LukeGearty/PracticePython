# Create a program that gets user input for a number
def get_num():
    num = int(input("Give me a number: "))
    return num
# Create a function that lists out the divisors of that number
def divisors():
    user_num = get_num()
    divisor_list = []
    for num in range(1,user_num+1):
        if user_num%num == 0:
            divisor_list.append(num)
    print(divisor_list)
