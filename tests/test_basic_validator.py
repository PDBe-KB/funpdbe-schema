from unittest import TestCase
from basic_validator.basic_validator import run


class TestBasicValidator(TestCase):

    def test_run_with_valid_json(self):
        self.assertTrue(run("./tests/test_schema.json", "./tests/test_json_valid.json"))

    def test_run_with_invalid_json(self):
        self.assertFalse(run("./tests/test_schema.json", "./tests/test_json_invalid.json"))