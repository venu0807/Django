from django.contrib import admin
from client.models import Pending,Solved

class PendingAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','age','causeofcomplaint','contact']

class SolvedAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','age','causeofcomplaint','contact']


admin.site.register(Pending,PendingAdmin)
admin.site.register(Solved,SolvedAdmin)
