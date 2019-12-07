# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KMueller,12.5.2019,Added code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__=="__main__":

    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Data #
lstEmpTable = []
lstFileData = []

# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmpTable.append(Emp(row[0], row[1], row[2].strip()))

# Show user a menu of options

while True:
    Eio.print_menu_items()
# Get user's menu option choice
    strOption = Eio.input_menu_options()
    if strOption == "1":
    # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstEmpTable)
        continue
    elif strOption == "2":
    # Let user add data to the list of employee objects
        lstEmpTable.append(Eio.input_employee_data())
        continue
    if strOption == "3":
    # let user save current data to file
        Fp.save_data_to_file("EmployeeData.txt", lstEmpTable)
        continue
    elif strOption == "4":
    # Let user exit program
        print("****** You have exited the program ******")
        break
# Main Body of Script  ---------------------------------------------------- #