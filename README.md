Overview
The script is designed to log the battery percentage of a device into an Excel file at regular intervals. It checks the battery percentage, records the date and time of the check, and saves this information in an Excel file.

Code Explanation
Imports:

import psutil  
import time  
from openpyxl import Workbook, load_workbook  
from datetime import datetime  
psutil: Used to access battery information.
time: Provides the ability to pause execution for a specified duration between log entries.
openpyxl: Used to read from and write to Excel files.
datetime: To manage and format date and time.
Function: get_battery_percentage():

def get_battery_percentage():  
    battery = psutil.sensors_battery()  
    return battery.percent  
This function uses psutil to retrieve the current battery status and returns the battery percentage.
Function: log_battery_percentage(file_name):

def log_battery_percentage(file_name):  
    try:  
        workbook = load_workbook(file_name)  
        sheet = workbook.active  
    except FileNotFoundError:  
        workbook = Workbook()  
        sheet = workbook.active  
        sheet.append(["Date", "Time", "Battery Percentage (%)"])  
Tries to load an existing Excel file (file_name).
If the file does not exist, it creates a new Excel workbook and initializes it with headers ("Date", "Time", "Battery Percentage (%)").
Logging Loop:

while True:  
    now = datetime.now()  
    date_str = now.strftime("%Y-%m-%d")  
    time_str = now.strftime("%H:%M:%S")  
    percentage = get_battery_percentage()  
    
    sheet.append([date_str, time_str, percentage])  
    
    workbook.save(file_name)  
    print(f"Logged at {date_str} {time_str}: {percentage}%")  
    
    time.sleep(7)  # Wait for 30 seconds before logging again  
Inside an infinite loop (while True):
Gets the current date and time.
Calls get_battery_percentage() to get the current battery level.
Appends a new row with the date, time, and battery percentage to the active worksheet.
Saves the workbook to the specified Excel file.
Prints a confirmation message to the console indicating the logged time and percentage.
Then, it sleeps for 7 seconds before logging again (but based on your comments, you might have meant to pause for 30 seconds).
Main Execution Block:

if __name__ == "__main__":  
    file_name = "battery_log_pg.xlsx"  
This part of the code checks if the script is being run directly (not imported as a module). If it is, it sets the file name for the Excel file to "battery_log_pg.xlsx" but does not actually call the logging function.
How to Use the Script
To make the script functional, you need to call the log_battery_percentage(file_name) function in the if __name__ == "__main__": block. Here’s the modified section:

if __name__ == "__main__":  
    file_name = "battery_log_pg.xlsx"  
    log_battery_percentage(file_name)  # Call the logging function  
Summary
The script monitors and logs the battery percentage of a device every 7 seconds (or any desired interval) and saves the data in an Excel file, creating a new file if it doesn't already exist. This is useful for tracking battery performance over time.
