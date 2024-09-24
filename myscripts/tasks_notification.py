import csv
import time
from datetime import datetime
from win10toast import ToastNotifier
import winsound

# Function to read tasks from CSV
def read_tasks(csv_file):
    tasks = {}
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks[row['Time']] = row['Task']
    return tasks

# Function to show notification
def notify(task):
    # Windows notification
    toaster = ToastNotifier()
    toaster.show_toast("Task Reminder", f"Next task: {task}", duration=10, threaded=True)

    # Play Windows sound (Beep sound)
    winsound.MessageBeep()

# Main function to track time and notify
def task_scheduler(csv_file):
    tasks = read_tasks(csv_file)
    while True:
        # Get current time in HH:MM format
        current_time = datetime.now().strftime("%H:%M")

        # If a task matches the current time, notify
        if current_time in tasks:
            notify(tasks[current_time])
        
        # Wait for 15 minutes before checking again
        time.sleep(900)  # 15 minutes = 900 seconds

# Path to your tasks CSV file
csv_file = r"C:\Users\leopoldo.costa\OneDrive\Tasks.csv"

# Start the scheduler
if __name__ == "__main__":
    task_scheduler(csv_file)