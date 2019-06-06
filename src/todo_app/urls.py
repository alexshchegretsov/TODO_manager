from django.urls import path
from .views import home
from .views import create_task
from .views import edit_task
from .views import delete_task
from .views import to_up_task
from .views import to_down_task


urlpatterns = [
    path('', home, name='home_url'),
    path('create/', create_task, name='create_task_url'),
    path('edit/<int:task_id>/', edit_task, name='edit_task_url'),
    path('delete/<int:task_id>/', delete_task, name='delete_task_url'),
    path('<int:task_id>/', to_up_task, name='up_task_url'),
    path('down/<int:task_id>/', to_down_task, name='down_task_url'),
]