def print_student_info(student_data):
    print("Student id ---> %s" % student_data[0])
    for index in range(1, len(student_data)):
        print(student_data[index], end=" | ")


def print_students_list(student_data):
    for student in student_data:
        print(" | ".join(student))


def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option)) + "----->" + option)


def print_command_result(message):
    print(2 * "\n" + message)


def yes_no():
    user_input = input("Back to main menu? Y or N:\n")
    return user_input 
