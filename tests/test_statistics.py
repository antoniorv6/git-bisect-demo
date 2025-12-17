import unittest
from src.models import Task, Priority, Status
from src.statistics import Statistics


class TestStatistics(unittest.TestCase):
    
    def setUp(self):
        self.tasks = [
            Task("Task 1", "", Priority.HIGH),
            Task("Task 2", "", Priority.MEDIUM),
            Task("Task 3", "", Priority.LOW),
            Task("Task 4", "", Priority.LOW),
        ]
        self.tasks[0].status = Status.DONE
        self.tasks[1].status = Status.IN_PROGRESS
        self.tasks[2].status = Status.TODO
        self.tasks[3].status = Status.TODO

    
    def test_count_by_status(self):
        counts = Statistics.count_by_status(self.tasks)
        self.assertEqual(counts[Status.DONE], 1)
        self.assertEqual(counts[Status.IN_PROGRESS], 1)
        self.assertEqual(counts[Status.TODO], 2)
    
    def test_completion_rate(self):
        rate = Statistics.completion_rate(self.tasks)
        self.assertAlmostEqual(rate, 25, places=1)
    
    def test_productivity_score(self):
        score = Statistics.productivity_score(self.tasks)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 100)


if __name__ == '__main__':
    unittest.main()
