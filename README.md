# ProgBasics Personal Assessment

## MentorBot ver.3.0

Mentors feel overwhelmed by all the duties in Codecool. They asked you to write a short program that will help him cope with course management.

### Structure

MENTORBOT structure consists of three modules:

**data.py** - store functions regarding data management

**display.py** - store functions responsible for printing all the required data. In this module functions responsible for printing result are already implemented. First, try to understand how are they work and use them!

**main_program.py** - Heart of MENTORBOT that contains the main function and import data.py and display.py. **Also implements all functions for changing .txt file**

Module tests.py stores basic unit test for your project, based on test_class_data.txt Module bonus_tests.py stores tests for additional features --> **DO NOT MODIFY THOSE FILES!**

For your implementation operate only on class_data.txt REST OF TXT FILES ARE FOR TESTING PURPOSES ONLY - **DO NOT MODIFY THEM!**

The program has to import .txt file with values separated by commas as a primary source of data. Each line of the file represents student data in the following order:

`id,name,surname,year of birth,class,average grade,average presence`

Data exported to file should have the same format.

Basic functionality of the program focus on filtering and changing data by a user from the source file, with a certain level of persistence (the program can also save and export data)

### General info about requirements

Passing tests is something you need to get 10 or 12 points. However, if during manual testing, we find errors not found by tests from tests.py or bonus_tests.py, you will not reach max points for requirements.

### Requirements

1. You must implement all functions without docstring note that they are bonus features to get 10 points for requirements.
2. Your code must pass all basic tests (tests without BONUS in their name) to get 10 points for requirements.
3. Every empty basic function should be implemented as described in its docstrings. **PLEASE READ THEM CAREFULLY**
4. Built-in function **print() is forbidden in data.py module**
5. Your program's main menu offers at least four options for the user (you can choose which one from data.py module, for instance ----> 1. Print all students, 2. Get student by id,  3. Display the youngest student, 4. display the oldest student)
6. At least one function should be foolproof
7. At least one function should be able to handle potential exceptions (you can choose which one)
8. Create at least one additional function that wasn't defined in any of the modules
9. Use functions from the display module to display data
10. If you read this last requirement, smile and keep your head up! You can do it! :)

You can add your functions to any module if you feel they are needed to make your code cleaner.

### Additional Requirements

If your code passes all basic tests (tests without BONUS in their name, defined in tests.py), we will check bonus tests. To get 12 points for requirements your code has to pass all bonus tests (described in bonus_tests.py).

1. Extend your program by new function altering file values. Remember about clean code basic principles!
2. Implement sort_by_age function from data
3. Implement get_all_by_gender from data
4. Implement generate_id from data
5. Implement add_new_student from main_program
6. Every empty bonus function should be implemented as it was described in it's docstrings. **PLEASE READ THEM CAREFULLY**

### What are we going to check?

To mark your assignment, we'll use a [danish scale](https://en.wikipedia.org/wiki/Academic_grading_in_Denmark).
To get a green card, you should get 7 points at least in each category.
To get a yellow card, you should get 7 points at least for requirements and other category.
If you get a red card, you should take another PA trial.

|Criterion|12|10|7|4|2|0|-3|Comments|
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
|Conform requirements|pass all tests and implement ui + bonus tests|pass all tests and implement ui|pass 12 tests at least|pass 8 tests at least|pass 4 tests at least|pass no tests, but the program runs|program doesn't run|UI can be incomplete, but should be stable|
|Python Basics|extra tricks (one-liners, list comprehension etc.)|no mistakes or 1 minor mistake|1 major mistake or 2 minor mistakes at least|2 major mistakes or 4 minor mistakes at least|3 major mistakes or 6 minor mistakes at least|4 major mistakes or 8 minor mistakes at least|more than 4 major mistakes|Examples of mistakes: iterate by key in dictionary, useless continue/break etc., recursive function codes, force exceptions (use try/except statement wile condition should be checked)|
|Clean Code Basics|beautiful code, nothing to improve|short methods (<30 lines), if there's a nested code block more than 3 indications) it should be shorter than 10 lines|no repeated code blocks, no multiply statement in one line|proper naming, use PEP-8, no dead code|proper naming|misleading naming|it's impossible to understand what's going on|

During the interview, we'll verify these skills and technical language.
