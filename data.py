"""
This module should use random module to generate_id
"""
import random

def import_data_from_file(filename='class_data.txt'):
    """
    Import data from file to list. Expected returned data format:
        [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
        ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61'],
        ...]

    :param str filename: optional, name of file to be imported

    :returns: list of lists representing students' data
    :rtype: list
    """
    students_list = []

    with open(filename, "r") as class_list:
        all_students = class_list.readlines()

        for line in all_students:
            properties = line.strip("\n").split(",")
            students_list.append(properties)
        return students_list


def export_to_file(data, filename='class_data.txt', mode='a'):
    """
    Export data from list to file. If called with mode 'w' it should overwritte
    data in file. If called with mode 'a' it should append data at the end.

    :param list data: students' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode != "a" and mode != "w":
        raise ValueError("Wrong write mode")

    with open(filename, mode) as class_list:
        for student in data:
            line = ",".join(student)
            class_list.write(line + "\n")



def get_student_by_id(uid, students):
    """
    Get student by unique id

    :param str uid: student unique id
    :param list students: students' data

    :raises ValueError: if student's uid not found in class data.
        Error message: 'Student does not exist'

    :returns: specific student's data
    :rtype: list
    """

    for properties in students:
        if properties[0] == uid:
            return properties
        if uid not in properties:
            raise ValueError("Student does not exist")


def get_students_of_class(students, class_name):
    """
    Get all students from given class

    :param list students: list of nested list imported from file
    :param str class_name: string representing class name that student\
        attends to

    :returns: students from given class only
    :rtype: list
    """

    students_from_class = []
    class_index = 4

    for properties in students:
        if properties[class_index] == class_name:
            students_from_class.append(properties)
    return students_from_class


def get_youngest_student(students):
    """
    Get youngest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: youngest student
    :rtype: list
    """

    year_index = 3
    latest_year = 1900

    for properties in students:
        birth_year = int(properties[year_index])
        if birth_year > latest_year:
            latest_year = birth_year

    for properties in students:
        if latest_year == int(properties[year_index]):
            return properties


def get_youngest_student_of_class(students, class_name):
    """
    Get youngest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: youngest student from given class
    :rtype: list
    """
    
    latest_year = 1900
    year_index = 3
    class_index = 4
    
    for properties in students:
        if properties[class_index] == class_name:
            birth_year = int(properties[year_index])
            if birth_year > latest_year:
                latest_year = birth_year

    for properties in students:
        if latest_year == int(properties[year_index]):
            return properties


def get_oldest_student(students):
    """
    Get oldest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: oldest student
    :rtype: list
    """

    year_index = 3
    current_year = 2020

    for properties in students:
        birth_year = int(properties[year_index])
        if birth_year < current_year:
            current_year = birth_year

    for properties in students:
        if current_year == int(properties[year_index]):
            return properties


def get_oldest_student_of_class(students, class_name):
    """
    Get oldest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: oldest student
    :rtype: list
    """
    year_index = 3
    class_index = 4
    current_year = 2020

    for properties in students:
        if properties[class_index] == class_name.lower() or properties[class_index] == class_name.upper():
            birth_year = int(properties[year_index])
            if birth_year < current_year:
                current_year = birth_year

    for properties in students:
        if current_year == int(properties[year_index]):
            return properties


def get_average_grade_of_students(students):
    """
    Calculate average grade of all students

    IMPORTANT:
        Implement this function without built-in functions like sum()
        or similar

    :param list students:  students' data

    :returns: average grade of students value
    :rtype: float
    """

    grade_index = 5
    student_counter = 0
    grade_sum = 0

    for properties in students:
        student_counter += 1
        grade_sum += float(properties[grade_index])
        grade_avg = float(grade_sum/student_counter)
    return grade_avg


def get_average_presence_of_students(students):
    """
    Returns rounded average presence of all students. For instance,
    if average presence is 35.4912, returned value should be 35,
    if average presence is 41.5, returned value should be 42,

    IMPORTANT:
        Implement this function without built-in functions like sum(), round()
        or similar

    :param list students:  students' data

    :returns: average presence of students rounded to int
    :rtype: int
    """

    presence_index = 6
    student_counter = 0
    presence_sum = 0

    for properties in students:
        student_counter += 1
        presence_sum += int(properties[presence_index])
        presence_avg = presence_sum/student_counter

    if isinstance(presence_avg, float) is True:
        presence_avg = presence_avg + 0.5
    else:
        isinstance(presence_avg, int) is True
    return int(presence_avg)


def get_current_ids(students):

    current_ids = []
    for properties in students:
        uid_index = 0
        current_ids.append(properties[uid_index])
    return current_ids

def generate_id(current_ids):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Generate unique id. It should be unique in all existing students list. If
    generated id was already used, function should regenerate it untill it is
    totaly new. Newly generated unique id should be added to current_ids

    REQUIREMENTS:
        - All ids must be 4-characters long
        - Characters should appear in given order:
            1. Upper letter
            2. Digit from 0 to 9
            3. Special character from this list: !@#$%^&*()_+
            4. Lower letter

            Example ids:
                W1&p
                M9@p
                P1!n

    :param list current_ids: list of all ids. It's used to check if
            generated id is unique or not. If new id is unique, current_ids
            should be extended to include this new id.

    :returns: unique id
    :rtype: str
    """

    pattern = "UNCL"
    unique_id = ""
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "!@#$%^&*()_+"

    for character in pattern:
        if character == 'U':
            unique_id += upper_case[random.randrange(len(upper_case))]
        if character == 'N':
            unique_id += numbers[random.randrange(len(numbers))]
        if character == 'C':
            unique_id += special_chars[random.randrange(len(special_chars))]
        if character == 'L':
            unique_id += lower_case[random.randrange(len(lower_case))]

    if unique_id not in current_ids:
        current_ids.append(unique_id)
        return unique_id


