from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.core.files.storage import FileSystemStorage 
from django.db.models import Q
from .models import *

# Create your views here.
def post_job(request):
    return render(request,'postform.html')

def save_posted_job(request):
    if request.method == "POST":
        get_all = request.POST
        get_title = request.POST ['title']
        get_category = request.POST ['category']
        get_job_type = request.POST ['job_type']
        get_salary = request.POST ['salary']
        get_description = request.POST ['description']
        uploaded_file = request.FILES.get("file")
        fs = FileSystemStorage()
        get_file = fs.save(uploaded_file.name, uploaded_file)
        post_obj = Post(title=get_title,category=get_category,job_type=get_job_type, salary=get_salary, description =get_description, file=get_file)
        post_obj.save()
        return redirect ("/postjob/data")

