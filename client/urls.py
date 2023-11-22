from django.contrib import admin
from django.urls import path
from client.views import Complaint,PendingCases,SolvedCases,DeleteComplaint,UpdateComplaint,move,search_feature_client

urlpatterns = [
    path('c/',Complaint),
    path('p/',PendingCases),
    path('s/',SolvedCases),
    path('d/<int:id>/',DeleteComplaint),
    path('u/<int:id>/',UpdateComplaint),
    path('move/<int:id>/',move),
    path('search/',search_feature_client,name='search-view'),
]
