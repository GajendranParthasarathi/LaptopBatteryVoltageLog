import psutil
import time
from openpyxl import Workbook, load_workbook
from datetime import datetime

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

def log_battery_percentage(file_name):
    try:
        workbook = load_workbook(file_name)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Date", "Time", "Battery Percentage (%)"])
    
    while True:
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        percentage = get_battery_percentage()
        
        sheet.append([date_str, time_str, percentage])
        
        workbook.save(file_name)
        print(f"Logged at {date_str} {time_str}: {percentage}%")
        
        time.sleep(7)  # Wait for 30 seconds before logging again

if __name__ == "__main__":
    file_name = "battery_log_pg.xlsx"
