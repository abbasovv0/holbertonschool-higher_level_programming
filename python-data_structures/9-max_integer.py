#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    
    largest_num = my_list[0]

    for num in my_list[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num
my_list = [3,4,1,0,-2,7,9,10]
print(f"biggest number:{max_integer(my_list)}")
