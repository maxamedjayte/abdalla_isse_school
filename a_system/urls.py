from django.urls import path
from . import views
urlpatterns = [



    path('adminlogin/',views.adminLoginPage),
    path('adminlogout/',views.adminLogoutPage),

    # 
    path('',views.indexWeb),
    
    # path('login/',views.loginPage),
    # path('logout/',views.logoutPage),
    
    path('school-admin/',views.dashboard),
    # student 
    path('ardada/',views.studentRegManag),
    path('xogtaArdayda/',views.xogtaArdayda),
    path('xogtaArdaygaan/<str:pk>/',views.thisStdInfo),

    # class
    path('fasalada/',views.classRegMang),
    path('xogtaFasalada/',views.xogtaFasalada),

    # sanad dugsiyedka
    path('academic_year/',views.sanadDugsiyedkaRegMang),

    # subjects
    path('subjects/',views.subjects),

    # examEntring
    path('imtixaanada/',views.imtixanRegMang),

    # examTypes
    path('noocaImtixaanka/',views.examTypeRegMang),


    # galida imtixaanka
    path('examEntringClasses/',views.examEntringShow),

    path('examEntringStd/<str:pk>/',views.examEntringStdShow),

    path('studentExamMang/<str:pk>/',views.studentExamMang),


    # invoice
    path('exam-class/<str:pk>/',views.examClassInvoice),
    
    # test
    path('examFileExporting/<str:pk>/',views.examFileExporting),

    path('examFileUploadtest/',views.examFileUploadtest),
    

    path('assingStudent/',views.assaignEachClassStdCount),
    path('class-transfer/',views.classTransfer),


    path('exam-file-upload/',views.examFileUpload),

    path('exam-files/',views.examFiles)



]