# SDM: Here I am making a program modeled after the Autofocus application.  The purpose of this program will be to make a
#      task management software so that one can input tasks that they have into a list, they may delete the entire list, 
#      they can prioritize items in the list, they could mark items as done within the list, have the ability to view the 
#      list, and have the option to quit whenever they would prefer to.  It will use a series of functions to generate 
#      the outputs, compute these instructions, and then output the desired results.

class Program: # creating Program class to make program's framework

    def __init__(self): # creates the lists with self calling function to implement into later functions
        """Takes in self parameter and produces an empty list to start to_do_list as well as a list with options to start option_list."""
        self.to_do_list = []
        self.option_list = ["Quit the Task Wizard Software", "Add Item to List", "Delete Your List", "Prioritize List", "Mark Ready Item as Complete", "See The List"]
    
    def print_welcome_statement(self): 
        """Prints out initial welcoming statement."""
        print("Welcome to Alex's version of the Autofocus application called: Task Wizard.")
    
    def show_option_list(self):
        """Shows the list of options that one can choose from like a main menu,"""
        print("Here are the options that you can choose from.\n")
        for num in range(len(self.option_list)): # lines 21, 22 print out the option list numbered for easy understanding and user interaction.
            print(f"{num + 1}:{self.option_list[num]}")
    
    def quitting(self):
        """Prints out a closing statement after user quits the program."""
        print("You are now quitting the Task Wizard Software.  We hope our application helped you manage your tasks well this time!")
    
    def adding(self):
        """Enables user to add some input of their own to the to-do-list they are creating."""
        print("You would like to add something to your to-do list.  What would you prefer to add?")
        List_Item = input("> ") 
        self.to_do_list.append({"item":List_Item, "status":"ready"}) # adds to the end of the list a dictionary with the item inputted and the status of that item as ready
        if len(self.to_do_list) > 1: 
            for num in range(len(self.to_do_list)):
                a = self.to_do_list[num]
                if num != 0:
                    a["status"] = "new" # reformats the previous 'ready' list items with the 'new' status instead as they are not yet prioritized
        print(f"You added '{List_Item}' to your to-do list.")
    
    def clearing(self):
        """Enables user to get rid of all items from their list with a fresh blank list as the output."""
        print("You will be clearing your list...\n")
        self.to_do_list.clear() # deletes the entire list and its contents from the to_do_list
        print(f"You have now cleared your list.\n")

    def prioritizing(self):
        """Enables user to input which items they would prefer to prioritize over others and changes the status of the prioritized item as the output."""
        for index in range(len(self.to_do_list) - 1):
            if self.to_do_list[0]["status"] not in ("dotted", "done"): # tests if the status of the first item in the list is marked or prioritized already
                a = self.to_do_list[0]
            else:
                a = self.to_do_list[1]
            b = self.to_do_list[index + 1] 
            if b["status"] != "done" and b["status"] != "dotted": # tests if the status of the item to be asked is also markd or prioritized already
                while True: # while loop to continuously ask question until all items are gone through with a yes or no answer
                    print(f"Would you like to {b["item"]} more than {a["item"]}? [Please give an answer as 'Yes' or 'No'.]\n")
                    Prioritize_Ans = (input("> "))
                    if Prioritize_Ans != "Yes" and Prioritize_Ans != "No": # checks for invalid inputs
                        print("Answer to prioritize must be 'Yes' or 'No'. Plese write one and press enter to continue.\n")
                    else:
                        if Prioritize_Ans == "Yes": 
                            b["status"] = "dotted" # changes the asked item's status to 'dotted' if the answer is yes to prioritize this item over another
                        break

    def marking(self):
        """Enables user to mark an item in the list as done with the prior list as the input and updated list as the output."""
        print("You want to mark the prioritized item as done.")
        for item in reversed(self.to_do_list): # looks at each item but in the opposite order than given
            if item["status"] == "dotted": 
                item["status"] = "done" # changes the marking item's status to 'done' if it is currently prioritized
                for item in reversed(self.to_do_list):
                    if item["status"] == "ready":
                        item["status"] = "dotted" # this makes sure that the next item that is given in reverse order from the list is then changed to prioritized from 'ready'
                break
            else:
                for item in self.to_do_list:
                    if item["status"] == "new": # if no items are 'dotted', it will make sure to change the status of a 'new' item to a 'ready' one
                        item["status"] = "ready"
                        break
    
    def showing(self):
        """Shows the user's current to-do-list for their view."""
        if not self.to_do_list: # checks if there is nothing in the list at that moment
            print("There are no items in your list currently.")
        else:
            print("Here is your list at the moment:\n")
            for item in self.to_do_list:
                state = item["status"] # assigns the items' statuses to the variable 'state'
                if state in ("ready", "dotted"):
                    format = "[O]" # formats the item when showing it to the user to have a '[O]' when ready or dotted
                elif state == "done":
                    format = "[X]" # formats the item when showing it to the user to have a '[x]' when done
                else:
                    format = "[ ]" # formats the item when showing it to the user to have a '[ ]' when new
                print(f"{format} {item["item"]}")
    
    def checking(self):
        """Nested function that checks whether the given input is in the correct format to apply.  Only outputs if correct."""
        answer = None
        while not isinstance(answer, int): # while loop created to make sure that when wrong input is given, it doesn't continue but loops back to have an input again
            try: # try block to get correct inputs as integers in the range wanted (between 1-6)
                answer = int(input("> "))
                if (answer > 0) and (answer < 7):
                    return answer
                else: 
                    print("The number must be in the range of the numbers given from the list above.\n")
            except ValueError: # except block to print out error message so user can put in valid answer
                print("Invalid input.  Please enter a valid number according to the option numbers above.")

    def provide_input(self): 
        """Enables user to give a choice regarding what they would like to do with the program.""" 
        Choosing = True
        while Choosing: # while loop made to keep asking user for a valid choice from the option list
            print("Please select a number choice from the options and input that below.\n")
            for num in range(len(self.option_list)):
                print(f"{num + 1}:{self.option_list[num]}") # formats the option list again in the appropriate maner
            answer = self.checking() # gets the result from the checking function to use here
            if (len(self.to_do_list) == 0): # lines 118-129 do another test this time based on the length of the current input list 'to_do_list'
                if (answer > 3) and (answer < 6): # if there are no items in list and user attempts to prioritize or mark, they get message back saying not possible
                    print("You cannot prioritize or mark an empty list.  Select another option.")
                else:
                    return answer
            elif (len(self.to_do_list) == 1):
                if (answer == 4): # if there is one item list and user attempts to prioritize, they get message back saying not possible
                    print("You cannot prioritize a list with one item in it.  Select another option.")
                else:
                    return answer
            elif (len(self.to_do_list) > 1):
                return answer # all options possible with more than one item in the list
            
    def prioritize_check(self):
        """Nested function that checks whether the list items' statuses are all marked done or not.  Outputs True Boolean if they are."""
        if all(item["status"] == "done" for item in self.to_do_list): # if statement to check the statuses of all items at once
            return True

    # Main body of the code starts here.
    def run_code_bloc(self):
        """Enables the code to be combined into one runnable algorithm by taking in arguments, functions, and variables from other prior functions.  Outputs according to what is chosen."""
        self.print_welcome_statement() # calls print welcome statement function here
        print() # line for formatting space preferability
        Running = True
        while Running: # main while loop in order to continue main program unless quit
            answer1 = self.provide_input() # gets the result from the providing input function here
            if (answer1 == 1): # if block runs the quitting function if user chooses that option from list
                self.quitting()
                Running = False
            elif (answer1 == 2): # elif block runs the adding function if user chooses that option from list
                self.adding()
                print()
            elif (answer1 == 3): # elif block runs the clearing function if user chooses that option from list
                self.clearing()
            elif (answer1 == 4): # elif block runs the prioritizing function if user chooses that option from list
                if self.prioritize_check(): # only time it won't work is if prioritize checking function gives back True result from check
                    print("You cannot prioritize items that are all prioritized (No ready, dotted, or both items.)")
                else:
                    self.prioritizing()
                print()
            elif (answer1 == 5): # elif block runs the marking function if user chooses that option from list
                self.marking()
                print()
            elif (answer1 == 6): # elif block runs the showing function if user chooses that option from list
                self.showing()
                print()

