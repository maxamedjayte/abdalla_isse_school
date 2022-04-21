function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
async function getCurrentClassSubjects(pk) {
    var thisClassSubjects
    await fetch('/api/classe-detail/' + pk + '/').then((resp) => resp.json()).then(function (classeResp) {

        thisClassSubjects = classeResp


    })
    return thisClassSubjects
}
async function delArdayga(id) {

    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Ardaygaan ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/user-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Garaysay Ardaygaan", {
                        icon: "success",
                    });
                    location.reload()
                }
            });

        }




    });

}
function delClass(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Fasalkaan ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            fetch('/api/classe-delete/' + id + '/', {
                method: 'DELETE',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
            }).then((response) => {

                swal("Waad Delete Garaysay Fasalkaan", {
                    icon: "success",
                });
                location.reload()


            })
        }
    });

}

async function isThereOneExam(stdId) {
    var isOneExam = false
    return isOneExam;
}
async function getSubjectInfo(subId) {
    var subjectInfo
    await fetch('/api/subject-detail/' + subId + '/').then((resp) => resp.json()).then(function (subjectResp) {
        subjectInfo = subjectResp

    })
    return subjectInfo
}

async function getClassInfo(classId) {
    var classInfo
    await fetch('/api/classe-detail/' + classId + '/').then((resp) => resp.json()).then(function (classeResp) {
        classInfo = classeResp

    })
    return classInfo
}


async function getSubjectInfo(subId) {
    var subjectInfo
    await fetch('/api/subject-detail/' + subId + '/').then((resp) => resp.json()).then(function (subjectResp) {
        subjectInfo = subjectResp

    })
    return subjectInfo
}




async function getSchoolExams() {
    var schoolExams
    await fetch('/api/examType-list/').then((resp) => resp.json()).then(function (examTypeResp) {

        schoolExams = examTypeResp

    })
    return schoolExams
}


async function thisYearExamEntring(academicYear) {
    var examEntring
    await fetch('/api/this-year-examEntring-list/' + academicYear + '').then((resp) => resp.json()).then(async function (theExamEntringRes) {
        examEntring = theExamEntringRes
    })
    return examEntring
}

function delImt(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Galida Imtixaanka ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            fetch('/api/examEntring-delete/' + id + '/', {
                method: 'DELETE',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
            }).then((response) => {

                swal("Imtixaankan Waad Bixisay", {
                    icon: "success",
                });
                location.reload()

            })
        }
    });
}
function delSubj(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Maadada ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            fetch('/api/subject-delete/' + id + '/', {
                method: 'DELETE',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
            }).then((response) => {

                swal("Maadadaan Waad Bixisay", {
                    icon: "success",
                });
                location.reload()

            })
        }
    });
}
function delImtType(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Noca Imtiaankan ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            fetch('/api/examType-delete/' + id + '/', {
                method: 'DELETE',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
            }).then((response) => {

                swal("Waad Delete Garaysay Imtixanak", {
                    icon: "success",
                });
                location.reload()


            })
        }
    });
}


function delAcademic(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Deleting Sanad-Dugisyeedka ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            fetch('/api/academicYear-delete/' + id + '/', {
                method: 'DELETE',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
            }).then((response) => {
                console.log(response)
                swal("Sanad-Dugsiyeedkan Waad Bixisay", {
                    icon: "success",
                });
                location.reload()

            })
        }
    });
}

async function updateClassStd() {
    await $.ajax({
        url: '/assingStudent/',
        method: 'GET',
        success: function (res) {
        }
    })
}


async function activeThisAcademicYear(academicYearId) {
    var academicYearsData
    await $.ajax({
        url: '/api/academicYear-list/',
        method: 'GET',
        success: function (academicYearsResp) {
            academicYearsData=academicYearsResp
        }
    });
    for(var theAcademicYear of academicYearsData){
        if (theAcademicYear.id==academicYearId) {
            await $.ajax({
                method: 'POST',
                url: '/api/academicYear-update/' + theAcademicYear.id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                data: JSON.stringify({
                    'isCurrentAcademicYear': true,
                }),
                success: function (res) {
                   console.log(res)
                }
            })
        }else{
            await $.ajax({
                method: 'POST',
                url: '/api/academicYear-update/' + theAcademicYear.id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                data: JSON.stringify({
                    'isCurrentAcademicYear': false,
                }),
                success: function (res) {
                   console.log(res)
                }
            })
        }

    }
    swal("Sanad-Dugsiyeedkan Waa La Active Greeyey", {
        icon: "success",
    });
    location.reload()
}


async function addClassToAccessed(newClassId,studentId) {
    var theStdAccesedClasses
    await $.ajax({
        url: '/api/student-detail/'+studentId+'/',
        method: 'GET',
        success: function (theStdAccesedClassesResp) {
            theStdAccesedClasses=theStdAccesedClassesResp.accessedClasses
        }
    });
    theStdAccesedClasses.push(newClassId)
    await $.ajax({
        method: 'POST',
        url: '/api/student-update/' + studentId + '/',
        headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
        data: JSON.stringify({
            'accessedClasses': theStdAccesedClasses,
        }),
        success: function (res) {
           console.log(res)
        }
    })
}


async function getSchoolExams() {
    var schoolExams
    await fetch('/api/examType-list/').then((resp) => resp.json()).then(function (examTypeResp) {

        schoolExams = examTypeResp

    })
    return schoolExams
}

async function checkIfThisClassIsExist(classRaqam, classe, clsAcademicYear) {
    var isExist = false
    await fetch('/api/checkingClassExist/' + classe + '/' + classRaqam + '/' + clsAcademicYear + '/').then((resp) => resp.json()).then(function (classeResp) {
        if (classeResp.isExist == true) {
            isExist = true
        } else {
            isExist = false
        }

    })
    return isExist
}


async function changeClassStatus(id,status) {
    $.ajax({
        method: 'POST',
        url: '/api/classe-update/' + id + '/',
        headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
        data: JSON.stringify({
            'status': status=='0'?false:true,
        }),
        success: function (classResp) {
            if (classResp.status == 'success') {
                swal("Waa Savegreeyey Isbadalki ", {
                    icon: "success"
                });

                location.reload()
            }
        }
    })
}


function delFile(id) {
    swal({
        title: "Ma Hubtaa Inaad?",
        text: "Delete Garyso Filekaan ",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then(async (willDelete) => {
        if (willDelete) {
            $.ajax({
                method: 'DELETE',
                url: '/api/examentringFiles-delete/' + id + '/',
                headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Content-type': "application/json" },
                success: function (stdDelResp) {
                    swal("Waad Delete Garaysay Filka", {
                        icon: "success",
                    });
                    location.reload()
                }
            });

        }




    });
}