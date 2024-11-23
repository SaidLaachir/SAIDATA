# __init__.py

from .cpu import Display_CPU_Info
from .ram import Display_RAM_Info
from .disk import Display_DISK_Info
from .processes import Display_PROC_Info
from .initDisplay import Display_Initial_Data

# saidata/__init__.py
__all__ = ['saidata', 'initDisplay', 'cpu', 'ram', 'disk', 'processes']
