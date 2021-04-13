
#Payusan, Justine B.
#Simple Student Information System

import csv

studAttributes = ['Name', 'ID Number', 'Year Level', 'Gender', 'Course']
studDatabase = 'StudentData.csv'

def Main():
    print("____________________________________________")
    print("    MSU-IIT STUDENT INFORMATION SYSTEM      ")
    print("____________________________________________")
    print("1. DISPLAY STUDENTS")
    print("2. ADD NEW STUDENT")
    print("3. EDIT STUDENT")
    print("4. DELETE STUDENT")
    print("5. SEARCH STUDENT")
    print("6. EXIT")
    print()
    
    
def ViewStud():
    global studAttributes 
    global studDatabase
    
    print("______________________")
    print("     STUDENT LIST     ")
    print("_____________________")
    
    with open(studDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for x in studAttributes :
            print( x, end = "\n")
        print("\n-------------------------------------------------")
        
        for row in reader:
            for item in row:
                print( item, end = "\n")
            print()        
    input("Press any key to continue:")
    

def AddStud():
    print("_____________________")
    print("    ADD STUDENT      ")
    print("_____________________")
    
    global studAttributes
    global studDatabase
    
    studData = []
    for field in studAttributes :
        value = input("Enter " + field + ": ")
        studData.append(value)
        
    with open(studDatabase, "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([studData])
    
    print("Wow! Data added successfully!")
    input("Press any key to continue:")
    return

def EditStud():
    global studAttributes 
    global studDatabase
    
    print("________________________")
    print("     UPDATE STUDENT     ")
    print("________________________")
    
    studID = input("Enter ID Number of student you want to edit: ")
    studIndex = None
    EditData = []
    with open(studDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if studID == row[1]:
                    studIndex = counter
                    print("Student Found: at index ", studIndex)
                    studData = []
                    for field in studAttributes :
                        value = input("Enter " + field + ": ")
                        studData.append(value)
                    EditData.append(studData)
                else:
                    EditData.append(row)
                counter += 1
                
# Check if the record is found or not found
    if studIndex is not None:
        with open(studDatabase, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(EditData)
    
    else:
        print("Sorry! ID Number could not be found\n")
       
    input("Press any key to continue:")
    
    
    
def DeleteStud():
    global studAttributes 
    global studDatabase
    
    print("________________________")
    print("      DELETE STUDENT    ")
    print("________________________")
    
    studID = input("Enter ID Number of student to remove: ")
    studFound = False
    EditData = []
    with open(studDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if studID != row[1]:
                    EditData.append(row)
                    counter += 1
                else:
                    StudFound = True
    
    if StudFound is True:
        with open(studDatabase, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(EditData)
        print("ID Number:\n ", studID, "Removed successfully!")
    
    else:
        print("Oops! ID Number could not be found")
    
    input("Press any key to continue:")
    
def SearchStud():
    global studAttributes 
    global studDatabase
    
    print("________________________")
    print("     SEARCH STUDENT     ")
    print("________________________")
    
    studID = input("Enter ID Number:")
    with open(studDatabase, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if studID == row[1]:
                    print("You found it!")
                    print("Name: ", row[0])
                    print("ID Number: ", row[1])
                    print("Year Level: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        
        else:
            print("Oops! This Student does not exist!")
    input("Press any key to continue:")
    

# Main
while True:
    Main()
    
    choice = input("Do you want to try?:")
    if choice == '1':
        ViewStud()
    elif choice == '2':
        AddStud()
    elif choice == '3':
        EditStud()
    elif choice == '4':
        DeleteStud()
    elif choice == '5':
        SearchStud()
    else:
        break


# Termination
print("************************************")
print("*  THE SYSTEM HAS BEEN TERMINATED  *")
print("************************************")



