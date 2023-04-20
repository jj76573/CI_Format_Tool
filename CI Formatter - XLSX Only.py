import csv
import openpyxl
import os

# Prompt user for the input file name
input_file = input("Enter your filename: ")

# Add .xlsx extension if missing
if not input_file.endswith('.xlsx'):
    input_file += '.xlsx'

# Check if the input file exists
if os.path.exists(input_file):
    # Open the Excel file and read the values in the first two columns (DB values USERID and USERNAME)
    workbook = openpyxl.load_workbook(input_file)
    sheet = workbook.active
    user_ids = [cell.value for cell in sheet['A']]
    usernames = [cell.value for cell in sheet['B']]
    # combine userID and username
    user_data = list(zip(user_ids, usernames))

# set the default values
password = ''
active = '1'
role = ''
change_pw = '1'
dispense_count = ''
dispense_amount = ''
till_list = ''
delete_flag = '0'


# set the values based on user input
password = input("Enter the password (leave blank for no change): ")
# Active status
active = input("User inactive? (0 for inactive, blank for active): ")
if active == '':
    active = '1'
# Role code
role = input("Please enter the User Role code: ")
# Change password flag
change_pw = input("Enter 1 to require password change or 0 to not require change (leave blank for no change): ")
if change_pw == '':
    change_pw = '1'
# Dispense count
dispense_count = input("Enter the maximum daily dispense count (leave blank for no change): ")
# Dispense amount
dispense_amount = input("Enter the maximum daily dispense amount (e.g. 1300 for $1300) (leave blank for no change): ")
# till list
till_list = input("Enter the till IDs separated by commas (leave blank for no change): ")
# Delete flag
delete_flag = input("Enter 1 to delete the user (leave blank for no change): ")
if delete_flag == '':
    delete_flag = '0'

# initialize the data list outside of the for loop
data = []

# loop through the user data and create a row for each user
for user_id, username in user_data:
    # create a list with the default values
    row_data = [user_id, username, role, password, '', active, change_pw, dispense_count, dispense_amount, till_list, delete_flag, '', '']

    # append the row data to the data list
    data.append(row_data)
    
# initialize the data list outside of the for loop
data = []

# loop through the user data and create a row for each user
for user_id, username in user_data:
    # create a list with the default values
    row_data = [user_id, username, role, password, '', active, change_pw, dispense_count, dispense_amount, till_list, delete_flag, '', '']
    # append the row data to the data list if it's not empty
    if not all(val == '' for val in row_data):
        data.append(row_data)

# write the modified data list to a new csv file with _parsed in the filename and utf-8 encoding
output_filename = input("Enter the name of the output file: ")
with open(output_filename + '_parsed.csv', 'w', encoding='utf-8', newline='') as modified_csv_file:
    writer = csv.writer(modified_csv_file, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
