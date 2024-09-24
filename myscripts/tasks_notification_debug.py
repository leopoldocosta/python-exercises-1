import csv
from datetime import datetime
from plyer import notification
import schedule
import time

# Function to read tasks from CSV with semicolon as the delimiter and UTF-8-SIG encoding to handle BOM
def read_tasks(csv_file):
    tasks = {}
    try:
        # Open the CSV file with utf-8-sig encoding to handle the BOM character
        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # Use delimiter=';'
            
            # Print the actual fieldnames (headers) from the CSV for debugging
            print(f"CSV Headers: {reader.fieldnames}")
            
            for row in reader:
                time_column = row.get('Time', '').strip()  # Strip leading/trailing spaces
                task_column = row.get('Task', '').strip()  # Strip leading/trailing spaces
                if time_column and task_column:
                    tasks[time_column] = task_column
                else:
                    print(f"Error: Missing 'Time' or 'Task' in row: {row}")
    except UnicodeDecodeError as e:
        print(f"Error reading CSV file due to encoding issue: {e}")
    return tasks

# Function to show notification
def notify(task):
    notification.notify(
        title="Task Reminder",
        message=f"Next task: {task}",
        app_name="Task Scheduler",
        timeout=10
    )
    print(f"Notification Sent: {task}")  # Debugging print

# Schedule notifications for tasks
def schedule_tasks(tasks):
    current_time = datetime.now().strftime("%H:%M")
    
    for task_time, task_description in tasks.items():
        # Schedule task if its time hasn't passed yet
        if task_time >= current_time:
            schedule.every().day.at(task_time).do(notify, task_description)
            print(f"Task scheduled for {task_time}: {task_description}")

# Function to notify that the script has started
def notify_startup():
    notification.notify(
        title="Task Scheduler",
        message="The task scheduler has started running.",
        app_name="Task Scheduler",
        timeout=10
    )
    print("Startup notification sent.")  # Debugging print

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