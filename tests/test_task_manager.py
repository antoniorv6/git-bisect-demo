import unittest
import tempfile
import shutil
from src.task_manager import TaskManager
from src.models import Priority, Status
from src.storage import Storage


class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.storage = Storage(self.temp_dir)
        self.manager = TaskManager(self.storage)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_create_task(self):
        task = self.manager.create_task("Test Task", "Description")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test Task")
    
    def test_get_task(self):
        task = self.manager.create_task("Test")
        retrieved = self.manager.get_task(task.id)
        self.assertEqual(retrieved.id, task.id)
    
    def test_list_tasks(self):
        self.manager.create_task("Task 1")
        self.manager.create_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
    
    def test_update_status(self):
        task = self.manager.create_task("Test")
        success = self.manager.update_status(task.id, Status.DONE)
        self.assertTrue(success)
        updated = self.manager.get_task(task.id)
        self.assertEqual(updated.status, Status.DONE)


if __name__ == '__main__':
    unittest.main()
