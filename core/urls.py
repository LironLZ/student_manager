from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.teacher_login, name='login'),
    path('logout/', views.teacher_logout, name='logout'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_assignment/<int:student_id>/', views.add_assignment, name='add_assignment'),
    path('edit_assignment/<int:assignment_id>/', views.edit_assignment, name='edit_assignment'),
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
]
