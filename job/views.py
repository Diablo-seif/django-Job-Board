from django.shortcuts import render
from .models import *
from .form import ApplyForm

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    context = {"jobs": job_list}
    return render(request, "pages/job/job_list.html", context)

def job_detail (request,slug) :
    job_detail = Job.objects.get(slug=slug)
    if request.method =='POST' :
        print('\n 1 \n')
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            print('\n 2 \n')
            myform = form.save(commit=False)
            myform.job=job_detail
            myform.save()
    else:
        form = ApplyForm()

    context = {"job":job_detail,"form":form}
    return render (request,"pages/job/job_detail.html",context)

