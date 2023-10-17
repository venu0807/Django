from django.contrib import admin
from officer.models import Team1,Team2

class T1admin(admin.ModelAdmin):
    list_display=['id','name','fathername','age','batch','role','contact']

class T2admin(admin.ModelAdmin):
    list_display=['id','name','fathername','age','batch','role','contact']

admin.site.register(Team1,T1admin)
admin.site.register(Team2,T2admin)