def get_all_by_gender(students, gender):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Get all students with given gender. As someone forgot to ask students about
    it, the only way JERZYBOT can find out if someone is female is her name.
    Treat all students with name ending with 'a' as female (Maria, Anna, etc).
    (we're sorry Miriam, we'll update JERZYBOT as soon as possible)

    :param list students:  students' data
    :param str gender: gender to filter by. 'female' will return female
        students, 'male' will return list of male students

    :raises ValueError: if gender other than 'female' or 'male' was given.
        Error message: 'Wrong gender'

    :returns: list of students filtered by given gender
    :rtype: list
    """
    name_index = 1
    index = 0
    students_by_gender = []

    for properties in students:
        name = students[index][name_index]
        if gender == "female" or gender == "f":
            if name[-1] == "a":
                students_by_gender.append(properties)

        elif gender == "male" or gender == "m":
            if name[-1] != "a":
                students_by_gender.append(properties)
        else:
            raise ValueError("Wrong gender")
        index += 1
    return students_by_gender


def sort_students_by_age(students, order=None):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Sorts student list by age. User can choose sorting order by passing
    'desc' for descending order or 'asc' for ascening order.
    If order is None returns empty list

    IMPORTANT:
        Implement this function without using sorted() or similar built-in
        functions

    :param list students:  students' data
    :param str order: optional, sorting order

    :raises ValueError: if order other than 'asc', 'desc' or None
        was given

    :returns: sorted students or empty list
    :rtype: list
    """
    year_index = 3
    index = 0
    students_length = len(students)

    if order == "asc":
        while index < students_length-1:
            next_index = 0
            while next_index < students_length - index - 1:
                if students[next_index][year_index] > students[next_index+1][year_index]:
                    temp = students[next_index+1][year_index]
                    students[next_index+1][year_index] = students[next_index][year_index]
                    students[next_index][year_index] = temp
                next_index = next_index + 1
            index = index + 1
        return students

    elif order == "desc":
        while index < students_length-1:
            next_index = 0
            while next_index < students_length - index - 1:
                if students[next_index][year_index] < students[next_index+1][year_index]:
                    temp = students[next_index+1][year_index]
                    students[next_index+1][year_index] = students[next_index][year_index]
                    students[next_index][year_index] = temp
                next_index = next_index + 1
            index = index + 1
        return students

    elif order is None:
        students = []
        return students

    else:
        raise ValueError("Wrong order")


def main():
    pass


if __name__ == '__main__':
    main()