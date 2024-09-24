import csv
import time
from datetime import datetime
from win10toast import ToastNotifier
import winsound

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
                # Make sure 'Time' and 'Task' columns exist in the row
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