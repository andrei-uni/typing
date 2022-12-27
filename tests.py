import random
import time
import unittest
from Modules.Accuracy_Statistics import AccuracyStatistic
from Modules.FileVerifier import FileVerifier
from Modules.Speed_Statistics import SpeedStatistics


class TestAccuracy(unittest.TestCase):

    def test_start_position(self):
        cur_index = 0
        correct_count = 0
        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)
        self.assertEqual(stat, 0)

    def test_zero_correct(self):
        cur_index = 100
        correct_count = 0
        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)

        self.assertEqual(stat, 0)

    def test_random_position(self):
        cur_index = random.randint(0, 1000)
        correct_count = random.randint(0, 1000)
        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)

        if correct_count > cur_index:
            self.assertEqual(stat, 0)
        else:
            self.assertEqual(stat, int(correct_count / cur_index * 100))

    def test_current_less_correct(self):
        cur_index = 10
        correct_count = 12

        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)

        self.assertEqual(stat, 0)

    def test_current_eql_correct(self):
        cur_index = 12
        correct_count = 12

        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)

        self.assertEqual(stat, 100)

    def test_basic(self):
        cur_index = 10
        correct_count = 6

        stat = AccuracyStatistic.calculate_correctness_percent(cur_index, correct_count)

        self.assertEqual(stat, 60)


class TestSpeedStatistic(unittest.TestCase):

    def test_simple(self):
        cur_index = 10
        start_time = time.perf_counter()

        time.sleep(3)

        stat = SpeedStatistics.calculate_speed(cur_index, start_time)
        self.assertEqual(stat, 200)

    def test_zero_current(self):
        cur_index = 0
        start_time = time.perf_counter()

        time.sleep(3)

        stat = SpeedStatistics.calculate_speed(cur_index, start_time)

        self.assertEqual(stat, 0)

    def test_random_current(self):
        cur_index = random.randint(0, 100)
        start_time = time.perf_counter()

        time.sleep(3)

        stat = SpeedStatistics.calculate_speed(cur_index, start_time)

        self.assertEqual(stat, 20*cur_index)


class TestTextReplacement(unittest.TestCase):

    def test_empty_text(self):
        text = ""

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "")

    def test_one_rome_number_text(self):
        text = "Ⅴ"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "V")

    def test_some_rome_numbers_text(self):
        text = "ⅤⅬⅣⅢ"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "VLIVIII")

    def test_one_rome_number_with_normal_symbols(self):
        text = "simple Ⅲ"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "simple III")

    def test_some_rome_numbers_with_normal_symbols(self):
        text = "simple Ⅲ to me in ⅩⅣ"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "simple III to me in XIV")

    def test_text_without_replacements(self):

        text = "simple text without replacements"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, text)

    def test_dash_replacements(self):

        text = "—–‒―"

        result = FileVerifier.replace_not_keyboard_symbols(text)

        self.assertEqual(result, "----")



