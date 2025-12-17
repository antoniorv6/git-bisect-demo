import unittest
from datetime import datetime, timedelta
from src.models import Task, Priority, Status
from src.notifications import NotificationSystem


class TestNotifications(unittest.TestCase):
    
    def test_critical_task_notification(self):
        system = NotificationSystem()
        task = Task("Critical bug", "", Priority.CRITICAL)
        task.id = 1
        notifications = system.check_task(task)
        self.assertGreater(len(notifications), 0)
        self.assertIn("CRÍTICO", notifications[0])
    
    def test_old_task_notification(self):
        system = NotificationSystem()
        task = Task("Old task", "", Priority.MEDIUM)
        task.id = 1
        task.created_at = datetime.now() - timedelta(days=40)
        notifications = system.check_task(task)
        self.assertGreater(len(notifications), 0)


if __name__ == '__main__':
    unittest.main()
