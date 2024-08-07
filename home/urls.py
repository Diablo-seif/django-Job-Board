from django.urls import path
from . import views 

app_name = 'home'  # تأكد من وجود هذا السطر

urlpatterns = [
    path('', views.home_view, name='home'),
    # أضف باقي المسارات هنا
]
