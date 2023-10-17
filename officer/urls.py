from django.contrib import admin
from django.urls import path
from officer.views import homepage
from officer.views import T1,T2,Add,Add2

urlpatterns = [
    path('',homepage),
    path('t1/',T1),
    path('t2/',T2),
    path('add/',Add),
    path('add2/',Add2),
]