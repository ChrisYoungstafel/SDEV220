# Christopher Youngstafel
# Module 2 Lab - Case Study.py
# Description - the program will ask for students names and GPA's then output where they placed

# start loop to check the student
while True:
    # get last name and quit if "zzz"
    last_name = input("Enter the students last name, enter 'ZZZ' to quit: ")
    if last_name == "zzz" or last_name == "ZZZ":
        print ("Exiting")
        break

    # get first name
    first_name = input("Enter the students first name: ")

    # get GPA
    gpa = float(input("What is the students GPA: "))

    # output where they placed
    if gpa >= 3.5:
        print(first_name + " " + last_name + " made the dean's list")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the honor roll")
    else:
        print(first_name + " " + last_name + " did not make the dean's list or honor roll")
