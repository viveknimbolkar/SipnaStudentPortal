from django.shortcuts import redirect, render
# Create your views here.
def index(req):
    return render(req,"pages/home.html")


def student_login(req):
    return render(req,"pages/student-login.html")


def student_dashboard(req):
    return render(req,'pages/student-dashboard.html')


def student_profile(req):
    return render(req,'pages/student-dashboard.html')


def student_notifications(req):
    return render(req,'pages/student-notification-dashboard.html')