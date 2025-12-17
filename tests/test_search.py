import unittest
from src.models import Task, Priority, Status
from src.search import SearchEngine


class TestSearchEngine(unittest.TestCase):
    
    def setUp(self):
        self.tasks = [
            Task("Buy groceries", "Milk and bread", Priority.HIGH),
            Task("Write report", "Q4 report", Priority.MEDIUM),
            Task("Call client", "Follow up", Priority.LOW),
        ]
        self.tasks[0].tags = ["shopping", "urgent"]
        self.tasks[1].tags = ["work"]
        self.tasks[2].tags = ["work", "client"]
    
    def test_search_by_title(self):
        results = SearchEngine.search_by_title(self.tasks, "report")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Write report")
    
    def test_search_by_tag(self):
        results = SearchEngine.search_by_tag(self.tasks, "work")
        self.assertEqual(len(results), 2)
    
    def test_filter_by_priority(self):
        results = SearchEngine.filter_by_priority(self.tasks, Priority.HIGH)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Buy groceries")
    
    def test_sort_by_priority(self):
        sorted_tasks = SearchEngine.sort_by_priority(self.tasks)
        self.assertEqual(sorted_tasks[0].priority, Priority.HIGH)


if __name__ == '__main__':
    unittest.main()
