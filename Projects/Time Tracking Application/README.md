>   Name: Time Tracker
    Version: 1.0
    Author: Victor T. Migwe
    Dependencies: Python 3.6 or later
    Project Description: Time Tracking Application
    Bugs: None known at this time.
    License: This program is licensed under the MIT License.


# Time Tracking Application
The Time Tracking Application is a command-line Python program that allows users to track and manage tasks along with their elapsed times. It provides various functionalities such as;
Starting a task, stopping a task, displaying the task history, displaying the total completed time, and exporting the task history to a text file.

## Features

### Start a Task

-   Allows the user to start a new task by entering a task name.
-   Adds the task to the tasks dictionary with the current time as the start time.
-   If the task name already exists, it displays a message indicating that the task already exists.

### Stop a Task

-   Allows the user to stop a running task by entering the task name.
-   Calculates the elapsed time since the task was started.
-   Stores the task in the tasks dictionary as a tuple with the start and end times.
-   If the task name is not found or the task is already stopped, it displays an appropriate message.

### Display Task History

-   Displays the task history along with their respective elapsed times.
-   If a task is currently running, it displays "In progress" instead of the elapsed time.
-   If no tasks are tracked, it displays a message indicating that no tasks are tracked.

### Display Total Completed Time

-   Calculates and displays the total completed time across all the stopped tasks.
-   Ignores the running tasks and considers only the tasks that have been stopped.

### Export Task History

-   Allows the user to export the task history to a text file.
-   By default, the exported file is named "task\_history.txt" and has a .txt extension.
-   The user can specify a different filename during the export process.
-   The exported file includes the task history with their respective elapsed times.
-   If a task is currently running, it is indicated as "In progress" in the exported file.

### Exit the Program

-   Allows the user to exit the program gracefully.


## Time Tracking Application

The Time Tracking Application is a simple command-line program that allows users to track the duration of tasks. It provides features to start and stop tasks, display task history, calculate total completed time, and export task history to a file.

### Features

1.  `Start a Task:`
Users can start a new task by providing a task name. The application records the start time of the task.
    
2.  `Stop a Task:`
Users can stop an ongoing task by providing the task name. The application calculates the elapsed time since the task started and records the start and end times of the task.
    
3.  `Display Task History:`
Users can view the history of all completed tasks along with their respective elapsed times.
    
4.  `Display Total Completed Time:`
Users can see the total completed time across all tasks.
    
5.  `Export Task History:`
Users can export the task history to a file for record-keeping or further analysis.
    
6.  `Exit the Program:`
Users can exit the application.
