from saidata.initDisplay import Display_Initial_Data
from saidata.cpu import Display_CPU_Info
from saidata.ram import Display_RAM_Info
from saidata.disk import Display_DISK_Info
from saidata.processes import Display_PROC_Info

def main():
    #? Displaying a welcome message:
    print("\nWelcome to the SAIDATA program!")
    print("This tool displays essential system resource usage information.\n")
    print("Available commands:")
    print("  SAIDATA.CPU.all  - Show detailed real-time information about CPU")
    print("  SAIDATA.RAM.all  - Show detailed real-time information about RAM")
    print("  SAIDATA.DISK.all - Show detailed real-time information about Disk Usage")
    print("  SAIDATA.PROC.all - Show detailed real-time information about Heavy Processes")
    print("  SAIDATA.help     - Show detailed descriptions about the available commands in SAIDATA.")

    print("  exit             - Exit the program\n")   

    #* Displaying initial data
    Display_Initial_Data()

    #* CREATANG AN INTERRACTIVE PROMPT LINE
    while True:
        #! Display a prompt nd get the user input
        user_input = input("\nSAIDATA> ").strip()

         #*Exit command
        if user_input.lower() == "exit":
            print("\nExit SAIDATA. See you :)\n")
            break
        elif user_input == "SAIDATA.CPU.all":
            Display_CPU_Info()
        elif user_input == "SAIDATA.RAM.all":
            Display_RAM_Info()
        elif user_input == "SAIDATA.DISK.all":
            Display_DISK_Info()
        elif user_input == "SAIDATA.PROC.all":
            Display_PROC_Info()
        elif user_input == "SAIDATA.help":
            print("\nAvailable commands:")
            print("  SAIDATA.CPU.all  - Show detailed real-time information about CPU")
            print("  SAIDATA.RAM.all  - Show detailed real-time information about RAM")
            print("  SAIDATA.DISK.all - Show detailed real-time information about Disk Usage")
            print("  SAIDATA.help     - Display information about all the commands.\n")
            print("  SAIDATA.PROC.all - Show detailed real-time information about Heavy Processes")
            print("  exit             - Exit the program\n")
            
        elif user_input == "":
            print("The prompt was empty please enter a command that is valid.")
        else:
            print("\nInvalid command. Please enter a valid command.\n")
            
if __name__ == "__main__":
    main()
