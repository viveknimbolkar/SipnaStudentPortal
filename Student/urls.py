from Student import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.student_login,name='student login'),
    path('dashboard',views.student_dashboard,name='student dashboard'),
    path('profile',views.student_profile,name='student profile'),
    path('notifications',views.student_notifications,name='student notifications'),
]