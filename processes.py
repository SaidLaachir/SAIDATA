import psutil
import os
import time
import argparse

#import sys

from rich.console import Console
from rich.live import Live
from rich.table import Table

#? Lets initialise the console
console = Console()

#* Function to display all the proceses whome are 
#* orderd in a descending way based on their CPU COnsumption
def Display_PROC_Info():
    def generate_PROC_Table():
        #os.system('clear' if os.name == 'posix' else 'cls')
        # Create a table to display detailed process information
        table = Table(title="All Processes (Sorted Dicreasely by CPU Usage)")
        
        # Add columns for detailed process information
        table.add_column("PID", justify="right", style="cyan", no_wrap=True)
        table.add_column("PPID", justify="right", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("CPU (%)", justify="right", style="yellow")
        table.add_column("Memory (%)", justify="right", style="green")
        table.add_column("Threads", justify="right", style="blue")
        table.add_column("Status", style="red")
        table.add_column("Priority",  justify="right", style="white")

        # Gather all processes with relevant attributes
        process_list = []
        for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'memory_percent', 'num_threads', 'status']):
            try:
                # Add process info to the list
                process_info = proc.info
                process_info['priority'] = proc.nice()
                process_list.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        # Sort processes by CPU percentage in descending order
        sorted_processes = sorted(process_list, key=lambda p: p['cpu_percent'], reverse=True)

        # Add rows to the table
        for proc in sorted_processes:
            table.add_row(
                str(proc['pid']),            # PID
                str(proc['ppid']),           # PPID
                proc['name'],                # Name
                f"{proc['cpu_percent']:.2f}",# CPU Usage (%)
                f"{proc['memory_percent']:.2f}", # Memory Usage (%)
                str(proc['num_threads']),    # Thread Count
                proc['status'],              # Status
                str(proc['priority'])        # Priority
            )
        return table
    
    """with Live(console=console, refresh_per_second=1) as live:
        table = generate_PROC_Table()
        live.update(table)
            """
    #?Display the table
    while True:
        table = generate_PROC_Table()
        console.print(table)
        time.sleep(1)      #Pause for a second before refreshing

        user_input = input("\nTo come back to SAIDTA Menu press 'q': ")
        if user_input == 'q':
            print("\nExiting...\n")
            break
        else:
            console.print("Error. Invalid command, try to type 'q' to exit... ")

