import unittest
from src.models import Task, Priority, Status


class TestTask(unittest.TestCase):
    
    def test_task_creation(self):
        task = Task("Test Task", "Description")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertEqual(task.status, Status.TODO)
    
    def test_task_to_dict(self):
        task = Task("Test", "Desc", Priority.HIGH)
        task.id = 1
        data = task.to_dict()
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['title'], "Test")
        self.assertEqual(data['priority'], 3)


if __name__ == '__main__':
    unittest.main()
