"""
The main program should use functions from data and display modules
"""
import data
import display


def add_new_student(students, new_student):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Creates id for new student, adds it at the beginning of new student data,
    adds new student to students list and appends it to data file.

    :param list students: currently existing students
    :param list new_student: new student data without id. Format:
        name,surname,year of birth,class,average grade,average presence

    :returns: updated students list
    :rtype: list
    """
    current_ids = data.get_current_ids(students)
    uid = data.generate_id(current_ids)
    new_student.insert(0, uid)
    students.append(new_student)
    students[:] = students
    return students


def delete_student_by_id(students, uid):

    for properties in students:
        if uid == properties[0]:
            students.remove(properties)
    students[:] = students
    return students


def back_to_main_menu():
    yesno = display.yes_no()
    if yesno.lower() == "y":
        main()
    elif yesno.lower() == "n":
        print("See you!\n")
    else:
        print("There is no such choice.\n")
        back_to_main_menu()

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_commands = ["Get student by id\n", "Get students by class\n", "Get the youngest student data\n", "Get the oldest student data\n", "Get the youngest student data by class\n",   
    "Get the oldest student data by class\n", 
    "Get the average grade of students\n",
    "Get the average presence of students\n",        
    "Get students by gender\n",
    "Sort students by age (ascending and descending)\n",
    "Delete student by id\n",
    "Add new student\n",
    "Exit program\n"]

    title = open("title.txt", "r")
    menu_name = title.read()
    print(menu_name)
    title.close()

    students = data.import_data_from_file(filename='class_data.txt')
    display.print_program_menu(menu_commands)
    
    choice = input("Please give a number of an action to perform: \n")

    if choice != "12":

        if choice == "0":
            try:
                uid = input("\nPlease provide ID: \n")
                result = data.get_student_by_id(uid, students)
                print("\n")
                display.print_student_info(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("No such ID.")
                back_to_main_menu()

        elif choice == "1":
            try:
                class_name = (input("\nClass 'A' or 'B'?: \n")).upper()
                result = data.get_students_of_class(students, class_name)
                print("\n")
                display.print_students_list(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("No such class.")
                back_to_main_menu()

        elif choice == "2":
            print("\nThe youngest student:")
            result = data.get_youngest_student(students)
            print("\n")
            display.print_student_info(result)
            print("\n")
            back_to_main_menu()

        elif choice == "3":
            print("\nThe oldest student:")
            result = data.get_oldest_student(students)
            print("\n")
            display.print_student_info(result)
            print("\n")
            back_to_main_menu()

        elif choice == "4":
            try:
                class_name = (input("\nClass 'A' or 'B'?: \n")).upper()
                print("\nThe youngest student of the class:")
                result = data.get_youngest_student_of_class(students, class_name)
                print("\n")
                display.print_student_info(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("No such class.")
                back_to_main_menu()

        elif choice == "5":
            try:
                class_name = (input("\nClass 'A' or 'B'?: \n")).upper()
                print("\nThe oldest student of the class:")
                result = data.get_oldest_student_of_class(students, class_name)
                print("\n")
                display.print_student_info(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("No such class.")
                back_to_main_menu()

        elif choice == "6":
            print("\nThe average grade:")
            result = data.get_average_grade_of_students(students)
            print("\n")
            print(result)
            print("\n")
            back_to_main_menu()

        elif choice == "7":
            print("\nThe average presence:")
            result = data.get_average_presence_of_students(students)
            print("\n")
            print(result)
            print("\n")
            back_to_main_menu()

        elif choice == "8":
            try:
                gender = (input("\nmale(m) or female(f)?: \n")).lower()
                result = data.get_all_by_gender(students, gender)
                print("\n")
                display.print_students_list(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("Wrong gender!")
                back_to_main_menu()

        elif choice == "9":
            try:
                order = input("\nascending ('asc') or desc order('desc')?: \n")
                result = data.sort_students_by_age(students, order)
                print("\n")
                display.print_students_list(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("Wrong order!")
                back_to_main_menu()

        elif choice == "10":
            try:
                uid = input("\nPlease provide ID of student to delete: \n")
                result = delete_student_by_id(students, uid)
                print("\n")
                print("Updated table:\n")
                display.print_students_list(result)
                print("\n")
                back_to_main_menu()
            except ValueError:
                print("No such ID.")
                back_to_main_menu()
        
        elif choice == "11":
            
            list_labels = ["name", "surname", "birth year", "average grade", "average presence"]
            title = "Please provide student data to add: \n"
            new_student = display.get_inputs(list_labels, title)
            result = add_new_student(students, new_student)
            print("\n")
            print("Updated table:\n")
            display.print_students_list(result)
            print("\n")
            back_to_main_menu()

    elif choice == "12":
            print("See you!\n")


if __name__ == '__main__':
    main()
