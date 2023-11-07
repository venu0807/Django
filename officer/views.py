from django.shortcuts import render
from django.http import HttpResponse
from officer.models import Team1,Team2
from officer.forms import AddofficerForm,AddofficerForm2
from client.models import Pending

def homepage(request):
    return render(request,'index.html')

def T1(request):
    result=Team1.objects.all()
    team={'allofficers1':result}
    return render(request,'officer/t1.html',team)

def T2(request):
    result=Team2.objects.all()
    team={'allofficers2':result}
    return render(request,'officer/t2.html',team)

def Add(request):
    form = AddofficerForm
    cform = {'form':form}

    if request.method == 'POST':
        form = AddofficerForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
    return render(request,'officer/add.html',cform)

def Add2(request):
    form = AddofficerForm2
    cform = {'form':form}

    if request.method == 'POST':
        form = AddofficerForm2(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
    return render(request,'officer/add.html',cform)
