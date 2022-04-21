from django.urls import path
from . import views
urlpatterns = [

    path('dash-info/',views.dashInfo),
    # user request
    path('user-list/',views.userList),
    path('user-create/',views.userCreate),
    path('user-update/<str:pk>/',views.userUpdate),
    path('user-delete/<str:pk>/',views.userDelete),
    path('user-detail/<str:pk>/',views.userDetail),
    path('user-password-format/<str:pk>/',views.passwordFormat),


    # boosaska request
    path('academicYear-list/',views.academicYearList),
    path('academicYear-create/',views.academicYearCreate),
    path('academicYear-update/<str:pk>/',views.academicYearUpdate),
    path('academicYear-delete/<str:pk>/',views.academicYearDelete),
    path('academicYear-detail/<str:pk>/',views.academicYearDetail),

    # subject
    path('subject-list/',views.subjectList),
    path('subject-create/',views.subjectCreate),
    path('subject-update/<str:pk>/',views.subjectUpdate),
    path('subject-delete/<str:pk>/',views.subjectDelete),
    path('subject-detail/<str:pk>/',views.subjectDetail),


    # students
    path('student-list/',views.studentList),
    path('student-create/',views.studentCreate),
    path('student-update/<str:pk>/',views.studentUpdate),
    path('student-delete/<str:pk>/',views.studentDelete),
    path('student-detail/<str:pk>/',views.studentDetail),    
    path('checkingUserExist/<str:username>/',views.checkingUserExist), 

    # classes
    path('classe-list/',views.classeList),
    path('classe-create/',views.classeCreate),
    path('classe-update/<str:pk>/',views.classeUpdate),
    path('classe-delete/<str:pk>/',views.classeDelete),
    path('classe-detail/<str:pk>/',views.classeDetail),
    path('classe-subjects/<str:pk>/',views.classeSubjects),
    path('checkingClassExist/<str:className>/<str:classRaqam>/<int:academicYear>/',views.checkingClassExist),
    path('getStudentsForThisClass/<str:pk>/',views.studentsForThisClass),


    # exam
    path('examEntring-list/',views.examEntringList),
    path('examEntring-create/',views.examEntringCreate),
    path('examEntring-update/<str:pk>/',views.examEntringUpdate),
    path('examEntring-delete/<str:pk>/',views.examEntringDelete),
    path('examEntring-detail/<str:pk>/',views.examEntringDetail),
    path('checingExamEntringExist/<int:examType>/<int:academicYear>/',views.checingExamEntringExist),
    path('this-year-examEntring-list/<str:pk>/',views.thisYearExamEntringList),
    # path('this-year-examentring-id/<str:examType>/<str:academicYear>/',views.thisYearExamEntringId),

    # exam
    path('examType-list/',views.examTypeList),
    path('examType-create/',views.examTypeCreate),
    path('examType-update/<str:pk>/',views.examTypeUpdate),
    path('examType-delete/<str:pk>/',views.examTypeDelete),
    path('examType-detail/<str:pk>/',views.examTypeDetail),



    # result
    path('result-list/',views.resultList),
    path('result-create/',views.resultCreate),
    path('result-update/<str:pk>/',views.resultUpdate),
    path('result-delete/<str:pk>',views.resultDelete),
    path('result-detail/<str:pk>/',views.resultDetail),



    # marks
    path('marks-list/',views.marksList),
    path('marks-create/',views.marksCreate),
    path('marks-update/<str:pk>/',views.marksUpdate),
    path('marks-delete/<str:pk>',views.marksDelete),
    path('marks-detail/<str:pk>/',views.marksDetail),
    path('std-marks-list/<str:pk>/<str:cls>/',views.stdMarksList),
    path('this-class-marks-list/<str:pk>/',views.thisClasseMarksList),
    path('this-subject-mark/<str:examEntring>/<str:subjectId>/<str:studentId>/<str:stdClasse>/',views.thisSubjectMarks),
    



    # upload exams
    path('examFileUpload/',views.examUplading),







    # user request
    path('examentringFiles-list/',views.examEntringFilesList),
    path('examentringFiles-create/',views.examEntringFilesCreate),
    path('examentringFiles-update/<str:pk>/',views.examEntringFilesUpdate),
    path('examentringFiles-delete/<str:pk>/',views.examEntringFilesDelete),
    path('examentringFiles-detail/<str:pk>/',views.examEntringFilesDetail),
    
    
]