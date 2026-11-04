from django.urls import path
from .views import home,update,delete

urlpatterns=[
    path('', home, name='home'),
    path('update/<int:task_id>/', update, name='update'),
    path('delete/<int:task_id>/', delete, name='delete'),
]