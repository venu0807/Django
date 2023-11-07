from django.shortcuts import render
from django.http import HttpResponse
from client.models import Pending,Solved
from client.forms import ComplaintForm
from officer.views import homepage



def Complaint(request):
    form=ComplaintForm
    cform={'form':form}


    if request.method =='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
        
    return render(request,'client/c.html',cform)

def PendingCases(request):
    result=Pending.objects.all()
    pen={'allpending':result}
    return render(request,'client/p.html',pen)

def DeleteComplaint(request,id):
    result=Pending.objects.get(id=id)
    result.delete()
    return homepage(request)

def UpdateComplaint(request,id):
    result=Pending.objects.get(id=id)
    form=ComplaintForm(instance=result)
    update={'form':form}
    

    if request.method =='POST':
        form=ComplaintForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            return PendingCases(request)
        

    return render(request,'client/update_complaint.html',update)


def move(request,id):
    table1 = Pending.objects.get(id=id)
    
    Solved.objects.create(
        name       = table1.name,
        fathername = table1.fathername,
        age = table1.age,
        causeofcomplaint = table1.causeofcomplaint,
        contact = table1.contact,
        )
    result = Pending.objects.get(id=id)
    result.delete()
    return homepage(request)


def SolvedCases(request):
    result=Solved.objects.all()
    sol={'allsolved':result}
    return render(request,'client/s.html',sol)
        

def Search_complaint(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Pending.objects.filter(name__contains=query_name)
            return render(request, 'complaint-search.html', {"results":results})

    return render(request, 'complaint-search.html')