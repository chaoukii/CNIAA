from django.contrib import admin

# Register your models here.
from workshop.models import Comment, Submit, Speciality

admin.site.register(Comment)
admin.site.register(Submit)
admin.site.register(Speciality)
