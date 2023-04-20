def ask_name():
    name = input("Enter your name: ")
    return name
def ask_age():
    age = input("Enter your age: ")
    return age
def ask_num():
    num = input("Enter how many times you want this message: ")
    return num
def year_hundred():
    name = ask_name()
    age = int(ask_age())
    num = int(ask_num())
    year = 2023 + (100-age)
    print(("Your name is " + name + " and you will be 100 years old by " + str(year) + '\n')*num)
year_hundred()
