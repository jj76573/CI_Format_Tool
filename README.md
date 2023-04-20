# CI_Format_Tool
Python Script to automate mass user imports to the CI Server

# Prerequisites
Python 3.6 or above
Add Python to PATH
openpyxl module

# Installation
Save the .txt files as .py.
Install openpyxl module: pip install openpyxl.

# Usage
Open Command Prompt or PowerShell as an administrator.
Change directory to the folder containing the script: cd <directory_path>.
Run the script: python '<script_name>.py'.

# Scripts

# 1. CI Formatter - Only XLSX.py

Use this script if you are creating new accounts or deleting/deactivating old ones. It is more suitable if you do not need to retain specific information from a current import list. The script references an .xlsx file containing only the columns UserID and UserName.
```
Example:

   A	        B

jj76573	Jaiden Johnson
```
You will be prompted to enter values for each field, which will apply to all users in the list. 
The script creates 13 columns and formats them in UTF-8 .csv format.

# 2. CI Formatter - CSV and XLSX.py
Use this script if you want to reference a .csv file exported from the server against an .xlsx file. 
This is useful if you have already pulled an export from the server and want to narrow the list by referencing an .xlsx file. 
The .xlsx file should only contain the columns UserID and UserName.
```
Example:

  A	        B

jj76573	Jaiden Johnson
```
Again, you will be prompted to enter values for each field. These values will apply to all users in the list. The script creates 13 columns and formats them in UTF-8 .csv format.

Before:
jj76573,Jaiden Johnson,10,,2/16/2023 10:20,1,0,3,,,0

After:
"jj76573","Jaiden Johnson","10","Password","","1","1","5","","1,10,TIPVALET","0","",""

# Example of steps:
```
1. python 'CI Formatter - CSV and XLSX Reference.py'
2. Enter your csv file name: Testing
3 .Enter your xlsx file name: Copy of reference list
4. Enter the password (leave blank for no change): Password
5. User inactive? (0 for inactive, blank for active):
6. Please enter the User Role code: 10
7. Enter 1 to require password change or 0 to not require change (leave blank for no change): 1
8. Enter the maximum daily dispense count (leave blank for no change): 5
9. Enter the maximum daily dispense amount (e.g. 1300 for $1300) (leave blank for no change):
10. Enter the till IDs separated by commas (leave blank for no change): 1,10,TIPVALET
11. Enter 1 to delete the user (leave blank for no change):
12. Enter the name of the output file: Testing_Parsed
```
