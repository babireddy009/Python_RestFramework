from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    students = [
        {id:1, "name":"sachin","age":20, "email":"sachin@gmail.com"},
        {id:2, "name":"rahul","age":23, "email":"rahul@gmail.com"},
        {id:3, "name":"Venkat","age":23, "email":"venkat@gmail.com"},
        {id:4, "name":"vara","age":25, "email":"vara@gmail.com"},
 
    ]
    return HttpResponse(students)