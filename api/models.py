
from statistics import mode
from aiohttp import request
from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import false, null, true
# Create your models here.
class AcademicYear(models.Model):
    fromDate=models.DateField()
    toDate=models.DateField()
    isCurrentAcademicYear=models.BooleanField(default=False)
    desc=models.TextField(null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.fromDate)+' -- '+str(self.toDate)

class Subject(models.Model):
    name=models.CharField(max_length=255)
    # classId=models.CharField(max_length=255,null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Classe(models.Model):
    name=models.CharField(max_length=255,unique=True,null=True,blank=True)
    subjects=models.ManyToManyField(Subject,blank=True)
    classRamaq=models.CharField(max_length=255,)
    studentsCount=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=True)
    academicYear=models.ForeignKey(AcademicYear,on_delete=models.CASCADE,null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name )+' -- '+str(self.classRamaq)


class Student(models.Model):
    studentId=models.CharField(max_length=255)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    password=models.CharField(max_length=255)
    gender=models.CharField(max_length=10,default='Male')
    image=models.ImageField(upload_to="students",blank=True,null=True)
    name=models.CharField(max_length=255)
    number=models.CharField(max_length=15,null=True,blank=True)
    masuulkaName=models.CharField(max_length=255,null=True,blank=True)
    masuulkaNumber=models.CharField(max_length=15,null=True,blank=True)
    stdClass=models.ForeignKey(Classe,null=True,blank=True,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    dateModified=models.DateTimeField(auto_now=True)
    accessedClasses=models.ManyToManyField(Classe,related_name='accessedClasses')
    stdARegistredAcademicYear=models.ForeignKey(AcademicYear,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)
    
class ExamType(models.Model):
    examName=models.CharField(max_length=255)
    examInfo=models.TextField()
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.examName)

class ExamEntring(models.Model):
    examType=models.ForeignKey(ExamType,on_delete=models.CASCADE)
    dateEnrying=models.DateField(null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    academicYear=models.ForeignKey(AcademicYear,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.dateEnrying)+' -- '+str(self.examType)+' -- '+str(self.academicYear)

class Result(models.Model):
    examId=models.ForeignKey(ExamEntring,on_delete=models.CASCADE)
    studentId=models.ForeignKey(Student,on_delete=models.CASCADE)
    resutPercentage=models.CharField(max_length=255,null=True,blank=True)
    resultSum=models.IntegerField(null=True,blank=True)
    resutlStatus=models.BooleanField(default=True)

class Marks(models.Model):
    theExamId=models.ForeignKey(ExamEntring,on_delete=models.CASCADE)
    studentId=models.ForeignKey(Student,on_delete=models.CASCADE)
    subjectId=models.ForeignKey(Subject,on_delete=models.CASCADE)
    stdClasse=models.ForeignKey(Classe,on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.studentId )+str(' '+str(self.subjectId)+' '+str(self.marks)+' '+str(self.theExamId))


class ExamEntringFiles(models.Model):
    examEntringFile=models.FileField(upload_to='examsEntringFile')
    theClasse=models.ForeignKey(Classe,on_delete=models.CASCADE)
    uploadedUser=models.ForeignKey(User,on_delete=models.CASCADE)
    dateUploaded=models.DateTimeField(auto_now=True)
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.examEntringFile.storage, self.examEntringFile.path
        # Delete the model before the file
        super(ExamEntringFiles, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)


class MarksTemp(models.Model):
    theExamId=models.ForeignKey(ExamEntring,on_delete=models.CASCADE)
    studentId=models.ForeignKey(Student,on_delete=models.CASCADE)
    subjectId=models.ForeignKey(Subject,on_delete=models.CASCADE)
    stdClasse=models.ForeignKey(Classe,on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.studentId )+str(' '+str(self.subjectId)+' '+str(self.marks)+' '+str(self.theExamId))
