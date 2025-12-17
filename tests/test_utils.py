import unittest
from datetime import datetime, timedelta
from src.models import Task
from src.utils import DateUtils, TextUtils, ValidationUtils


class TestDateUtils(unittest.TestCase):
    
    def test_format_date(self):
        date = datetime(2024, 1, 15, 10, 30, 0)
        formatted = DateUtils.format_date(date)
        self.assertIn("2024-01-15", formatted)
    
    def test_get_age_in_days(self):
        task = Task("Test")
        task.created_at = datetime.now() - timedelta(days=5)
        age = DateUtils.get_age_in_days(task)
        self.assertEqual(age, 5)


class TestTextUtils(unittest.TestCase):
    
    def test_truncate(self):
        text = "A" * 100
        truncated = TextUtils.truncate(text, 50)
        self.assertEqual(len(truncated), 50)
        self.assertTrue(truncated.endswith("..."))
    
    def test_generate_slug(self):
        slug = TextUtils.generate_slug("Hello World Test")
        self.assertEqual(slug, "hello-world-test")


class TestValidationUtils(unittest.TestCase):
    
    def test_validate_title(self):
        self.assertTrue(ValidationUtils.validate_title("Valid Title"))
        self.assertFalse(ValidationUtils.validate_title(""))
        self.assertFalse(ValidationUtils.validate_title("  "))


if __name__ == '__main__':
    unittest.main()
