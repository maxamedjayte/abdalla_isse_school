from django.db import models
from django.db.models import fields
from numpy import source
from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'



class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model=AcademicYear
        fields='__all__'
        # depth = 1 


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'
        # depth = 1 


class ClasseSerializer(serializers.ModelSerializer):
    # maadooyinka = serializers.ReadOnlyField(source='subjects')
    isActive=serializers.ReadOnlyField(source='academicYear.isCurrentAcademicYear')
    sanadDugsiyedkaFrom = serializers.ReadOnlyField(source='academicYear.fromDate')
    sanadDugsiyedkaTo = serializers.ReadOnlyField(source='academicYear.toDate')
    class Meta:
        model=Classe
        fields='__all__'
        # depth = 1 


class StudentSerializer(serializers.ModelSerializer):
    stdClassName = serializers.ReadOnlyField(source='stdClass.name')
    stdClassRaqam = serializers.ReadOnlyField(source='stdClass.classRamaq')
    stdClassSanadDugsiyedkaFrom =serializers.ReadOnlyField(source='stdClass.academicYear.fromDate')
    stdClassSanadDugsiyedkaTo =serializers.ReadOnlyField(source='stdClass.academicYear.toDate')
    stdAccessedClasses=Student.accessedClasses
    class Meta:
        model=Student
        fields='__all__'
        # depth = 2 


class ExamEntringSerializer(serializers.ModelSerializer):
    examEntringName = serializers.ReadOnlyField(source='examType.examName')
    sanadDugsiyedkaFrom = serializers.ReadOnlyField(source='academicYear.fromDate')
    isActive=serializers.ReadOnlyField(source='academicYear.isCurrentAcademicYear')
    sanadDugsiyedkaTo = serializers.ReadOnlyField(source='academicYear.toDate')
    class Meta:
        model=ExamEntring
        fields='__all__'
        # depth = 1 



class ExamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExamType
        fields='__all__'
        # depth = 1 




class MarksSerializer(serializers.ModelSerializer):
    theExamName = serializers.ReadOnlyField(source='theExamId.name')
    studentName = serializers.ReadOnlyField(source='studentId.name')
    subjectName = serializers.ReadOnlyField(source='subjectId.name')
    class Meta:
        model=Marks
        fields='__all__'
        # depth = 1 

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields='__all__'


class ExamEntringFilesSerializer(serializers.ModelSerializer):
    className = serializers.ReadOnlyField(source='theClasse.name')
    classRaqam = serializers.ReadOnlyField(source='theClasse.classRamaq')
    classSanadDugsiyedkaFrom =serializers.ReadOnlyField(source='theClasse.academicYear.fromDate')
    classSanadDugsiyedkaTo =serializers.ReadOnlyField(source='theClasse.academicYear.toDate')
    username=serializers.ReadOnlyField(source='uploadedUser.username')
    fullname=str(serializers.ReadOnlyField(source='uploadedUser.first_name'))
    class Meta:
        model=ExamEntringFiles
        fields='__all__'