Task_Wizard_Software = Program() # assigns the Class Program to the variable Task_wizard_Software
Task_Wizard_Software.run_code_bloc() # calls Program's run_code_bloc() to do start the entire program.

###########################################################################################################################################################################

# Everything below here was the final version of my try without the classes and dictionaries implemented.  
# Just for reference considering how much work was done for this.


# to_do_list = []

# option_list = ["Quit the Task Wizard Software", "Add Item to List", "Delete Your List", "Prioritize List", "Mark Ready Item as Complete", "See The List"]

# def print_welcome_statement():
#     """Prints out initial welcoming statement."""
#     print("Welcome to Alex's version of the Autofocus application called: Task Wizard.")

# def show_option_list():
#     """Shows the list of options that one can choose from like a main menu,"""
#     print("Here are the options that you can choose from.\n")
#     for num in range(len(option_list)):
#         print(f"{num + 1}:{option_list[num]}")

# def quitting():
#     """Prints out a closing statement after user quits the program."""
#     print("You are now quitting the Task Wizard Software.  We hope our application helped you manage your tasks well this time!")

# def adding():
#     """Enables user to add some input of their own to the to-do-list they are creating."""
#     print("You would like to add something to your to-do list.  What would you prefer to add?")
#     List_Item = input("> ")
#     to_do_list.append(List_Item)
#     print(f"You added '{List_Item}' to your to-do list.")
#     return to_do_list

