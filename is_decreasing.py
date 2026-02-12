#Author:Gabriel Venegas
#Github:GVenegas1
#Feb 11, 2026
#Description: Checking if every single step goes down.If the first one is bigger than
#the second one, you move to the next pair and check again. If you ever find a number that
#is smaller than or equal to the one after it,you return False.


def check_going_down(my_list):
    """This function checks if numbers in a list keep getting smaller.
        Each number has to be less than the one before it.Returns True if they keep going down,
        False if they don't"""

    #if there's only 2 numbers left, just compare them
    if len(my_list) == 1:
        if my_list[0] > my_list[1]:
            return True
        else:
            return False

    #check if the first number is bigger than the second number
    if my_list[0] > my_list[1]:
        #now check the rest of the list without the first number
        return check_going_down(my_list[1:])
    else:
        #first number isn't bigger so the list isn't decreasing
        return False

