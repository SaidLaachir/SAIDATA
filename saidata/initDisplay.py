import psutil
import os
import time
import argparse

#import sys

from rich.console import Console
from rich.table import Table

#? Lets initialise the console
console = Console()

#* function that displays main system info
def Display_Initial_Data():

    #todo Now we create a table to isplay these information inside
    table = Table(title="System Resources Usage")
    
    #?Make the column names
    table.add_column("Resource", justify="right", style="cyan", no_wrap=True)
    table.add_column("Usage", style="magenta")
    table.add_column("Name", style="green")

    #? Now gathering system information
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    diskUsage = psutil.disk_usage('/')

    #* this after finnishing with the initial table
    """process = sorted(psutil.process_iter(['cpu_percent', 'memory', 'name']), key=lambda p:p.info['cpu_percent'], reverse=True)
    top_process = process[:5]"""

    #?Display the rows of the table
    table.add_row("CPU Usage", f"{cpu_percent}%", "")
    table.add_row("Memory Usage", f"{memory.percent}%", "")
    table.add_row("Disk Usage",f"{diskUsage.percent}%", "")


    #!processes part display
    #?add the process in the array top_process
    top_process = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            process_info = proc.info
            top_process.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    #?sort the process in a descending way
    top_process = sorted(top_process, key=lambda p: p['cpu_percent'], reverse=True)

    table.add_row("Top 5 processes", "", "")
    for process in top_process[:5]:
        table.add_row("", "", process['name'])

        
    #todo print the table components : CPU RAM DISK
    #todo also the 5 top proceses. 
    console.print(table)
    
