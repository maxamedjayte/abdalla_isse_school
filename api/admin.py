from django.contrib import admin

from api.models import AcademicYear, Classe,  ExamEntring, ExamEntringFiles, ExamType, Marks, MarksTemp,  Result, Student, Subject

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Subject)
admin.site.register(Classe)
admin.site.register(Student)
admin.site.register(ExamEntring)
admin.site.register(ExamType)
admin.site.register(Result)
admin.site.register(Marks)
admin.site.register(ExamEntringFiles)
admin.site.register(MarksTemp)