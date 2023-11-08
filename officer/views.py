from django.shortcuts import render
from django.http import HttpResponse
from officer.models import Team1,Team2
from officer.forms import AddofficerForm,AddofficerForm2
from django.db.models import Q

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

def Delete_Officer1(request,id):
    result=Team1.objects.get(id=id)
    result.delete()
    return homepage(request)


def Delete_Officer2(request,id):
    result=Team2.objects.get(id=id)
    result.delete()
    return homepage(request)

def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Team1.objects.filter(name__contains=search_query) or Team2.objects.filter(name__contains=search_query)
        return render(request, 'officer/officer-search.html', {'querys':search_query, 'post':posts})
    else:
        return render(request, 'officer/officer-search.html',{})