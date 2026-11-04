from django.test import TestCase
from django.urls import reverse

from .models import task as Task


class TaskTests(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Learn Django",
            description="Finish CRUD assignment",
            completed=False
        )

    # -------------------
    # Model Test
    # -------------------

    def test_task_creation(self):
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(self.task.title, "Learn Django")
        self.assertFalse(self.task.completed)

    # -------------------
    # List View
    # -------------------

    def test_list_tasks(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)  # Redirect to login page if not authenticated

    # -------------------
    # Create View
    # -------------------

    def test_create_task(self):
        response = self.client.post(
            reverse("home"),
            {
                "title": "New Task",
                "description": "New Description",
                "completed": False,
            },
        )

        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertEqual(Task.objects.count(), 2)
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    # -------------------
    # Update View
    # -------------------

    def test_update_task(self):
        response = self.client.post(
            reverse("update", args=[self.task.id]),
            {
                "title": "Updated Title",
                "description": "Updated Description",
                "completed": "on",
            },
        )

        self.assertEqual(response.status_code, 302)  # Redirect after successful update

        self.task.refresh_from_db()

        self.assertEqual(self.task.title, "Updated Title")
        self.assertEqual(self.task.description, "Updated Description")
        self.assertTrue(self.task.completed)

    # -------------------
    # Delete View
    # -------------------

    def test_delete_task(self):
        response = self.client.post(
            reverse("delete", args=[self.task.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)