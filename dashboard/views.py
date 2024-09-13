from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *


class DashboardView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        data = {
            'faculties': Faculty.objects.count(),
            'departments': Department.objects.count(),
            'groups': Group.objects.count(),
            'subjects': Subject.objects.count(),
            'teachers': Teacher.objects.count(),
            'students': Student.objects.count(),
        }
        return Response(data)


class FacultyListView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
