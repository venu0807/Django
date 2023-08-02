from django.shortcuts import render
from django.http import HttpResponse
from officer.models import Team1

def homepage(request):
    return render(request,'index.html')

def T1(request):
    result=Team1.objects.all()
    team={'allofficers1':result}
    return render(request,'officer/t1.html',team)

def T2(request):
    return render(request,'officer/t2.html')