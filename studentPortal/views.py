from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from api.models import Student
# Create your views here.
def loginPage(request):
    status=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/std/portal/')
        else:
            status='Usernameka ama Passwordka ayaa qaldan'
    data={
        'status':status
    }
    return render(request,'std-exam-portal/login.html',data)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/std/login/')


# student porta
@login_required(login_url='/std/login/')
def stdPortalDashboard(request):
    if Student.objects.filter(studentId=request.user.username).exists():
        userId=Student.objects.get(studentId=request.user.username).pk
        return render(request,'std-exam-portal/exam-portal.html',{'pk':userId})
    else:
        return HttpResponseRedirect('/std/login/')

def examResultTr(request):
    if Student.objects.filter(studentId=request.user.username).exists():
        userId=Student.objects.get(studentId=request.user.username).pk
        return render(request,'std-exam-portal/examResutlTr.html',{'pk':userId})
    else:
        return HttpResponseRedirect('/std/login/')

def examResultClasse(request):
    if Student.objects.filter(studentId=request.user.username).exists():
        userId=Student.objects.get(studentId=request.user.username).pk
        return render(request,'std-exam-portal/examResutlClasse.html',{'pk':userId})
    else:
        return HttpResponseRedirect('/std/login/')