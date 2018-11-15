"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'attendance'
urlpatterns = [
     url(r'^student_profile/(?P<slug>.*)/$', views.student_profile, name="student_profile"),
     url(r'^add_attendance/$', views.add_attendance, name="add_attendance"),
     path('view-attendence/<int:sem>/<str:prog>/<str:sub>', views.faculty_view_attendence, name="faculty_view_attendence"),
     path('search-view-attendence/<int:sem>/<str:prog>/<str:sub>', views.faculty_search_view_attendence, name="faculty_search_view_attendence"),
     path('student_list/<int:sem>/<str:prog>/<str:sub>', views.student_list, name = "student_list"),

     path('today-attendance/<str:prof>/<int:semester>/<str:prog>/<str:sub>/<str:date>', views.today_attendance, name="today_attendance"),

     path('todays_add_attendance/<str:prof>/<int:semester>/<str:prog>/<str:sub>/<str:date>', views.todays_add_attendance, name="todays_add_attendance"),

    url(r'^view_attendance/$', views.view_attendance, name="view_attendance"),

    path('view_my_attendance_sem/<int:roll>/<int:sem>/<str:sub>', views.view_my_attendance_sem, name="view_my_attendance_sem"),


]
