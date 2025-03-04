from django.urls import path
from . import views

urlpatterns = [
    path('registeration/', views.registration,name='registeration'),
    path('login/', views.login,name='login'),
    path('courselist/', views.courselist,name='courselist'),
    path('logout/', views.logout,name='logout'),
    path('subject<int:id>/', views.subject,name='subject'),
    path('addcourse/', views.addcourse,name='addcourse'),
    path('addsubject/', views.addsubject,name='addsubject'),
    path('enrollment/', views.enrollment,name='enrollment'),
]