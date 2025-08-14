from django.urls import path
from tasks.views import show_task,show_task_specific_work

urlpatterns = [
    path('show-task/',show_task),
    path('show-task/<int:id>/',show_task_specific_work)
]
