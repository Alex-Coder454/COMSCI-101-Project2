# SDM: Here I am making a program modeled after the Autofocus application.  The purpose of this program will be to make a
#      task management software so that one can input tasks that they have into a list, they may delete the entire list, 
#      they could mark items as done within the list, have the ability to view the list, and have the option to quit whenever 
#      they would prefer to.  It will use a series of functions to generate the outputs, compute these instructions, and 
#      then output the desired results.

to_do_list = []

option_list = ["Quit the Task Wizard Software", "Add Item to List", "Mark Item as Complete", "See Your Current List", "Clear Your List", "Delete Item from List",]

def print_welcome_statement():
    """Prints out initial welcoming statement."""
    print("Welcome to Alex's version of the Autofocus application called: Task Wizard.")

def show_option_list():
    """Shows the list of options that one can choose from like a main menu,"""
    print("Here are the options that you can choose from.\n")
    for num in range(len(option_list)):
        print(f"{num + 1}:{option_list[num]}")

def quitting():
    """Prints out a closing statement after user quits the program."""
    print("You are now quitting the Task Wizard Software.  We hope our application helped you manage your tasks well this time!")

def showing():
    """Shows the user's current to-do-list for their view."""
    print("Here is your list at the moment:\n")
    for num in range(len(to_do_list)):
        print(f"[]:{to_do_list[num]}")

def adding():
    """Enables user to add some input of their own to the to-do-list they are creating."""
    print("You would like to add something to your to-do list.  What would you prefer to add?")
    List_Item = input("> ")
    to_do_list.append(List_Item)
    print(f"You added '{List_Item}' to your to-do list.")
    return to_do_list

def deleting(list):
    """Enables user to get rid of a list item of their choosing with the prior list as the input and updated list as the output."""
    print("You would like to delete something from your to-do list.  Which item would you prefer to delete from the list?")
    for num in range(len(list)):
        print(f"{num + 1}:{list[num]}")
    print("Please input a number.")
    Delete_Item = None
    while not isinstance(Delete_Item, int):
        try:
            Delete_Item = int(input("> "))
            list_length = int(len(list)) + 1
            if (Delete_Item > 0) and (Delete_Item < (list_length)):
                index = int(Delete_Item) - 1
                print(f"You deleted '{list[index]}' from your to-do list.")
                to_do_list = list.pop(index) 
                return to_do_list
            else: 
                print("The number must be in the range of the numbers given from the list above.\n")
        except ValueError:
            print("Invalid input.  Please enter a valid number according to the item numbers above.")

def clearing():
    """Enables user to get rid of all items from their list with a fresh blank list as the output."""
    print("You will be clearing your list.\n")
    to_do_list.clear()
    print(f"Your list now is: {to_do_list}\n")
    return to_do_list

def updated_list(list, num):
    """A nested function to create the formatting for a marked item from the list.  Gives back a new list as output."""
    index = int(num - 1)
    item = list[index]
    for item in list:
        new_value = (f"[x]:{item}")
        list[index] = new_value
    return list
        
def marking(list):
    """Enables user to mark an item in the list as done with the prior list as the input and updated list as the output."""
    print("You are wanting to mark (an) item(s) as complete.  What/which item(s) would you prefer to mark done?")
    for num in range(len(to_do_list)):
        print(f"{num + 1}:{to_do_list[num]}")
    print("Please input a number.")
    Mark_Item = None
    while not isinstance(Mark_Item, int):
        try:
            Mark_Item = int(input("> "))
            list_length = int(len(list)) + 1
            if (Mark_Item > 0) and (Mark_Item < (list_length)):
                updated_list(list, Mark_Item)
                return list
            else: 
                print("The number must be in the range of the numbers given from the list above.\n")
        except ValueError:
            print("Invalid input.  Please enter a valid number according to the item numbers above.")

def checking():
    """Nested function that checks whether the given input is in the correct format to apply.  Only outputs if correct."""
    answer = None
    while not isinstance(answer, int):
        try:
            answer = int(input("> "))
            if (answer > 0) and (answer < 7):
                return answer
            else: 
                print("The number must be in the range of the numbers given from the list above.\n")
        except ValueError:
            print("Invalid input.  Please enter a valid number according to the item numbers above.")
    
def provide_input(): 
    """Enables user to give a choice regarding what they would like to do with the program.""" 
    print("Please select a number choice from the list and input that below.\n")
    show_option_list()
    answer = checking()
    Choosing = True
    while Choosing:
        if ((len(option_list)) > 1):
            return answer
        elif (len(option_list == 1)):
            if (answer < 6):
                return answer
            elif (answer < 7):
                print("You cannot delete one item from a list with just one in it.  Try to clear the list instead.")
            else:
                print("Please choose a valid number from 1-6.  Please select from either adding an item to the list, clearing the list, checking the list, marking as complete, or quitting the program altogether.")
        elif (len(option_list == 0)):
            if (answer < 3):
                return answer
            elif (answer < 7):
                print("You cannot delete from the list with no items, you cannot see a list with no items in it, you cannot mark anything as done when there is nothing, or you cannot clear an entire list with nothing to clear.")            
            else:
                print("Please choose a valid number from 1-6.  Please select from either adding an item to the list or quitting the program altogether.")

# Main body of the code starts here.
print_welcome_statement()
print()
Running = True
while Running:
    answer1 = provide_input()
    if (answer1 == 1):
        quitting()
        Running = False
    elif (answer1 == 4):
        showing()
        print()
    elif (answer1 == 2):
        adding()
        print()
    elif (answer1 == 6):
        deleting(to_do_list)
        print()
    elif (answer1 == 5):
        clearing()
    elif (answer1 == 3):
        marking(to_do_list)
    










