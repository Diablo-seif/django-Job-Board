from django.urls import path
from . import views 

app_name = 'accounts'  # تأكد من وجود هذا السطر

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # أضف باقي المسارات هنا
]
