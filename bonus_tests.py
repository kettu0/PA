import unittest
import re
import random

from data import sort_students_by_age, get_all_by_gender, generate_id


class BonusTestCase(unittest.TestCase):

    def setUp(self):
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

    def _sort_students(self, students, rev=False):
        return sorted(students, key=lambda student: student[3], reverse=rev)

    def test_BONUS_1_if_student_list_sorted_by_age_desc(self):
        sorted_students_list = sort_students_by_age(self.students, 'desc')
        expected = self._sort_students(sorted_students_list, True)

        self.assertListEqual(sorted_students_list, expected)

    def test_BONUS_2_if_student_list_sorted_by_age_asc(self):
        sorted_students_list = sort_students_by_age(self.students, 'asc')
        expected = self._sort_students(sorted_students_list)

        self.assertListEqual(sorted_students_list, expected)

    def test_BONUS_3_if_returns_empty_list_when_order_is_none(self):
        sorted_students_list = sort_students_by_age(self.students)

        self.assertListEqual(sorted_students_list, [])

    def test_BONUS_4_if_raise_error_when_sorting_with_wrong_order(self):
        self.assertRaisesRegex(ValueError, 'Wrong order', sort_students_by_age,
                               self.students, 'anything')

    def test_BONUS_5_if_get_student_by_gender_return_female(self):
        expected = [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
                    ['P3$o', 'Magdalena', 'Niedomirska', '1985', 'B', '83',
                    '72'],
                    ['K8^t', 'Katarzyna', 'Gdowski', '1991', 'B', '88', '74'],
                    ['Z7*r', 'Anna', 'Zmienna', '1996', 'A', '94', '87'],
                    ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61']]
        actual = get_all_by_gender(self.students, 'female')

        self.assertListEqual(actual, expected)

    def test_BONUS_6_if_raise_error_when_sorting_with_wrong_order(self):
        self.assertRaisesRegex(ValueError, 'Wrong gender', get_all_by_gender,
                               self.students, 'anything')

    def test_BONUS_7_if_generated_id_has_valid_format(self):
        current_ids = ['A4@z', 'W1&p', 'P9!x', 'P1)n', 'S0*l', 'M9@p', 'P3$o',
                       'L5%h', 'Q9(k', 'K8^t', 'Z7*r', 'R6$o', 'E4)i']
        example_id = generate_id(current_ids)
        id_regex = re.compile('^([A-Z][0-9][!@#$%^&*()_+)][a-z])$')

        self.assertTrue(id_regex.search(example_id))

    def test_BONUS_8_if_generated_id_is_unique(self):
        current_ids = ['A4@z', 'W1&p', 'P9!x', 'P1)n', 'S0*l', 'M9@p', 'P3$o',
                       'L5%h', 'Q9(k', 'K8^t', 'Z7*r', 'R6$o', 'E4)i']

        random.seed(1)
        first_id = generate_id(current_ids)
        random.seed(1)
        second_id = generate_id(current_ids)

        self.assertNotEqual(first_id, second_id)


if __name__ == '__main__':
    unittest.main()
