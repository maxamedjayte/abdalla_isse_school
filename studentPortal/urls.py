from django.urls import path
from . import views
urlpatterns = [
    # student portal
    path('login/',views.loginPage),
    path('logout/',views.logoutPage),
    path('',views.stdPortalDashboard),
    path('portal/',views.stdPortalDashboard),
    path('exam_result_tr/',views.examResultTr),
    path('exam_result_classe/',views.examResultClasse)
]