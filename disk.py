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

#*function to display disk props
def Display_DISK_Info():
    table = Table(title="Detailed Disk Information")
    table.add_column("Metric", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    # Disk-related metrics
    disk = psutil.disk_usage('/')
    table.add_row("Total Disk Space", f"{disk.total / (1024**3):.2f} GB")
    table.add_row("Used Disk Space", f"{disk.used / (1024**3):.2f} GB")
    table.add_row("Free Disk Space", f"{disk.free / (1024**3):.2f} GB")
    table.add_row("Disk Usage", f"{disk.percent}%")

    # Optionally, show partition info
    table_partitions = Table(title="Disk Partitions")
    table_partitions.add_column("Partition", style="cyan")
    table_partitions.add_column("Mount Point", style="magenta")
    table_partitions.add_column("File System", style="green")

    for partition in psutil.disk_partitions():
        table_partitions.add_row(partition.device, partition.mountpoint, partition.fstype)

    
    console.print(table)
    console.print(table_partitions)

    while True:
        user_input = input("\nType 'q' to go back: ")
        if user_input.lower() == 'q':
           print("\nExiting...\n")
           break
        else:
           print("Invalid input. Please type 'q' to return.")
