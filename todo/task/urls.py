from django.urls import path
from .views import home,update,delete
from django.http import FileResponse

urlpatterns=[
    path('', home, name='home'),
    
    path('llms.txt', lambda request: FileResponse(open('LLms.txt', 'rb'), content_type='text/plain')),
    path('robots.txt', lambda request: FileResponse(open('robots.txt', 'rb'), content_type='text/plain')),
    path('update/<int:task_id>/', update, name='update'),
    path('delete/<int:task_id>/', delete, name='delete'),
]  