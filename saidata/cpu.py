import psutil
import time
import curses

from rich.console import Console
from rich.live import Live
from rich.table import Table

#?initiate the console
console = Console()

def generate_CPU_Table():
    # Create a table to display detailed CPU information
    table = Table(title="Detailed CPU Information")
    table.add_column("Metric", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    # CPU-related metrics
    cpu_percent = psutil.cpu_percent(interval=1)  # Current CPU utilization
    cpu_times = psutil.cpu_times()  # Detailed time usage of the CPU
    cpu_freq = psutil.cpu_freq()  # CPU frequency details
    cpu_cores = psutil.cpu_count(logical=True)  # Logical cores count
    physical_cores = psutil.cpu_count(logical=False)  # Physical cores count

    # Add rows with detailed CPU information
    table.add_row("CPU Usage", f"{cpu_percent}%")
    table.add_row("CPU Frequency (Current)", f"{cpu_freq.current:.2f} MHz")
    table.add_row("CPU Frequency (Max)", f"{cpu_freq.max:.2f} MHz")
    table.add_row("Logical Cores", str(cpu_cores))
    table.add_row("Physical Cores", str(physical_cores))
    table.add_row("User Time", f"{cpu_times.user:.2f} seconds")
    table.add_row("System Time", f"{cpu_times.system:.2f} seconds")
    table.add_row("Idle Time", f"{cpu_times.idle:.2f} seconds")

    # If available, display additional times (like iowait, etc.)
    if hasattr(cpu_times, 'iowait'):
        table.add_row("IO Wait Time", f"{cpu_times.iowait:.2f} seconds")
    if hasattr(cpu_times, 'steal'):
        table.add_row("Steal Time", f"{cpu_times.steal:.2f} seconds")

    return table

#*function to display cpu props
def Display_CPU_Info():    
    #todo:  Generate and display the CPU table
    """with Live(console=console, refresh_per_second=1) as live:
        while True:    
        
                live.update(generate_CPU_Table())"""
    while True:
            
        table = generate_CPU_Table()
        console.print(table) 
        time.sleep(0.1)  # Add a small delay to reduce CPU load

        user_input = input("\nTo come back to SAIDTA Menu press 'q': ")
        if user_input == 'q':
            print("\nExiting...\n")
            break
        else:
            console.print("Error. Invalid command, try to type 'q' to exit... ")

#? initialaise the cursor and start the function
#Display_CPU_Info()

  