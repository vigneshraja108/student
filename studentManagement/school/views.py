from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Student


# Create your views here.
def get_student(request):
    student_data = Student.objects.values()
    return HttpResponse(student_data)


@csrf_exempt
def add_student(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    create_student = Student(roll_number=body["roll_number"], name=body["name"], date_of_birth=body["date_of_birth"],
                             marks=body["marks"])
    create_student.save()

    return HttpResponse("successfully added")


@csrf_exempt
def get_exact_student(request, pk):
    student_data = Student.objects.filter(roll_number=pk).values()
    return HttpResponse(student_data)


@csrf_exempt
def add_student_mark(request, pk):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    update_student_mark = Student.objects.get(roll_number=pk)
    update_student_mark.marks = body["marks"]
    update_student_mark.save()
    return HttpResponse("successfully added")


@csrf_exempt
def get_student_mark(request, pk):
    student_mark = Student.objects.filter(marks=pk).values()
    return HttpResponse(student_mark)


def results(request):
    student_results = Student.objects.values("marks")
    grade_f = 0
    other_g = 0
    for i in student_results:
        for key, value in i.items():
            if value < 50:
                grade_f += value
            else:
                other_g += value
    pass_percentage = (other_g - grade_f) / other_g * 100

    return HttpResponse(f"The pass percentage is:{int(pass_percentage)}%")
