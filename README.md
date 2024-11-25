# SAIDATA

**SAIDATA** is a simple Python-based system monitoring tool that displays real-time information about your computer's CPU, RAM, Disk, and running processes. It's designed to be user-friendly and interactive, allowing you to easily check the health and performance of your system.

## Installation

To install **SAIDATA**, follow these steps:

### 1. Clone the repository:
   If you have `git` installed, you can clone the repository:
 
   git clone https://github.com/SaidLaachir/SAIDATA.git
   


### 2. create a virtual environment:
    Try to type : 

    python3 -m vev myenv_new

    Then to activate it :

    source ~/myenv_new/bin/activate

### 3. Install the dependencies:
    You can install the required dependencies using pip. Run:

    cd SAIDATA

    pip install -r requirements.txt 

    But if it didnt work try:

    pip install rich psutil setuptools

### 3. Install the package:
    Once the dependencies are installed, you can install the SAIDATA package itself:

    pip install .

### Usage
    After installation, you can run SAIDATA directly from your terminal. Simply type:

    saidata

    If it didnt work from the first time you can run this command in SAIDATA repository:

        python
        
        from saidata.saidata import main

        main()
        
        exit()

        then go bck to the hom edirectory by typing :
        
        cd ~

        Then type the command: 
        
        saidata
