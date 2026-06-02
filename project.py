"""
This is my final project for CS50's Introduction to Programming with Python course from HarvardX.

My goal was to implement a simple CLI - Task Manager that let's a user access the program and perform a few functionalities.

By running this program a user can:

    - Add tasks with date, start and end time, and content. Each task get a unique ID and a status (default is "pending")
    - Mark the status of the task as "done"
    - Remove tasks
    - Exit the program

In order to have a permanent memory for the manager, tasks get saved to a CSV file, which is checked and updated everytime an action is
performed by the user.

The content of the CSV file gets displayed for the user to have access to the IDs in order to know which tasks to modify.

"""


# Import the necessary modules for the program to run
import sys
from datetime import datetime as dt
from tabulate import tabulate
from task_manager import TaskManager


# Main function that runs the program
def main():
    # create a TaskManager instance and load data from CSV (if it exists)
    manager = TaskManager()
    manager.load_from_csv()

    # let's the user interact with the Task Manager
    user_activity(manager)


def get_user_input():
    """
    This function prompts the user for input inside the CLI.

    Input collected:
        - date:         date in "%d/%m/%Y" format
        - start time:   time in "%H:%M" format
        - end time:     time in "%H:%M" format
        - content:      string
        - status:       set to Fasle (default value meaning the task is pending)

    Returns:
        - task:         tuple which is passed on to add_task function in the TaskManager class    
    
    """ 

    # start loop to get date in correct format
    while True:        
        date = input("Date: ")
        try:
            # if correct format continue to start time
            date = dt.strptime(date, "%d/%m/%Y")            
            break
        except ValueError:
            # reminder if wrong date format is used
            print("Please enter date as: DD/MM/YYYY")
            continue
    
    # start loop to get start time in correct format
    while True:
        starttime = input("Start: ")
        try:
            # if correct format continue to end time
            starttime = dt.strptime(starttime, "%H:%M")
            break
        except ValueError:
            # reminder if wrong time format is used
            print("Please enter time as HH:MM")
            continue
    
    # start loop to get end time in correct format
    while True:
        endtime = input("End: ")
        try:
            # if correct format continue to content
            endtime = dt.strptime(endtime, "%H:%M")
            break
        except ValueError:
            # reminder if wrong time format is used
            print("Please enter time as HH:MM")
            continue

    # user enters content as string
    content = input("TO-DO: ")
    # status id set to default 
    status = False
    # store input as tuple and return it
    task_tuple = (date, starttime, endtime, content, status)
    return task_tuple



def display_tasks(manager):
    """
    Function that displays the manager content for interaction.

    :param: manager: list of tasks

    """
    # if tasks exist, store them in a table for display
    if manager.tasks:
        table = []            
        for task in manager.tasks:
            table.append({
                "ID": task.task_id,
                "Date": task.date.strftime("%d/%m/%Y"),
                "Start": task.starttime.strftime("%H:%M"),
                "End": task.endtime.strftime("%H:%M"),
                "Activity": task.content.capitalize(),
                "Status": "✅" if task.status else "⏳"
            })

        # print the table with tasks to terminal for user to see
        print(tabulate(table, headers="keys", tablefmt="grid"))
    
    # display print statement if no tasks exist yet
    else:
        print("\nNo tasks yet.")


def user_activity(manager):
    """
    Loop that let's user interact with Task Manager content.

    Calls the display_tasks function to show content.

    Gives user 4 options to choose from and interact with manager.
    Depending on the action, different functions are called.
    
    """

    # start interaction loop until user exits program
    while True:        
        try:
            # print empty line for better visibility
            print("")
            # display table containing tasks
            display_tasks(manager)
            # display options for interaction
            print("\nExit = 0\nAdd task = 1\nMark status = 2\nRemove task = 3")
            # prompt user for number of action to perform
            action = int(input("\nEnter action: "))
            # entering "0" exits the program
            if action == 0:
                sys.exit("See you next time!\n")
            # entering "1" prompts user for input by calling get_user_input function         
            elif action == 1:        
                new_task = get_user_input()
                # add input to Task Manager by calling add_task from TaskManager class
                manager.add_task(new_task)                
            # entering "2" lets the user change the status of a task form "pending" to "done" or form "done" to "pending"
            elif action == 2:
                mark = int(input("Task to mark: "))
                # change task status by calling mark_status function from TaskManager class
                manager.mark_status(mark)                                
            # entering "3" lets user remove a task from the manager
            elif action == 3:
                rem = int(input("Task to remove: "))
                # remove task by calling remove_task from TaskManager class
                manager.remove_task(rem)                                
            else:
                raise ValueError

        # if wrong number or input, reprompt user
        except ValueError:
            print("Select action to perform.\n")


if __name__ == "__main__":
    main()