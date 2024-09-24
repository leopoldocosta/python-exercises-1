import csv
from datetime import datetime, timedelta
import sched
import time
from win10toast import ToastNotifier
import winsound

# Function to read tasks from CSV with semicolon as the delimiter and UTF-8-SIG encoding to handle BOM
def read_tasks(csv_file):
    tasks = {}
    try:
        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # Use delimiter=';'
            for row in reader:
                time_column = row.get('Time', '').strip()  # Strip leading/trailing spaces
                task_column = row.get('Task', '').strip()  # Strip leading/trailing spaces
                if time_column and task_column:
                    tasks[time_column] = task_column
    except UnicodeDecodeError as e:
        print(f"Error reading CSV file due to encoding issue: {e}")
    return tasks

# Function to show notification
def notify(task):
    toaster = ToastNotifier()
    toaster.show_toast("Task Reminder", f"Next task: {task}", duration=10, threaded=True)
    winsound.MessageBeep()

# Function to notify script start
def notify_start():
    toaster = ToastNotifier()
    toaster.show_toast("Task Scheduler", "The task scheduler has started.", duration=5, threaded=True)
    winsound.MessageBeep()

# Scheduler function that checks tasks and orchestrates notifications
def schedule_next_task(scheduler, tasks):
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time in tasks:
        notify(tasks[current_time])

    # Schedule next task check for the next minute
    next_check = now + timedelta(minutes=1)
    delay = (next_check - datetime.now()).total_seconds()
    scheduler.enter(delay, 1, schedule_next_task, (scheduler, tasks))

# Main function to embark on the task scheduling
def task_scheduler(csv_file):
    tasks = read_tasks(csv_file)  # Read tasks from CSV
    notify_start()  # Notify that the script has started

    # Create a scheduler to manage task notifications dynamically
    scheduler = sched.scheduler(time.time, time.sleep)
    
    # Schedule the first check
    scheduler.enter(0, 1, schedule_next_task, (scheduler, tasks))
    
    # Start the scheduler
    scheduler.run()

# Path to your tasks CSV file
csv_file = r"C:\Users\leopoldo.costa\OneDrive\Tasks.csv"

# Start the scheduler
if __name__ == "__main__":
    task_scheduler(csv_file)
