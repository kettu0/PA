"""
The main program should use functions from data and display modules
"""


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


def delete_student_by_id(students, uid):
    """
    Deletes student from list by given unique id and updates data file

    :param list students: currently existing students
    :param str uid: unique id of student to be deleted

    :returns: updated students list
    :rtype: list
    """


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """


if __name__ == '__main__':
    main()
