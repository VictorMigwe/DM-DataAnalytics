# Time Tracking Application

import time

def start_task(tasks):
    """
    This function Starts a new task by adding it to the tasks dictionary with the current time as the start time.
    
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
    This function Stops a task bey calculating the time that it has been running and sorts it in the dictionary
    
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
    This function Displays the task history with their time taken.
    
    Args:
        tasks (dict): Dictionary containing the tasks
    
    Returns:
        None
    """
    if tasks:
        print("Task History:")
        for task_name, task_info in tasks.items():
            if isinstance(task_info, float):  # Check if task is currently running
                print(f"- {task_name}: In progress")
            else:
                start_time, end_time = task_info
                elapsed time = endtime - start_time
                print(f"- {task_name}: {elapsed_time:.2f} seconds")
    else:
        print("No tasks tracked.")

def display_total_completed_time(tasks):
    """
    This function Displays the total elapsed time across all tasks.
    
    Args:
        tasks (dict): Dictionary containing the tasks
    
    Returns:
        None    
    """
    
    total_time = 0
    for task_info in tasks.values():
        if isinstance(task_info, tuple):  # Check if task is stopped
            start_time, end_time = task_info
            elapsed_time = end_time - start_time
            total_time += elapsed_time
            
    print(f"Total Completed Time: {round(total_time, 2)} seconds")

def export_task_history
    """
    This function exports the task history to a file.
    
    Args:
        tasks (dict): Dictionary containign the tasks
        filename (str): The name of the file to export the task history.
        
    Returns:
        None    
    """
    with open(filename, 'w') as file:
        file.write("Task History: \n")
        for task_name, task_info in task.items():
            if isinstance(task_info, float):    #Check if task is currently running
                file.write(f"- {task_name} In progress \n")
            else:
                start_time, end_time = task_info
                elapsed_time = end_time - start_time
                file.write (f"= {task_name}: {elapsed_time: .2f} seconds \n)
        print(f"Task history exported to '{file_name}'.")
                
    
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