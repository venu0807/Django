from django.contrib import admin
from django.urls import path
from officer.views import homepage
from officer.views import T1,T2,Add,Add2,Delete_Officer1,Delete_Officer2

urlpatterns = [
    path('',homepage),
    path('t1/',T1),
    path('t2/',T2),
    path('add/',Add),
    path('add2/',Add2),
    path('d1/<int:id>/',Delete_Officer1),
    path('d2/<int:id>/',Delete_Officer2),
]