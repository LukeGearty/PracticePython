list_one = [1,3,5,7,9,11]
list_two = [1,5,9,100,102,105,109]

def list_overlap(list_one,list_two):
    return_list = []

    for char in list_one:
        if char in list_two:
            return_list.append(char)

    return return_list


print(list_overlap(list_one,list_two))
