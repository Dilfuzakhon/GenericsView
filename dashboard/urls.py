from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('faculties/', FacultyListView.as_view(), name='faculty-list'),
    path('faculties/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),

    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),

    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),

    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
