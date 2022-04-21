from unittest import result
from django.shortcuts import render
from django.http import HttpResponse, response
from django.http.response import JsonResponse
from django.shortcuts import render

# import xlrd

from rest_framework.decorators import api_view
from rest_framework.response import Response
from sqlalchemy import true

from api.models import *
from .serializers import *
from api import serializers
# Create your views here.



# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_url={
        'Doc-List':'/doc-list/',
        'Doc-create':'doc-create/',
        'Delete':'',
    }
    return Response(api_url)


# dashinfo
@api_view(['GET'])
def dashInfo(request):
    tiradaGabdhaha=Student.objects.filter(gender='female').count()
    tiradaWiilasha=Student.objects.filter(gender='male').count()
    tiradaFasalada=Classe.objects.filter().count()
    # tiradaGabdhaha=UserSerializer(Student.objects.filter(gender='Female').count,many=False)
    return Response({'gabdhaha':tiradaGabdhaha,'wiilasha':tiradaWiilasha,'fasalada':tiradaFasalada})

# user 
@api_view(['GET'])
def userList(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def userCreate(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

def passwordFormat(request,pk):
    theUser=User.objects.get(pk=pk)
    theUser.set_password(theUser.password)
    theUser.save()
    return HttpResponse('')
@api_view(['POST'])
def userUpdate(request,pk):
    user=User.objects.get(pk=pk)
    serializer=UserSerializer(instance=user,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def userDelete(request,pk):
    theUser=User.objects.get(pk=pk)
    theUser.delete()
    return Response()

@api_view(['GET'])
def userDetail(request,pk):
    user=User.objects.get(pk=pk)
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)









# ardada 
@api_view(['GET'])
def academicYearList(request):
    academicYear=AcademicYear.objects.all().order_by('-isCurrentAcademicYear')
    serializer=AcademicYearSerializer(academicYear,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def academicYearCreate(request):
    serializer=AcademicYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def academicYearUpdate(request,pk):
    academicYear=AcademicYear.objects.get(pk=pk)
    serializer=AcademicYearSerializer(instance=academicYear,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def academicYearDelete(request,pk):
    academicYear=AcademicYear.objects.get(pk=pk)
    academicYear.delete()
    return Response()

@api_view(['GET'])
def academicYearDetail(request,pk):
    academicYear=AcademicYear.objects.get(pk=pk)
    serializer=AcademicYearSerializer(academicYear,many=False)
    return Response(serializer.data)





# Subject
@api_view(['GET'])
def subjectList(request):
    subject=Subject.objects.all()
    serializer=SubjectSerializer(subject,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def subjectCreate(request):
    serializer=SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def subjectUpdate(request,pk):
    subject=Subject.objects.get(pk=pk)
    serializer=SubjectSerializer(instance=subject,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def subjectDelete(request,pk):
    subject=Subject.objects.get(pk=pk)
    subject.delete()
    return Response()

@api_view(['GET'])
def subjectDetail(request,pk):
    subject=Subject.objects.get(pk=pk)
    serializer=SubjectSerializer(subject,many=False)
    return Response(serializer.data)







# classes
@api_view(['GET'])
def classeList(request):
    classe=Classe.objects.all().order_by('-id')
    serializer=ClasseSerializer(classe,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def classeCreate(request):
    serializer=ClasseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def classeUpdate(request,pk):
    classe=Classe.objects.get(pk=pk)
    serializer=ClasseSerializer(instance=classe,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def classeDelete(request,pk):
    classe=Classe.objects.get(pk=pk)
    classe.delete()
    return Response()

@api_view(['GET'])
def classeDetail(request,pk):
    classe=Classe.objects.get(pk=pk)
    serializer=ClasseSerializer(classe,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def classeSubjects(request,pk):
    subjects=Classe.objects.get(pk=pk)
    serializer=ClasseSerializer(subjects,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def checkingClassExist(request,className,classRaqam,academicYear):
    classe=Classe.objects.filter(name=className,classRamaq=classRaqam,academicYear=academicYear).exists()
    # serializer=ClasseSerializer(classe,many=True)
    return Response({'isExist':classe})


@api_view(['GET'])
def studentsForThisClass(request,pk):
    students=Student.objects.filter(stdClass=pk)
    classInfo=Classe.objects.get(pk=pk)
    serializerClass=ClasseSerializer(classInfo,many=False)
    serializer=StudentSerializer(students,many=True)
    return Response({'stdData':serializer.data,'clsData':serializerClass.data})















# subjects
@api_view(['GET'])
def studentList(request):
    student=Student.objects.all()
    serializer=StudentSerializer(student,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def studentCreate(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def studentUpdate(request,pk):
    student=Student.objects.get(pk=pk)
    serializer=StudentSerializer(instance=student,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def studentDelete(request,pk):
    student=Student.objects.get(pk=pk)
    student.delete()
    return Response()

@api_view(['GET'])
def studentDetail(request,pk):
    student=Student.objects.get(pk=pk)
    serializer=StudentSerializer(student,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def checkingUserExist(request,username):
    userr=User.objects.filter(username=username).exists()
    # serializer=ClasseSerializer(classe,many=True)
    return Response({'isExist':userr})









# examEntring
@api_view(['GET'])
def examEntringList(request):
    exam=ExamEntring.objects.all()
    serializer=ExamEntringSerializer(exam,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def examEntringCreate(request):
    serializer=ExamEntringSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def examEntringUpdate(request,pk):
    exam=ExamEntring.objects.get(pk=pk)
    serializer=ExamEntringSerializer(instance=exam,data=request.data,partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def examEntringDelete(request,pk):
    exam=ExamEntring.objects.get(pk=pk)
    exam.delete()
    return Response()

@api_view(['GET'])
def examEntringDetail(request,pk):
    exam=ExamEntring.objects.get(pk=pk)
    serializer=ExamEntringSerializer(exam,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def checingExamEntringExist(request,examType,academicYear):
    classe=ExamEntring.objects.filter(examType=examType,academicYear=academicYear).exists()
    # serializer=ClasseSerializer(classe,many=True)
    return Response({'isExist':classe})

@api_view(['GET'])
def thisYearExamEntringList(request,pk):
    # lastAcademicYear=AcademicYear.objects.last()
    # print(lastAcademicYear)
    # print(registredAcademicYear)
    examE=ExamEntring.objects.filter(academicYear=pk)
    serializer=ExamEntringSerializer(examE,many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def thisYearExamEntringId(request,examType,academicYear):
#     isExist=ExamEntring.objects.filter(academicYear=academicYear).filter(examType=examType).exists()
#     print(isExist)
#     if isExist:
#         examE=ExamEntring.objects.filter(academicYear=academicYear).get(examType=examType)
#         serializer=ExamEntringSerializer(examE,many=False)
#     return Response({'exist':isExist,'data':serializer.data} )



# examTypes
@api_view(['GET'])
def examTypeList(request):
    exam=ExamType.objects.all()
    serializer=ExamTypeSerializer(exam,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def examTypeCreate(request):
    serializer=ExamTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def examTypeUpdate(request,pk):
    exam=ExamType.objects.get(pk=pk)
    serializer=ExamTypeSerializer(instance=exam,data=request.data,partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def examTypeDelete(request,pk):
    exam=ExamType.objects.get(pk=pk)
    exam.delete()
    return Response()

@api_view(['GET'])
def examTypeDetail(request,pk):
    exam=ExamType.objects.get(pk=pk)
    serializer=ExamTypeSerializer(exam,many=False)
    return Response(serializer.data)



# result
@api_view(['GET'])
def resultList(request):
    result=Result.objects.all()
    serializer=ResultSerializer(result,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def resultCreate(request):
    serializer=ResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def resultUpdate(request,pk):
    result=Result.objects.get(pk=pk)
    serializer=ResultSerializer(instance=result,data=request.data,partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def resultDelete(request,pk):
    result=Result.objects.get(pk=pk)
    result.delete()
    return Response()

@api_view(['GET'])
def resultDetail(request,pk):
    result=Result.objects.get(pk=pk)
    serializer=ResultSerializer(result,many=False)
    return Response(serializer.data)











# marks
@api_view(['GET'])
def marksList(request):
    marks=Marks.objects.all()
    serializer=MarksSerializer(marks,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def marksCreate(request):
    serializer=MarksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def marksUpdate(request,pk):
    marks=Marks.objects.get(pk=pk)
    serializer=MarksSerializer(instance=marks,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def marksDelete(request,pk):
    marks=Marks.objects.get(pk=pk)
    marks.delete()
    return Response()

@api_view(['GET'])
def marksDetail(request,pk):
    marks=Marks.objects.get(pk=pk)
    serializer=MarksSerializer(marks,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def stdMarksList(request,pk,cls):
    marks=Marks.objects.filter(studentId=pk).filter(stdClasse=cls).order_by('subjectId')
    serializer=MarksSerializer(marks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def thisClasseMarksList(request,pk):
    marks=Marks.objects.filter(stdClasse=pk)
    serializer=MarksSerializer(marks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def thisSubjectMarks(request,examEntring,subjectId,studentId,stdClasse):
    mark=''
    serializer=''
    try:
        mark=Marks.objects.filter(studentId=studentId).filter(stdClasse=stdClasse).filter(subjectId=subjectId).get(theExamId=examEntring)
        serializer=MarksSerializer(mark,many=False)
        return Response({'created':True,'data':serializer.data})
    except:
        serializer={'marks':0}
        return Response({'created':False,'data':serializer})
    



def examUplading(request):
    # examFlle = xlrd.open_workbook("book12.xls")
    # sheet = examFlle.sheet_by_name("Sheet1")
    # theClass=sheet.cell(3,1)
    # # ncols

    # for stdId in range(4, sheet.nrows):
    #     for marks in range(3,sheet.ncols):
    #         print('name '+str(sheet.cell(stdId,1).value)+' marks:'+str(sheet.cell(stdId,marks).value))
    return Response({})











# user 
@api_view(['GET'])
def examEntringFilesList(request):
    user=ExamEntringFiles.objects.all()
    serializer=ExamEntringFilesSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['POST','GET'])
def examEntringFilesCreate(request):
    serializer=ExamEntringFilesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['POST'])
def examEntringFilesUpdate(request,pk):
    user=ExamEntringFiles.objects.get(pk=pk)
    serializer=ExamEntringFilesSerializer(instance=user,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def examEntringFilesDelete(request,pk):
    theUser=ExamEntringFiles.objects.get(pk=pk)
    theUser.delete()
    return Response()

@api_view(['GET'])
def examEntringFilesDetail(request,pk):
    user=ExamEntringFiles.objects.get(pk=pk)
    serializer=ExamEntringFilesSerializer(user,many=False)
    return Response(serializer.data)



