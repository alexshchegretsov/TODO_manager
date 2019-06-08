from django.test import TestCase
from django.test import Client
from django.urls import reverse
from todo_app.views import create_task
from todo_app.views import edit_task
from todo_app.views import delete_task
from todo_app.models import Task


class TestView(TestCase):

    def setUp(self):
        self.c = Client()
        self.task = Task(content='test')
        self.task.save()

    def test_create_task_exists_at_desired_location(self):
        resp = self.c.get('/create/')
        self.assertEquals(resp.status_code, 200)

    def test_edit_task_exists_at_desired_location(self):
        resp = self.c.get(f'/edit/{self.task.id}/')
        self.assertEquals(resp.status_code, 200)

    def test_delete_task_exists_at_desired_location(self):
        resp = self.c.get(f'/delete/{self.task.id}/')
        self.assertEquals(resp.status_code, 302)

    def test_create_task_accessible_by_name(self):
        resp = self.c.get(reverse(create_task))
        self.assertEquals(resp.status_code, 200)

    def test_edit_task_accessible_by_name(self):
        resp = self.c.get(reverse(edit_task, args=[self.task.id]))
        self.assertEquals(resp.status_code, 200)

    def test_delete_task_accessible_by_name_and_redirect(self):
        resp = self.c.get(reverse(delete_task, args=[self.task.id]))
        self.assertEquals(resp.status_code, 302)

    def test_create_task_uses_correct_template(self):
        resp = self.c.get(reverse(create_task))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'todo_app/create.html')

    def test_edit_task_uses_correct_template(self):
        resp = self.c.get(reverse(edit_task, args=[self.task.id]))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'todo_app/edit.html')
