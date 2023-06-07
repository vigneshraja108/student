from django.urls import path
from .views import get_student, add_student, get_exact_student, get_student_mark, add_student_mark, results

urlpatterns = [
    path('api/students/', get_student, name="students"),
    path('api/student/add/', add_student, name="students"),
    path('api/student/results/', results, name="student_results"),
    path('api/student/<pk>/', get_exact_student, name="students"),
    path('api/student/<pk>/add-mark/', add_student_mark, name="students"),
    path('api/student/<pk>/mark/', get_student_mark, name="students"),
]
