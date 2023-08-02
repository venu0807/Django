from django.contrib import admin
from officer.models import Team1

class T1admin(admin.ModelAdmin):
    list_display=['id','name','fathername','age','batch','role','contact']

admin.site.register(Team1,T1admin)
