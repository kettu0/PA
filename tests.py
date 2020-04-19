import unittest

from data import import_data_from_file, export_to_file, get_students_of_class,\
    get_youngest_student, get_average_grade_of_students,\
    get_average_presence_of_students, get_oldest_student, get_student_by_id,\
    get_oldest_student_of_class, get_youngest_student_of_class


class DataTestCase(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'test_class_data.txt'
        self.students = [
            ['A4@z', 'Maciej', 'Nowak', '1990', 'B', '80', '70'],
            ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '40'],
            ['P9!x', 'Grzegorz', 'Zgierski', '1992', 'B', '100', '90'],
            ['P1)n', 'Adam', 'Nowakowski', '1994', 'A', '98', '80'],
            ['S0*l', 'Dominik', 'Leski', '1997', 'A', '90', '75'],
            ['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
            ['P3$o', 'Magdalena', 'Niedomirska', '1985', 'B', '83', '72'],
            ['L5%h', 'Filip', 'Kowalski', '1980', 'B', '87', '83'],
            ['Q9(k', 'Andrzej', 'Modulny', '1991', 'A', '88', '84'],
            ['K8^t', 'Katarzyna', 'Gdowski', '1991', 'B', '88', '74'],
            ['Z7*r', 'Anna', 'Zmienna', '1996', 'A', '94', '87'],
            ['R6$o', 'Cyprian', 'Norwid', '1987', 'A', '95', '79'],
            ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61']]

    def test_if_export_raise_error_when_given_wrong_mode(self):
        self.assertRaisesRegex(ValueError, 'Wrong write mode', export_to_file,
                               self.students, self.test_filename, 'r')

    def test_export_data(self):
        import os
        tmp_filename = 'test_class_data_tmp.txt'
        export_to_file(self.students, tmp_filename)
        are_identical = self._compare_file_contents(
            self.test_filename, tmp_filename)
        os.remove(tmp_filename)

        self.assertTrue(are_identical)

    def test_import_data(self):
        actual = import_data_from_file(self.test_filename)

        self.assertListEqual(actual, self.students)

    def test_get_students_of_class(self):
        expected = [
            ['A4@z', 'Maciej', 'Nowak', '1990', 'B', '80', '70'],
            ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '40'],
            ['P9!x', 'Grzegorz', 'Zgierski', '1992', 'B', '100', '90'],
            ['P3$o', 'Magdalena', 'Niedomirska', '1985', 'B', '83', '72'],
            ['L5%h', 'Filip', 'Kowalski', '1980', 'B', '87', '83'],
            ['K8^t', 'Katarzyna', 'Gdowski', '1991', 'B', '88', '74'],
            ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61']]
        students = get_students_of_class(self.students, 'B')

        self.assertEqual(students, expected)

    def test_get_students_of_class_search_in_class_field_only(self):
        expected = [
            ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '40'],
            ['P3$o', 'Anna', 'Niedomirska', '1985', 'B', '83', '72']]
        class_data = [
            ['A4@z', 'B', 'Nowak', '1990', 'A', '80', '70'],
            ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '40'],
            ['P9!x', 'Grzegorz', 'B', '1992', 'A', '100', '90'],
            ['P3$o', 'Anna', 'Niedomirska', '1985', 'B', '83', '72'],
            ['L5%h', 'B', 'B', '1980', 'C', '87', '83']]
        students = get_students_of_class(class_data, 'B')

        self.assertEqual(students, expected)

    def test_if_get_youngest_returns_youngest_student_data(self):
        youngest_student = get_youngest_student(self.students)
        expected_output = ['S0*l', 'Dominik', 'Leski', '1997', 'A', '90', '75']

        self.assertListEqual(youngest_student, expected_output)

    def test_if_get_youngest_of_class_returns_yougest_student_data(self):
        oldest_student = get_youngest_student_of_class(self.students, 'B')
        expected = ['P9!x', 'Grzegorz', 'Zgierski', '1992', 'B', '100', '90']

        self.assertListEqual(oldest_student, expected)

    def test_if_get_average_grade_returns_expected_value(self):
        expected_value = 89.4
        students_data = [['A4@z', 'Maciej', 'Nowak', '1990', 'B', '80', '70'],
                         ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '40'],
                         ['P9!x', 'Grzegorz', 'Zgierski', '1992', 'B', '100', '90'],
                         ['P1)n', 'Adam', 'Nowakowski', '1994', 'A', '98', '80'],
                         ['S0*l', 'Dominik', 'Leski', '1997', 'A', '90', '75']]

        actual = get_average_grade_of_students(students_data)

        self.assertAlmostEqual(actual, expected_value)

    def test_average_presence_rounded_down_below_half(self):
        expected_value = 74
        actual = get_average_presence_of_students(self.students)

        self.assertEqual(actual, expected_value)

    def test_average_presence_rounded_up_on_half(self):
        students = [
            ['A4@z', 'Maciej', 'Nowak', '1990', 'B', '80', '70'],
            ['W1&p', 'Piotr', 'Dolny', '1989', 'B', '79', '43']]
        expected_value = 57
        actual = get_average_presence_of_students(students)

        self.assertEqual(actual, expected_value)

    def test_if_get_oldest_returns_oldest_student_data(self):
        oldest_student = get_oldest_student(self.students)
        expected = ['L5%h', 'Filip', 'Kowalski', '1980', 'B', '87', '83']

        self.assertListEqual(oldest_student, expected)

    def test_if_get_oldest_of_class_returns_oldest_student_data(self):
        oldest_student = get_oldest_student_of_class(self.students, 'A')
        expected = ['R6$o', 'Cyprian', 'Norwid', '1987', 'A', '95', '79']

        self.assertListEqual(oldest_student, expected)

    def test_return_student_data_if_valid_id(self):
        actual = get_student_by_id('A4@z', self.students)
        expected = ['A4@z', 'Maciej', 'Nowak', '1990', 'B', '80', '70']

        self.assertListEqual(actual, expected)

    def test_if_raise_error_when_student_doesnt_exist(self):
        self.assertRaisesRegex(ValueError, 'Student does not exist',
                               get_student_by_id, '(A4@z', self.students)

    def _compare_file_contents(self, first, second):
        first_content = self._readfile(first)
        second_content = self._readfile(second)

        return first_content == second_content

    def _readfile(self, filename):
        content = ''
        with open(filename, 'r') as f:
            content = f.read()

        return content


if __name__ == '__main__':
    unittest.main()
