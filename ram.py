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

#*function to display ram props
def Display_RAM_Info():
    def generate_RAM_Table():

        
        table = Table(title="Detailed RAM Information")
        table.add_column("Metric", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        # RAM-related metrics
        memory = psutil.virtual_memory()

        table.add_row("Total RAM", f"{memory.total / (1024**3):.2f} GB")
        table.add_row("Available RAM", f"{memory.available / (1024**3):.2f} GB")
        table.add_row("Used RAM", f"{memory.used / (1024**3):.2f} GB")
        table.add_row("Free RAM", f"{memory.free / (1024**3):.2f} GB")
        table.add_row("Active RAM", f"{memory.active / (1024**3):.2f} GB")
        table.add_row("Inactive RAM", f"{memory.inactive / (1024**3):.2f} GB")
        table.add_row("Buffers", f"{memory.buffers / (1024**3):.2f} GB")
        table.add_row("Cached", f"{memory.cached / (1024**3):.2f} GB")
        table.add_row("Shared Memory", f"{memory.shared / (1024**3):.2f} GB")
        table.add_row("Swap Usage", f"{memory.percent}%")
        return table
    
    """with Live(console = console, refresh_per_second=1) as live:
    
        table = generate_RAM_Table()
        live.update(table)
        #console.print(table)
        time.sleep(1.5)
    """
    #?Display the table
    while True:           
        table = generate_RAM_Table()
        console.print(table)
        time.sleep(1.5)  # Add a small delay to reduce CPU load

        #! Check for 'q' keypress to exit
        user_input = input("\nTo come back to SAIDTA Menu press 'q': ")
        if user_input == 'q':
            print("\nExiting...\n")
            break
        else:
            console.print("Error. Invalid command, try to type 'q' to exit... ")