# def clearing():
#     """Enables user to get rid of all items from their list with a fresh blank list as the output."""
#     print("You will be clearing your list.\n")
#     to_do_list.clear()
#     print(f"Your list now is: {to_do_list}\n")
#     return to_do_list

# def prioritizing(list):
#     for index in range(len(list) - 1):
#         if list[index] != list[-1]:
#             print(f"Would you like to {list[index + 1]} more than {list[index]}?")
#             Prioritize_Ans = (input("> "))
#             if Prioritize_Ans != "Yes" and Prioritize_Ans != "No":
#                 print("Answer to prioritize must be 'Yes' or 'No'.  Select the prioritization option to try again.")
#                 break
#             elif Prioritize_Ans == "Yes":
#                 list[index + 1] = "-" + list[index + 1]
#                 print(list[index + 1])
#                 print(list)
#                 return list

#     # for item in range(len(to_do_list), 0, -1):
#     #     for item in list:
#     #         if item[1] == "O":
#     #             return [O]


# # status = prioritizing(to_do_list)

# # def prioritizing2(state):
# #     for item in range(len(to_do_list), 0, -1):
# #         if 
        
# def marking(list):
#     """Enables user to mark an item in the list as done with the prior list as the input and updated list as the output."""
#     print("You want to mark the prioritized item as done.")
#     for item in range(len(list), 0, -1):
#         temp_list = [item for item in list if "-" in item]
#         if temp_list:
#             print(temp_list)
#     # Mark_Item = None
#     # while not isinstance(Mark_Item, int):
#     #     try:
#     #         Mark_Item = int(input("> "))
#     #         list_length = int(len(list)) + 1
#     #         if (Mark_Item > 0) and (Mark_Item < (list_length)):
#     #             updated_list(list, Mark_Item)
#     #             return list
#     #         else: 
#     #             print("The number must be in the range of the numbers given from the list above.\n")
#     #     except ValueError:
#     #         print("Invalid input.  Please enter a valid number according to the item numbers above.")

# def showing():
#     """Shows the user's current to-do-list for their view."""
#     print("Here is your list at the moment:\n")
#     for num in range(len(to_do_list)):
#             if num == 0:
#                 print(f"[O]:{to_do_list[num]}")
#             else:
#                 print(f"[ ]:{to_do_list[num]}")
    
#     # if prioritizing_result == "ready":
#     #     for num in prioritizing_result:
#     #         print(f"[O]:{to_do_list[num]}")

    

# def checking():
#     """Nested function that checks whether the given input is in the correct format to apply.  Only outputs if correct."""
#     answer = None
#     while not isinstance(answer, int):
#         try:
#             answer = int(input("> "))
#             if (answer > 0) and (answer < 7):
#                 return answer
#             else: 
#                 print("The number must be in the range of the numbers given from the list above.\n")
#         except ValueError:
#             print("Invalid input.  Please enter a valid number according to the item numbers above.")
    
# def provide_input(): 
#     """Enables user to give a choice regarding what they would like to do with the program.""" 
#     print("Please select a number choice from the list and input that below.\n")
#     show_option_list()
#     answer = checking()
#     Choosing = True
#     while Choosing:
#         if ((len(option_list)) > 1):
#             return answer
#         elif (len(option_list == 1)):
#             if (answer < 6):
#                 return answer
#             elif (answer < 7):
#                 print("You cannot delete one item from a list with just one in it.  Try to clear the list instead.")
#             else:
#                 print("Please choose a valid number from 1-6.  Please select from either adding an item to the list, clearing the list, checking the list, marking as complete, or quitting the program altogether.")
#         elif (len(option_list == 0)):
#             if (answer < 3):
#                 return answer
#             elif (answer < 7):
#                 print("You cannot delete from the list with no items, you cannot see a list with no items in it, you cannot mark anything as done when there is nothing, or you cannot clear an entire list with nothing to clear.")            
#             else:
#                 print("Please choose a valid number from 1-6.  Please select from either adding an item to the list or quitting the program altogether.")

# # Main body of the code starts here.
# print_welcome_statement()
# print()
# Running = True
# while Running:
#     answer1 = provide_input()
#     if (answer1 == 1):
#         quitting()
#         Running = False
#     elif (answer1 == 2):
#         adding()
#         print()
#     elif (answer1 == 3):
#         clearing()
#     elif (answer1 == 4):
#         prioritizing(to_do_list)
#         print()
#     elif (answer1 == 5):
#         marking(to_do_list)
#         print()
#     elif (answer1 == 6):
#         showing()
#         print()
    

# # when adding item, mark item as ready
# # when adding newer item, it doesnt have to be marked
# # if marking item as done, then next item underneath should be marked as ready
# # can always delete the list
# # if multiple items are ready, mark done from bottom of list first