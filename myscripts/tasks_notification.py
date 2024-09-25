import csv
from datetime import datetime
from plyer import notification
import schedule
import time

# Function to show notification (used for both tasks and errors)
def notify(message, title="Task Reminder"):
    notification.notify(
        title=title,
        message=message,
        app_name="Task Scheduler",
        timeout=10
    )

# Function to read tasks from CSV with semicolon as the delimiter and UTF-8-SIG encoding to handle BOM
def read_tasks(csv_file):
    tasks = {}
    try:
        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                time_column = row.get('Time', '').strip()
                task_column = row.get('Task', '').strip()
                if time_column and task_column:
                    tasks[time_column] = task_column
                else:
                    notify(f"Error: Missing 'Time' or 'Task' in row: {row}", title="CSV Error")
    except UnicodeDecodeError as e:
        notify(f"Error reading CSV file: {e}", title="File Error")
    return tasks

# Schedule notifications for tasks
def schedule_tasks(tasks):
    current_time = datetime.now().strftime("%H:%M")
    
    for task_time, task_description in tasks.items():
        # Schedule task if its time hasn't passed yet
        if task_time >= current_time:
            schedule.every().day.at(task_time).do(notify, task_description)

# Function to notify that the script has started
def notify_startup():
    notify("The task scheduler has started running.", title="Task Scheduler")

# Path to your tasks CSV file
csv_file = r"C:\Users\leopoldo.costa\OneDrive\Tasks.csv"

if __name__ == "__main__":
    # Notify that the script has started
    notify_startup()

    # Load tasks from CSV
    tasks = read_tasks(csv_file)
    
    # Schedule all tasks
    schedule_tasks(tasks)
    
    # Run the scheduled tasks
    while True:
        schedule.run_pending()  # Run any scheduled tasks
        time.sleep(1)  # Minimal delay to prevent CPU overutilization
