"""
Task manager class that handles all functionality necessary to use the manager.

"""

import csv
from tasks import Task
from datetime import datetime as dt

class TaskManager:
    # Constructor function that initializes the manager as an empty list
    def __init__(self):
        self.tasks = []


    # load function that checks if csv file with tasks exists. If so, the tasks are appended to the empty list for further usage
    def load_from_csv(self):
        try:
            # open csv file if existing in reading mode
            with open("to_do_list.csv", "r", newline="") as csvfile:
                # read into dictionary
                reader = csv.DictReader(csvfile)
                for row in reader:                    
                    # append single tasks into list
                    self.tasks.append(Task(row["taskid"], row["date"], row["starttime"], row["endtime"], row["content"], row["status"]))        
        # if no file exists, ignore this function
        except FileNotFoundError:
            pass

    # save function that creates new csv file containing all tasks in the list
    def save_to_csv(self):
        # open new csv in writing mode
        with open("to_do_list.csv", "w", newline="") as csvfile:
            # define keys for file
            fieldnames = ["taskid", "date", "starttime", "endtime", "content", "status"]
            taskwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")            
            taskwriter.writeheader()
            # write entry for each task in list
            for task in self.tasks:                
                taskwriter.writerow({"taskid": task.task_id, "date": task.date.strftime("%d/%m/%Y"), "starttime": task.starttime.strftime("%H:%M"), "endtime": task.endtime.strftime("%H:%M"), "content": task.content, "status": task.status})  

    # add function that takes task_tuple from get_user_input() function, transforms it into Task object and saves it to file
    def add_task(self, task_tuple):        
        # unpack task_tuple from get_user_input() function into variables necessary to create Task object
        date, starttime, endtime, content, status = task_tuple
        
        # task_id is set either 1, if no task exists yet, or to the highest ID + 1
        task_id = max(task.task_id for task in self.tasks) + 1 if self.tasks else 1                          
                
        # create Task object from tuple, store it in self.tasks, and sort tasks
        task = Task(task_id, date, starttime, endtime, content, status)
        self.tasks.append(task)
        self.sort_tasks()

        # save task to csv and return task
        self.save_to_csv()
        print("Task was successfully added.\n")       
        return task    
    
    
    # sort function that makes sure tasks in file are in correct order
    def sort_tasks(self):
        # tasks should be sorted by date and also time (if there are more than 1 tasks in one day)
        self.tasks = sorted(self.tasks, key=lambda task: (task.date, task.starttime))

    # function to adjust the task status from pending to done or the other way around. Takes task_id as input.
    def mark_status(self, task_id):
        # if the task_id corresponds to a actual task within the list, change the status
        if any(task.task_id == task_id for task in self.tasks):
            # check for specific task
            for task in self.tasks:
                # if this task is actually the entered ID, change status and save to file
                if task.task_id == task_id:
                    task.status = not task.status
                    self.save_to_csv()
                    print("Task status was successfully changed.\n")
                    break
        # if task_id does not exist, print statement
        else:
            print("\nTask not found")
        


        
    # remove function that let's the user enter a task_id to remove
    def remove_task(self, task_id):
        # if the ID corresponds to task in list, remove 
        if any(task.task_id == task_id for task in self.tasks):
            self.tasks = [task for task in self.tasks if task.task_id != task_id]
            self.save_to_csv()
            print("Task was successfully removed.\n")
        # if id not in list, print statement
        else:
            print("\nTask not found")