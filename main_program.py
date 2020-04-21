"""
The main program should use functions from data and display modules
"""
import data


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


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    pass

if __name__ == '__main__':
    main()
