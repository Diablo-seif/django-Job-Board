from . import views 
from django.urls import path

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail),
]
