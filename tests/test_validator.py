import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_invalid_input_string_of_int(self):
        self.assertEqual(False, validate_name("111111111"))

    def test_validate_name_with_invalid_input_string_of_intstring(self):
        self.assertEqual(False, validate_name("1denny50"))

    def test_validate_name_with_valid_input_name(self):
        self.assertEqual(True, validate_name("Anna"))

    def test_validate_name_with_invalid_input_special_string(self):
        self.assertEqual(False, validate_name("มิว##!!!"))

    def test_validate_name_with_invalid_input_space(self):
        self.assertEqual(False, validate_name("มิ   ว"))

    def test_validate_name_with_invalid_noinput(self):
        self.assertEqual(False, validate_name(""))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
