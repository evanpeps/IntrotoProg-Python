# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   EPeper,11/11/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = '' # Holds data contained in JSON file
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {str, str}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of dictionaries (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    for item in students:
        file.close()
except FileNotFoundError as e:
    print("File not found. Creating...")
    open(FILE_NAME, 'w')
except Exception as e:
    print('Unknown exception. Resetting roster...')
    students = []
    print(type(e), e, sep='/n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('Please, do not enter a number in the name field')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise Exception('Please, do not enter a number in the name field')
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for item in students:
            print(f"Student {item['FirstName']} {item['LastName']} is registered for {item['CourseName']}")
        print("-"*50)

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for item in students:
                print(f"Student {item['FirstName']} {item['LastName']} is enrolled in {item['CourseName']}")
        except Exception as e:
            print('Error saving to the file')
            print(e)
        finally:
            if file and not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
