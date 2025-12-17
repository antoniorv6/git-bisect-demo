import unittest
import os
import tempfile
from src.models import Task, Priority
from src.export import Exporter


class TestExporter(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.tasks = [
            Task("Task 1", "Description 1", Priority.HIGH),
            Task("Task 2", "Description 2", Priority.LOW),
        ]
        self.tasks[0].id = 1
        self.tasks[1].id = 2
    
    def test_export_to_csv(self):
        filename = os.path.join(self.temp_dir, "tasks.csv")
        Exporter.to_csv(self.tasks, filename)
        self.assertTrue(os.path.exists(filename))
    
    def test_export_to_json(self):
        filename = os.path.join(self.temp_dir, "tasks.json")
        Exporter.to_json(self.tasks, filename)
        self.assertTrue(os.path.exists(filename))


if __name__ == '__main__':
    unittest.main()
