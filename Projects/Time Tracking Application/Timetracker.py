# Time Tracking Application

import time

def start_task(tasks):
    """
    Starts a new task by adding it to the tasks dictionary with the current time as the start time.
    
    Args:
        tasks (dict): Dictionary to store the tasks
        
    Returns:
        None
    
    """"
    
    task_name = input("Enter the Task Name: ")
    if task_name in tasks:
        print("Task already exists.")
    else:
        tasks[task_name] = time.time()

        
def stop_task(tasks):
    """
    Stops a task bey calculating the time that it has been running and sorts it in the dictionary
    
    Args: tasks(dict): Dictionary containing the tasks
    
    Returns:
        None
    """
    task_name = input("Enter the Task Name: ")
    if task_name in tasks:
        if isinstance(tasks[task_name], float):     #check if task is currently running
            start_time = tasks[task_name]
            elapsed_time = time.time() - start_time
            task[task_name] = (start_time, time.time())     #Store the task as a tuple with start and end times
            print(f"Stopped Task: {task_name}")
            print(f"Elapsed time: {elapsed time:.2f} second")
        else:
            print(f"Task '{task_name}' is already stopped.")
    else:
        print(f"Task '{task_name}' not found.")
       
    
def display_task_history(tasks):
    """
    Displays the task 
    """
    
    if tasks:
        print("Task History:")
        for task_name, task_info in tasks.items():
            if isinstance(task_info, float):  # Check if task is currently running
                # -----
                # TO DO
                # -----
            else:
                # -----
                # TO DO
                # -----
    else:
        print("No tasks tracked.")

def display_total_completed_time(tasks):
    total_time = 0
    for task_info in tasks.values():
        if isinstance(task_info, tuple):  # Check if task is stopped
            # -----
            # TO DO
            # -----
    print(f"Total Completed Time: {round(total_time, 2)} seconds")

def main_menu(tasks):
    while True:
        # -----
        # TO DO
        # -----
        print()

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

def run_program():
    tasks = {}
    main_menu(tasks)

run_program()