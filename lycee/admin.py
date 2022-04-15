from django.contrib import admin

from .models import Student, Cursus
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "phone")

admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus)