from django.contrib import admin

from web.models import Class, ClassTeacher, Parent, Students, Subjects


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age']


class ParentAdmin(admin.ModelAdmin):
    list_display = ['name','age']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_teacher','division']


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['name']


class ClassTeacherAdmin(admin.ModelAdmin):
    list_display = ['name','qualification']



admin.site.register(Students)
admin.site.register(Parent)
admin.site.register(Class)
admin.site.register(Subjects)
admin.site.register(ClassTeacher)


