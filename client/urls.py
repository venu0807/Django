from django.contrib import admin
from django.urls import path
from client.views import Complaint,PendingCases,SolvedCases,DeleteComplaint,UpdateComplaint

urlpatterns = [
    path('c/',Complaint),
    path('p/',PendingCases),
    path('s/',SolvedCases),
    path('d/<int:id>/',DeleteComplaint),
    path('u/<int:id>/',UpdateComplaint),
]
