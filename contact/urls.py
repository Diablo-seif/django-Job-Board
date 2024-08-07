from django.urls import path
from . import views 

app_name = 'contact'  # تأكد من وجود هذا السطر

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    # أضف باقي المسارات هنا
]
