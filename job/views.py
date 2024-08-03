from django.shortcuts import render
from .models import *
# Create your views here.
def job_list (request) :
    job_list = Job.objects.all()
    context = {"jobs":job_list}
    return render (request,"pages/job.html",context)
    

def job_detail (request,id) :
    job_detail = Job.objects.get(id=id)
    context = {"job":job_detail}
    return render (request,"pages/job_detail.html",context)

