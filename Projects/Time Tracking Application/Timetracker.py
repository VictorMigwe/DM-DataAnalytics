# Time Tracking Application

import time

def start_task(tasks):
    """
    Starts a new task by adding it to the tasks dictionary with the current time as the start time.
    Args:
        tasks (dict): Dictionary to store the tasks
    """"
    
    task_name = input("Enter the Task Name: ")
    
    
    
def stop_task(tasks):
    # -----
    # TO DO
    # -----

def display_task_history(tasks):
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