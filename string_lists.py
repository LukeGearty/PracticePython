def user_input():
    string = input("Enter a word or phrase and I'll see if it is a palindrome: ")
    return string
def palindrome():
    user_string = user_input()
    compare = ""
    punctuation = "!.?"
    for char in user_string:
        if char != " " and char not in punctuation:
            compare += char.lower()
    rev_string = compare[::-1]
    if rev_string == compare:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")
palindrome()
