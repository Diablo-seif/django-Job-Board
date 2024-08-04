from . import views 
from django.urls import path
app_name = 'job'

urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('<int:id>', views.job_detail,name='job_detail'),
]


