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


def SolvedCases(request):
    result=Solved.objects.all()
    sol={'allsolved':result}
    return render(request,'client/s.html',sol)


