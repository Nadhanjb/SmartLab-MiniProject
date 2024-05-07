from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from smartlab_app.models import *
from datetime import datetime



def main(request):
    return render(request,'index.html')

def login(request):
    return render(request,'logindex.html')




def logout(request):
    auth.logout(request)
    return render(request,'logindex.html')
def logincode(request):

    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=uname,password=pswd)
        if ob.type == 'admin':
            ob1 = auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid']=ob.id
            return HttpResponse('''<script>alert('Welcome to Admin Home');window.location="/ahome"</script>''')
        elif ob.type == 'staff':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
                obb=staff_table.objects.get(LOGIN__id=ob.id)
                request.session['name']=obb.name
                request.session['img']=obb.photo.url
            return HttpResponse('''<script>alert('Welcome to Staff Home');window.location="/staffhome"</script>''')
        elif ob.type == 'labassistant':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
                o=lab_assistant_table.objects.get(LOGIN__id=ob.id)
                request.session['n']=o.name
                request.session['img']=o.photo.url
            return HttpResponse('''<script>alert('Welcome to lab assistant Home');window.location="/labassistanthome"</script>''')
        elif ob.type == 'student':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
                oo=student_table.objects.get(LOGIN__id=ob.id)
                request.session['sn']=oo.fname+" "+oo.lname
                request.session['img']=oo.photo.url

            return HttpResponse('''<script>alert('Welcome to student Home');window.location="/studenthome"</script>''')
        else:
            return HttpResponse('''<script>alert('invalid user');window.location="/login"</script>''')
    except:
        return HttpResponse('''<script>alert('Invalid user');window.location="/login"</script>''')

@login_required(login_url='/')
def ahome(request):
    return render(request, 'Admin/adminindex.html')


@login_required(login_url='/')
def mngdept(request):
    ob=dept_table.objects.all()
    return render(request, 'Admin/Department.html',{'val':ob})

@login_required(login_url='/')
def adddept(request):
    return render(request, 'Admin/add dept.html')

@login_required(login_url='/')
def add_dept_action(request):
    dep = request.POST['textfield']
    details = request.POST['textfield2']
    dept_obj = dept_table()
    dept_obj.dept_name = dep
    dept_obj.details = details
    dept_obj.save()
    return HttpResponse('''<script>window.location="/mngdept#about"</script>''')


@login_required(login_url='/')
def edit_dept(request, dept_id):
    request.session['dept_id'] = dept_id
    ob = dept_table.objects.get(id=dept_id)
    return render(request, 'Admin/edit dept.html', {'val': ob})

@login_required(login_url='/')
def edit_dept_action(request):
    dept_obj = dept_table.objects.get(id=request.session['dept_id'])
    dep = request.POST['textfield']
    details = request.POST['textfield2']
    dept_obj.dept_name = dep
    dept_obj.details = details
    dept_obj.save()
    return HttpResponse('''<script>window.location="/mngdept#about"</script>''')


@login_required(login_url='/')
def dlt_depart(request,id):
    ob=dept_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mngdept#about"</script>''')

@login_required(login_url='/')
def mngcourse(request):
    o=dept_table.objects.all()
    ob = course_table.objects.all()
    ob1= course_table.objects.all()
    return render(request, 'Admin/Course.html',{'val':ob,'val1':o,'val2':ob1})

@login_required(login_url='/')
def addcourse(request):
    dept_obj = dept_table.objects.all()
    return render(request, 'Admin/add course.html', {'dept_obj': dept_obj})


@login_required(login_url='/')
def add_course_action(request):
    course = request.POST['textfield']
    details =request.POST['textarea']
    dept = request.POST['select']
    sem = request.POST['sem']
    course_obj =course_table()
    course_obj.course =course
    course_obj.details =details
    course_obj.sem =sem
    course_obj.DEPARTMENT = dept_table.objects.get(id=dept)
    course_obj.save()
    return HttpResponse('''<script>window.location="/mngcourse#about"</script>''')

@login_required(login_url='/')
def edit_course(request, course_id):
    request.session['course_id'] = course_id
    ob = course_table.objects.get(id=course_id)
    ob1=dept_table.objects.all()
    return render(request, 'Admin/edit course.html', {'val': ob, 'dept_obj': ob1})

@login_required(login_url='/')
def edit_course_action(request):
    course_obj = course_table.objects.get(id=request.session['course_id'])
    course = request.POST['textfield']
    details =request.POST['textarea']
    dept = request.POST['select']
    sem = request.POST['sem']
    course_obj.course =course
    course_obj.details =details
    course_obj.sem =sem
    course_obj.DEPARTMENT = dept_table.objects.get(id=dept)
    course_obj.save()
    return HttpResponse('''<script>window.location="/mngcourse#about"</script>''')

@login_required(login_url='/')
def dlt_course(request,id):
    ob=course_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mngcourse#about"</script>''')
@login_required(login_url='/')
def upgrade(request,id):
    ob=course_table.objects.get(id=id)
    total=ob.sem
    o=student_table.objects.filter(COURSE__id=id)
    if len(o)==0:
        return HttpResponse('''<script>window.location="/mngcourse#about"</script>''')
    else:
        s=student_table.objects.filter(COURSE__id=id)
        for i in s:
            lob=student_table.objects.filter(COURSE__id=id)
            for i in lob:
                if i.semester!='Completed':
                    if i.semester!=str(total):
                        i.semester =int(i.semester)+1
                        i.save()
                    else:
                        i.semester="Completed"
                        i.save


        return HttpResponse('''<script>window.location="/mngcourse#about"</script>''')









@login_required(login_url='/')
def mngcourse_search(request):
    o = dept_table.objects.all()
    oo = course_table.objects.all()
    dep = request.POST['select']
    course = request.POST['select1']
    print(dep,course,"00")
    if (dep != "" and course != ""):
        ob = course_table.objects.filter(DEPARTMENT__id=dep, id=course)
        return render(request, 'Admin/Course.html', {'val2': ob, 'val1': o, 'val': oo,'dep': int(dep),'cou':int(course)})
    elif dep != "":
        ob = course_table.objects.filter(DEPARTMENT__id=dep)
        return render(request, 'Admin/Course.html', {'val2': ob, 'val1': o, 'val': oo, 'dep': int(dep)})
    else:
        print("hiiii")
        ob = course_table.objects.filter(id=course)
        return render(request, 'Admin/Course.html', {'val2': ob, 'val1': o, 'val': oo,'cou':int(course)})





@login_required(login_url='/')
def mnglabsubj(request):
    ob = labsubject_table.objects.all()
    o=course_table.objects.all()
    return render(request, 'Admin/subject.html',{'val':ob,'val1':o})


@login_required(login_url='/')
def addlabsubj(request):
    ob = course_table.objects.all()
    return render(request, 'Admin/add subject.html',{'val':ob})


@login_required(login_url='/')
def add_labsubj_action(request):
    subject = request.POST['textfield']
    course = request.POST['select']
    syllabus= request.POST['textarea']
    subject_obj =labsubject_table()
    subject_obj.subject =subject
    subject_obj.syllabus =syllabus
    subject_obj.COURSE = course_table.objects.get(id=course)
    subject_obj.save()
    return HttpResponse('''<script>window.location="/mnglabsubj#about"</script>''')


@login_required(login_url='/')
def edit_labsub(request, id):
    ob=labsubject_table.objects.get(id=id)
    request.session['subj_id']=id
    o=course_table.objects.all()
    return render(request, 'Admin/edit subject.html',{'val':ob,'val1':o})


@login_required(login_url='/')
def edit_labsubj_action(request):
    subject_obj = labsubject_table.objects.get(id=request.session['subj_id'])
    subject = request.POST['textfield']
    course = request.POST['select']
    syllabus = request.POST['textarea']
    subject_obj.subject = subject
    subject_obj.syllabus = syllabus
    subject_obj.COURSE = course_table.objects.get(id=course)
    subject_obj.save()
    return HttpResponse('''<script>window.location="/mnglabsubj#about"</script>''')


@login_required(login_url='/')
def dlt_labsub(request,id):
    ob=labsubject_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mnglabsubj#about"</script>''')


@login_required(login_url='/')
def mnglabsubj_search(request):
    c=request.POST['select']
    ob = labsubject_table.objects.filter(COURSE__id=c)
    o=course_table.objects.all()
    return render(request, 'Admin/subject.html',{'val':ob,'val1':o,"c":int(c)})


@login_required(login_url='/')
def mngstaff(request):
    ob =staff_table.objects.all()
    for i in ob:
        i.qualification=i.qualification.split(",")
    cob=course_table.objects.all()
    return render(request, 'Admin/staff.html',{'val':ob,"val1":cob})


@login_required(login_url='/')
def addstaff(request):
    ob = dept_table.objects.all()
    ob1=course_table.objects.all()
    return render(request, 'Admin/add staff.html',{'val':ob, 'val1':ob1})


@login_required(login_url='/')
def add_staff_action(request):
    name = request.POST['textfield']
    gender= request.POST['radiobutton']
    dob = request.POST['textfield2']
    place = request.POST['textfield3']
    pin = request.POST['textfield4']
    post = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    qualification = request.POST['textarea']
    programming_lang =",".join(request.POST.getlist('checkbox'))
    course = request.POST['select2']
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    username=request.POST['textfield8']
    password=request.POST['textfield9']



    ox=staff_table.objects.filter(email = email)
    if len(ox) == 0:

        oy = staff_table.objects.filter(phone = phone)
        if len(oy) == 0:


                ob = login_table()
                ob.username = username
                ob.password = password
                ob.type = 'staff'
                ob.save()
                staff_obj = staff_table()
                staff_obj.name = name
                staff_obj.gender = gender
                staff_obj.dob = dob
                staff_obj.place = place
                staff_obj.pin = pin
                staff_obj.post = post
                staff_obj.phone = phone
                staff_obj.email = email
                staff_obj.qualification = qualification
                staff_obj.programming_lang = programming_lang
                staff_obj.COURSE = course_table.objects.get(id=course)
                staff_obj.photo = fsave
                staff_obj.LOGIN = ob
                staff_obj.save()
                return HttpResponse('''<script>window.location="/mngstaff#about"</script>''')
        else:

            return HttpResponse(
                '''<script>alert("This phone was already exist so doesnt use it again");window.location="/addstaff#about"</script>''')

    else:
        return HttpResponse('''<script>alert("This email was already exist so doesnt use it again");window.location="/addstaff#about"</script>''')



@login_required(login_url='/')
def editstaff(request,staff_id):
    request.session['staff_id'] = staff_id
    ob1=course_table.objects.all()
    ob2=staff_table.objects.get(id=staff_id)
    return render(request, 'Admin/edit staff.html',{ 'val1':ob1,'val2':ob2 ,"d":str(ob2.dob)})


@login_required(login_url='/')
def edit_staff_action(request):
    try:
        staff_obj = staff_table.objects.get(id=request.session['staff_id'])
        name = request.POST['textfield']
        gender= request.POST['radiobutton']
        dob = request.POST['textfield2']
        place = request.POST['textfield3']
        pin = request.POST['textfield4']
        post = request.POST['textfield5']
        phone = request.POST['textfield6']
        email = request.POST['textfield7']
        qualification = request.POST['textarea']
        programming_lang = ','.join(request.POST.getlist('checkbox'))
        course = request.POST['select2']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        staff_obj.name =name
        staff_obj.gender =gender
        staff_obj.dob=dob
        staff_obj.place=place
        staff_obj.pin=pin
        staff_obj.post=post
        staff_obj.phone=phone
        staff_obj.email=email
        staff_obj.qualification=qualification
        staff_obj.programming_lang=programming_lang
        staff_obj.COURSE =course_table.objects.get(id=course)
        staff_obj.photo=fsave
        staff_obj.save()
        return HttpResponse('''<script>window.location="/mngstaff#about"</script>''')
    except:
        staff_obj = staff_table.objects.get(id=request.session['staff_id'])
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield2']
        place = request.POST['textfield3']
        pin = request.POST['textfield4']
        post = request.POST['textfield5']
        phone = request.POST['textfield6']
        email = request.POST['textfield7']
        qualification = request.POST['textarea']
        programming_lang = ','.join(request.POST.getlist('checkbox'))
        course = request.POST['select2']
        # photo = request.FILES['file']
        # fs = FileSystemStorage()
        # fsave = fs.save(photo.name, photo)
        staff_obj.name = name
        staff_obj.gender = gender
        staff_obj.dob = dob
        staff_obj.place = place
        staff_obj.pin = pin
        staff_obj.post = post
        staff_obj.phone = phone
        staff_obj.email = email
        staff_obj.qualification = qualification
        staff_obj.programming_lang = programming_lang
        staff_obj.COURSE = course_table.objects.get(id=course)
        # staff_obj.photo = fsave
        staff_obj.save()
        return HttpResponse('''<script>window.location="/mngstaff"</script>''')


@login_required(login_url='/')
def dlt_staff(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mngstaff#about"</script>''')


@login_required(login_url='/')
def mng_staff_sch(request):
    n = request.POST['select']
    if n == "ALL":

        ob=staff_table.objects.all()
        cob = course_table.objects.all()
        for i in ob:
            i.qualification = i.qualification.split(",")
        cob = course_table.objects.all()
        return render(request, 'Admin/staff.html',{'val':ob,"val1":cob,"s":str(n)})
    else:
        ob=staff_table.objects.filter(COURSE__id=n)
        cob = course_table.objects.all()
        for i in ob:
            i.qualification = i.qualification.split(",")
        cob = course_table.objects.all()
        return render(request, 'Admin/staff.html',{'val':ob,"val1":cob,"s":int(n)})


@login_required(login_url='/')
def mnglabassist(request):
    ob = lab_assistant_table.objects.all()
    for i in ob:
        i.qualification = i.qualification.split(",")
    return render(request, 'Admin/lab assis.html',{'val':ob})


@login_required(login_url='/')
def addlabassist(request):
    return render(request, 'Admin/add lab assi.html')

@login_required(login_url='/')
def add_labassi_action(request):
    name = request.POST['textfield']
    gender = request.POST['radiobutton']
    dob = request.POST['textfield2']
    phone = request.POST['textfield3']
    email = request.POST['textfield4']
    place = request.POST['textfield5']
    pin = request.POST['textfield6']
    post = request.POST['textfield7']
    qualification = request.POST['textarea']
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    username=request.POST['textfield8']
    password=request.POST['textfield9']

    ox = lab_assistant_table.objects.filter(email=email)
    if len(ox) == 0:

        oy = lab_assistant_table.objects.filter(phone=phone)
        if len(oy) == 0:


            ob=login_table()
            ob.username=username
            ob.password=password
            ob.type = 'labassistant'
            ob.save()
            labassis_obj = lab_assistant_table()
            labassis_obj.name = name
            labassis_obj.gender = gender
            labassis_obj.dob = dob
            labassis_obj.place = place
            labassis_obj.pin = pin
            labassis_obj.post = post
            labassis_obj.phone = phone
            labassis_obj.email = email
            labassis_obj.qualification = qualification
            labassis_obj.photo = fsave
            labassis_obj.LOGIN = ob
            labassis_obj.save()
            return HttpResponse('''<script>window.location="/mnglabassist#about"</script>''')

        else:

            return HttpResponse(
                '''<script>alert("This phone was already exist so doesnt use it again");window.location="/addlabassist#about"</script>''')

    else:
        return HttpResponse('''<script>alert("This email was already exist so doesnt use it again");window.location="/addlabassist#about"</script>''')


@login_required(login_url='/')
def edit_lab_assi(request,id):
    request.session['labassi_id'] = id
    ob=lab_assistant_table.objects.get(id=id)
    return render(request, 'Admin/edit lab assi.html',{"val":ob,'dt':str(ob.dob)})



@login_required(login_url='/')
def edit_labassi_action(request):
    try:
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield2']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        place = request.POST['textfield5']
        pin = request.POST['textfield6']
        post = request.POST['textfield7']
        qualification = request.POST['textarea']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        labassis_obj = lab_assistant_table.objects.get(id=request.session['labassi_id'])
        labassis_obj.name = name
        labassis_obj.gender = gender
        labassis_obj.dob = dob
        labassis_obj.place = place
        labassis_obj.pin = pin
        labassis_obj.post = post
        labassis_obj.phone = phone
        labassis_obj.email = email
        labassis_obj.qualification = qualification
        labassis_obj.photo = fsave
        labassis_obj.save()
        return HttpResponse('''<script>window.location="/mnglabassist#about"</script>''')
    except:
        name = request.POST['textfield']
        gender = request.POST.get('radiobutton')
        dob = request.POST['textfield2']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        place = request.POST['textfield5']
        pin = request.POST['textfield6']
        post = request.POST['textfield7']
        qualification = request.POST['textarea']
        labassis_obj = lab_assistant_table.objects.get(id=request.session['labassi_id'])
        labassis_obj.name = name
        labassis_obj.gender = gender
        labassis_obj.dob = dob
        labassis_obj.place = place
        labassis_obj.pin = pin
        labassis_obj.post = post
        labassis_obj.phone = phone
        labassis_obj.email = email
        labassis_obj.qualification = qualification
        labassis_obj.save()
        return HttpResponse('''<script>window.location="/mnglabassist#about"</script>''')



@login_required(login_url='/')
def dlt_labassi(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mnglabassist#about"</script>''')


@login_required(login_url='/')
def mnglabassi_search(request):
    c=request.POST['textfield']
    ob = lab_assistant_table.objects.filter(name__icontains=c)
    for i in ob:
        i.qualification = i.qualification.split(",")
    return render(request, 'Admin/lab assis.html',{'val':ob,'c':c})


@login_required(login_url='/')
def mngstud(request):
    ob = student_table.objects.all()
    for i in ob:
        i.qualification=i.qualification.split(",")
    cob = course_table.objects.all()
    dob=dept_table.objects.all()
    return render(request, 'Admin/student.html', {'val2': ob, "val1": cob,"val":dob})


@login_required(login_url='/')
def addstud(request):
    ob1 = course_table.objects.all()
    return render(request, 'Admin/add student.html',{"val1": ob1})


@login_required(login_url='/')
def addstud_action(request):

    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    gender = request.POST['radiobutton']
    dob = request.POST['textfield6']
    place = request.POST['textfield3']
    pin = request.POST['textfield4']
    post = request.POST['textfield5']
    phone = request.POST['textfield9']
    email = request.POST['textfield8']
    qualification = request.POST['textfield12']
    course = request.POST['select2']
    semester=request.POST['select3']
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    username = request.POST['textfield10']
    password = request.POST['textfield11']
    ox=student_table.objects.filter(email=email)
    if len(ox)==0:
        oy = student_table.objects.filter(phone=phone)
        if len(oy) == 0:

            ob = login_table()
            ob.username = username
            ob.password = password
            ob.type = 'student'
            ob.save()
            stud_obj = student_table()
            stud_obj.fname = fname
            stud_obj.lname = lname
            stud_obj.gender = gender
            stud_obj.dob = dob
            stud_obj.place = place
            stud_obj.pin = pin
            stud_obj.post = post
            stud_obj.phone = phone
            stud_obj.email = email
            stud_obj.qualification = qualification
            stud_obj.semester = semester
            stud_obj.COURSE = course_table.objects.get(id=course)
            stud_obj.photo = fsave
            stud_obj.LOGIN = ob
            stud_obj.save()
            return HttpResponse('''<script>window.location="/mngstud#about"</script>''')

        else:

            return HttpResponse(
                '''<script>alert("This phone was already exist so doesnt use it again");window.location="/addstud#about"</script>''')

    else:
        return HttpResponse('''<script>alert("This email was already exist so doesnt use it again");window.location="/addstud#about"</script>''')






@login_required(login_url='/')
def edit_student(request,id):
    request.session['student_id'] = id
    ob = student_table.objects.get(id=id)
    obb=course_table.objects.all()
    return render(request, 'Admin/edit student.html', {"val": ob, 'dt': str(ob.dob),'val1':obb})


@login_required(login_url='/')
def edit_stud_action(request):
    try:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield6']
        place = request.POST['textfield3']
        pin = request.POST['textfield4']
        post = request.POST['textfield5']
        phone = request.POST['textfield9']
        email = request.POST['textfield8']
        qualification = request.POST['textfield12']
        course = request.POST['select2']
        semester = request.POST['select3']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        stud_obj = student_table.objects.get(id=request.session['student_id'])
        stud_obj.fname = fname
        stud_obj.lname = lname
        stud_obj.gender = gender
        stud_obj.dob = dob
        stud_obj.place = place
        stud_obj.pin = pin
        stud_obj.post = post
        stud_obj.phone = phone
        stud_obj.email = email
        stud_obj.qualification = qualification
        stud_obj.semester = semester
        stud_obj.COURSE = course_table.objects.get(id=course)
        stud_obj.photo = fsave
        stud_obj.save()
        return HttpResponse('''<script>window.location="/mngstud#about"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield6']
        place = request.POST['textfield3']
        pin = request.POST['textfield4']
        post = request.POST['textfield5']
        phone = request.POST['textfield9']
        email = request.POST['textfield8']
        qualification = request.POST['textfield12']
        course = request.POST['select2']
        semester = request.POST['select3']
        stud_obj = student_table.objects.get(id=request.session['student_id'])
        stud_obj.fname = fname
        stud_obj.lname = lname
        stud_obj.gender = gender
        stud_obj.dob = dob
        stud_obj.place = place
        stud_obj.pin = pin
        stud_obj.post = post
        stud_obj.phone = phone
        stud_obj.email = email
        stud_obj.qualification = qualification
        stud_obj.semester = semester
        stud_obj.COURSE = course_table.objects.get(id=course)
        stud_obj.save()
        return HttpResponse('''<script>window.location="/mngstud#about"</script>''')


@login_required(login_url='/')
def stud_search(request):
    o = dept_table.objects.all()
    oo1 = course_table.objects.all()
    dep = request.POST['select']
    course = request.POST['select2']
    semester = request.POST['select3']
    print(dep, ",", course, ",", semester, "======================")
    try:
        if dep != "" and course != "" and semester != "":
            ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester, COURSE__id=course)
            for i in ob:
                i.qualification = i.qualification.split(",")
            return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':semester,'dp':int(dep),'crs':int(course)})
        else:
            try:
                if dep != "" and (course == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':0 ,'dp':int(dep),'crs':0})
                elif course != "" and (dep == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':0,'dp':0,'crs':int(course)})
                elif semester != "" and (dep == "" and course == ''):
                    ob = student_table.objects.filter(semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':semester,'dp':0,'crs':0})
                elif (dep != "" and course != ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':0,'dp':int(dep),'crs':int(course)})
                elif dep != "" and semester != "":
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':semester,'dp':int(dep),'crs':0})
                elif semester != "" and course != "":
                    ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':semester,'dp':0,'crs':int(course)})
                else:
                    ob = student_table.objects.all()
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':0,'dp':0,'crs':0})

            except:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o,'sem':0,'dp':0,'crs':0})

    except:
        try:
            if dep != "" and (course == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o, })
            elif course != "" and (dep == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and (dep == "" and course == ''):
                ob = student_table.objects.filter(semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif (dep != "" and course != ""):
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif dep != "" and semester != "":
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and course != "":
                ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})
            else:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})

        except:
            ob = student_table.objects.all()
            for i in ob:
                i.qualification = i.qualification.split(",")
            return render(request, 'Admin/student.html', {'val2': ob, 'val1': oo1, 'val': o})

@login_required(login_url='/')
def dlt_student(request, id):
    ob = login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mngstud#about"</script>''')


@login_required(login_url='/')
def mngexam(request):
    ob = exam_table.objects.all()
    return render(request, 'Admin/Exam.html',{'val':ob})

@login_required(login_url='/')
def addexam(request):
    ob = labsubject_table.objects.all()
    ob1 = staff_table.objects.all()
    d=datetime.now().strftime("%Y-%m-%d")
    return render(request, 'Admin/add exam.html', {'val': ob, 'val1': ob1,"d":d})

@login_required(login_url='/')
def add_exam_action(request):
    exam_name = request.POST['textfield']
    subject = request.POST['select']
    details = request.POST['textarea']
    date = request.POST['textfield2']
    time = request.POST['textfield3']
    duration = request.POST['textfield4']

    staff_allotted=request.POST['select2']
    exam_obj=exam_table()
    exam_obj.exam_name=exam_name
    exam_obj.SUBJECT = labsubject_table.objects.get(id=subject)
    exam_obj.details = details
    exam_obj.date = date
    exam_obj.time = time
    exam_obj.duration = duration

    exam_obj.STAFF = staff_table.objects.get(id=staff_allotted)
    exam_obj.save()
    return HttpResponse('''<script>window.location="/mngexam#about"</script>''')

@login_required(login_url='/')
def edit_exam(request, exam_id):
    request.session['exam_id'] = exam_id
    ob=exam_table.objects.get(id=exam_id)
    ob1=labsubject_table.objects.all()
    ob2=staff_table.objects.all()
    return render(request, 'Admin/edit exam.html', {'val': ob, 'val1': ob1,'val2':ob2,'dt':str(ob.date),'t':str(ob.time)})

@login_required(login_url='/')
def edit_exam_action(request):
    exam_obj = exam_table.objects.get(id=request.session['exam_id'])
    exam_name = request.POST['textfield']
    subject = request.POST['select']
    details = request.POST['textarea']
    date = request.POST['textfield2']
    time = request.POST['textfield3']
    duration = request.POST['textfield4']
    syllabus = request.POST['textfield5']
    staff_allotted=request.POST['select2']
    exam_obj.exam_name=exam_name
    exam_obj.SUBJECT = labsubject_table.objects.get(id=subject)
    exam_obj.details = details
    exam_obj.date = date
    exam_obj.time = time
    exam_obj.duration = duration
    exam_obj.syllabus = syllabus
    exam_obj.STAFF = staff_table.objects.get(id=staff_allotted)
    exam_obj.save()
    return HttpResponse('''<script>window.location="/mngexam#about"</script>''')

@login_required(login_url='/')
def dlt_exam(request, id):
    ob = exam_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mngexam#about"</script>''')

@login_required(login_url='/')
def searchexm(request):
    dt=request.POST['dt']
    ob = exam_table.objects.filter(date=dt)
    return render(request, 'Admin/Exam.html',{'val':ob,'val1':dt})

@login_required(login_url='/')
def allocatesub_staff(request):
    ob = sub_staff_allo_table.objects.all()
    return render(request, 'Admin/subject - staff.html',{'val':ob})

@login_required(login_url='/')
def addsub_staff(request):
    obb=sub_staff_allo_table.objects.all()
    ls=[]
    for i in obb:
        ls.append(i.SUBJECT.id)
    ob = labsubject_table.objects.exclude(id__in=ls)
    ob1 = staff_table.objects.all()
    return render(request, 'Admin/add subject - staff.html',{'val':ob,'val1':ob1})

@login_required(login_url='/')
def addsub_staff_action(request):
    print(request.POST)
    name= request.POST['select']
    subject = request.POST['select2']
    ob=sub_staff_allo_table.objects.filter(STAFF__id=name,SUBJECT__id=subject)
    if len(ob) == 0:
        ss_obj =sub_staff_allo_table()
        ss_obj.STAFF = staff_table.objects.get(id=name)
        ss_obj.SUBJECT = labsubject_table.objects.get(id=subject)
        ss_obj.save()
        return HttpResponse('''<script>alert('addded');window.location="/allocatesub_staff#about"</script>''')
    else:
        return HttpResponse('''<script>alert('Already addded');window.location="/allocatesub_staff#about"</script>''')

@login_required(login_url='/')
def editsub_staff(request,id):
    request.session['id'] = id

    ob = labsubject_table.objects.all()
    ob1 = staff_table.objects.all()
    OBa=sub_staff_allo_table.objects.get(id=id)
    return render(request, 'Admin/edit subject - staff.html',{'val':ob,'val1':ob1,'va':OBa})

@login_required(login_url='/')
def editsub_staff_action(request):
    ss_obj =sub_staff_allo_table.objects.get(id=request.session['id'])
    name= request.POST['select']
    subject = request.POST['select2']
    ss_obj.STAFF = staff_table.objects.get(id=name)
    ss_obj.SUBJECT = labsubject_table.objects.get(id=subject)
    ss_obj.save()
    return HttpResponse('''<script>window.location="/allocatesub_staff#about"</script>''')

@login_required(login_url='/')
def dlt_sub_staff(request, id):
    ob = sub_staff_allo_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/allocatesub_staff#about"</script>''')

@login_required(login_url='/')
def time_shedule_staff(request,id):
    request.session['allo_id']=id
    ob = staff_lab_allocatio.objects.filter(SUBJECT_STAFF__id=id)
    return render(request, 'Admin/time_shedule _staff.html',{'val':ob})

@login_required(login_url='/')
def add_time_schedule_staff(request):
    return render(request, 'Admin/add_time_schedule_staff.html')

@login_required(login_url='/')
def add_time_schedule_action(request):
    day=request.POST['select']
    hour=request.POST.getlist("cb")
    task=0
    for i in hour:
        ob=staff_lab_allocatio.objects.filter(day=day,period=i)
        if len(ob) == 0:
            time_obj = staff_lab_allocatio()
            time_obj.SUBJECT_STAFF=sub_staff_allo_table.objects.get(id=request.session['allo_id'])
            time_obj.day=day
            time_obj.period=i
            time_obj.save()
        else:
            task=1
    if task==0:
        return HttpResponse('''<script>alert('addded');window.location="/allocatesub_staff#about"</script>''')
    else:
        return HttpResponse('''<script>alert('Already addded');window.location="/allocatesub_staff#about"</script>''')

@login_required(login_url='/')
def dlt_time_schedule(request, id):
    ob = staff_lab_allocatio.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/allocatesub_staff#about"</script>''')




@login_required(login_url='/')
def viewsystem(request):
    ob = system_table.objects.all()
    return render(request, 'Admin/systemview.html',{'val':ob})

@login_required(login_url='/')
def viewsystem_search(request):
    dt = request.POST['dt']
    ob = system_table.objects.filter(date=dt)
    return render(request, 'Admin/systemview.html',{'val':ob,'val1': str(dt)})


@login_required(login_url='/')
def viewfeedback(request):
    ob = student_feedback.objects.all()
    on=staff_table.objects.all()
    return render(request, 'Admin/Viewstudfeedback.html',{'val':ob,'va':on})

@login_required(login_url='/')
def viewfeedback_search(request):
    c = request.POST['select']
    on=staff_table.objects.all()
    ob = student_feedback.objects.filter(STAFF__id=c)
    return render(request, 'Admin/Viewstudfeedback.html',{'val':ob,'va':on,"c":int(c)})

@login_required(login_url='/')
def view_allo_sub_staff(request):
    ls=['Monday',     'Tuesday',    'Wednesday',    'Thursday',    'Friday']
    hr=['1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period',]
    op=[["Day/Hour",'1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period']]
    for i in ls:
        r=[i]
        for j in hr:
            o=staff_lab_allocatio.objects.filter(day=i,period=j)
            if len(o)==0:
                r.append("Free")
            else:
                r.append(o[0].SUBJECT_STAFF.STAFF.name+" - "+o[0].SUBJECT_STAFF.SUBJECT.subject)
        op.append(r)
    ob = student_feedback.objects.all()
    return render(request, 'Admin/timetable.html',{'val':op})



@login_required(login_url='/')
def staffhome(request):
    return render(request, 'Staff/staffindex.html',{'nm':request.session['name'],'im':str(request.session['img'])})

@login_required(login_url='/')
def viewstud(request):
    # os=staff_table.objects.get(LOGIN__id=request.session['lid'])
    # dep=os.COURSE.DEPARTMENT.dept_name
    ob = student_table.objects.all()
    for i in ob:
        i.qualification = i.qualification.split(",")
    o = dept_table.objects.all()
    oo1 = course_table.objects.all()
    return render(request, 'Staff/studview.html',{'val':o,'val2': ob, 'val1': oo1})

@login_required(login_url='/')
def viewstud_search(request):
    o = dept_table.objects.all()
    oo1 = course_table.objects.all()
    dep = request.POST['select']
    course = request.POST['select2']
    semester = request.POST['select3']
    print(dep, ",", course, ",", semester, "======================")
    try:
        if dep != "" and course != "" and semester != "":
            ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester, COURSE__id=course)
            return render(request, 'Staff/studview.html',
                          {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': int(dep), 'crs': int(course)})
        else:
            try:
                if dep != "" and (course == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': int(dep), 'crs': 0})
                elif course != "" and (dep == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': int(course)})
                elif semester != "" and (dep == "" and course == ''):
                    ob = student_table.objects.filter(semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': 0, 'crs': 0})
                elif (dep != "" and course != ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': int(dep), 'crs': int(course)})
                elif dep != "" and semester != "":
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': int(dep), 'crs': 0})
                elif semester != "" and course != "":
                    ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': 0, 'crs': int(course)})
                else:
                    ob = student_table.objects.all()
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Staff/studview.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': 0})

            except:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html',
                              {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': 0})

    except:
        try:
            if dep != "" and (course == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o, })
            elif course != "" and (dep == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and (dep == "" and course == ''):
                ob = student_table.objects.filter(semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif (dep != "" and course != ""):
                print("kiiiiii")
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif dep != "" and semester != "":
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and course != "":
                ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})
            else:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})

        except:
            ob = student_table.objects.all()
            for i in ob:
                i.qualification = i.qualification.split(",")
            return render(request, 'Staff/studview.html', {'val2': ob, 'val1': oo1, 'val': o})


@login_required(login_url='/')
def view_allocated_lab(request):
    ob = staff_lab_allocatio.objects.filter(SUBJECT_STAFF__STAFF__LOGIN=request.session['lid'])
    return render(request, 'Staff/view allo-sub.html',{'val':ob})

@login_required(login_url='/')
def view_allocated_lab_search(request):
    day=request.POST['select']
    ob = staff_lab_allocatio.objects.filter(day=day,SUBJECT_STAFF__STAFF__LOGIN=request.session['lid'])
    return render(request, 'Staff/view allo-sub.html',{'val':ob,'day':day})

@login_required(login_url='/')
def viewexam(request):
    o=staff_table.objects.get(LOGIN__id=request.session['lid'])
    ob = labsubject_table.objects.all()
    ob1 = exam_table.objects.filter(STAFF__name=o.name)
    return render(request, 'Staff/view exam.html',{'val':ob,'val1':ob1})

@login_required(login_url='/')
def viewexam_search(request):
    sub=request.POST['select']
    ob = labsubject_table.objects.all()
    ob1 = exam_table.objects.filter(SUBJECT__id=sub)
    return render(request, 'Staff/view exam.html',{'val':ob,'val1':ob1,'sub':int(sub)})

@login_required(login_url='/')
def viewcomplaint(request):
    ob =complaint_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'Staff/view complaint.html',{'val':ob})

@login_required(login_url='/')
def viewcomplaint_search(request):
    date = request.POST['dt']
    ob =complaint_table.objects.filter(date=date,STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'Staff/view complaint.html',{'val':ob,'val1':date})

@login_required(login_url='/')
def viewdoubt(request):
    ob =doubt_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'Staff/view doubt.html',{'val':ob})

@login_required(login_url='/')
def viewdoubt_s(request):
    date=request.POST['dt']
    ob =doubt_table.objects.filter(STAFF__LOGIN__id=request.session['lid'],date=date)
    return render(request, 'Staff/view doubt.html',{'val':ob,'val1':date})

@login_required(login_url='/')
def sendreply(request,id):
    request.session['ddid']=id
    return render(request, 'Staff/send reply.html')

@login_required(login_url='/')
def senddoubtreply(request):
    reply=request.POST['textarea']
    ob=doubt_table.objects.get(id=request.session['ddid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>window.location="/viewdoubt#about"</script>''')


@login_required(login_url='/')
def sendreplyco(request,id):
    request.session['coid']=id
    return render(request, 'Staff/cosend reply.html')


@login_required(login_url='/')
def sendcomplntreply(request):
    reply=request.POST['textarea']
    ob=complaint_table.objects.get(id=request.session['coid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>window.location="/viewcomplaint#about"</script>''')

@login_required(login_url='/')
def view_syst_stud_allocation(request):
    sob = staff_table.objects.get(LOGIN__id=request.session['lid'])
    cid = sob.COURSE.id
    sob = student_table.objects.filter(COURSE__id=cid)
    sids = []
    for i in sob:
        sids.append(i.id)
    obj = system_stud_allo_table.objects.filter(STUDENT__id__in=sids)
    return render(request, 'Staff/view sys-stud allo.html',{'val':obj})

@login_required(login_url='/')
def view_syst_stud_allocation_search(request):
    nm=request.POST['textfield']
    ob=system_stud_allo_table.objects.filter(STUDENT__fname__icontains=nm)
    return render(request, 'Staff/view sys-stud allo.html',{'val':ob,'c':nm})

def view_sys(request):
    sob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    cid=sob.COURSE.id
    sob=student_table.objects.filter(COURSE__id=cid)
    sids=[]
    for i in sob:
        sids.append(i.id)
    obj=system_stud_allo_table.objects.filter(STUDENT__id__in=sids)
    return render(request,'Staff/systems.html',{'val':obj})

def check_system(request,id):
    return render(request, 'Staff/checks systems.html',{'s':id})

def kill_sy(request):
    ob=process.objects.filter(SYSTEM__system_id=request.session['systid'])
    return render(request, 'Staff/kill.html',{'val':ob})


def kill_pro(request,pr,id):
    ob = command()
    ob.SYSTEM = system_table.objects.get(system_id=id)
    ob.process =pr
    ob.save()
    return redirect('/kill_sy')



def process_list(request,id):
    request.session['systid']=id
    ob=command()
    ob.SYSTEM=system_table.objects.get(system_id=id)
    ob.process="bgp"
    ob.save()
    return redirect('kill_sy')

def screenshots(request,id):
    request.session['ssid']=id
    ob=command()
    ob.SYSTEM=system_table.objects.get(system_id=id)
    ob.process="sc"
    ob.save()
    return redirect('detailed_view_notifi')

def restart(request,id):
    ob=command()
    ob.SYSTEM=system_table.objects.get(system_id=id)
    ob.process="rs"
    ob.save()
    return redirect('kill_sy')

def shutdown(request,id):
    ob=command()
    ob.SYSTEM=system_table.objects.get(system_id=id)
    ob.process="sd"
    ob.save()
    return redirect('kill_sy')




@login_required(login_url='/')
def view_notifi(request):
    obj=system_table.objects.all()
    ob = notification_table.objects.all()
    return render(request, 'Staff/view noti.html',{'val':ob,'val1':obj})


@login_required(login_url='/')
def view_notifi_search(request):
    nm = request.POST['select']
    obj=system_table.objects.all()
    ob = notification_table.objects.filter(SYSTEM__id=nm)
    return render(request, 'Staff/view noti.html',{'val':ob,'val1':obj,'val2':int(nm)})

@login_required(login_url='/')
def detailed_view_notifi(request):
    ob=screenshot.objects.filter(SYSTEM__system_id=request.session['ssid'])
    return render(request, 'Staff/detailed view.html',{'val':ob})


@login_required(login_url='/')
def labassistanthome(request):
    return render(request, 'Lab-assistant/labindex.html',{'n':request.session['n'],'im':request.session['img']})


@login_required(login_url='/')
def mngsystems(request):
    ob=system_table.objects.all()
    return render(request, 'Lab-assistant/system.html',{'val':ob})


@login_required(login_url='/')
def addsystems(request):
    return render(request, 'Lab-assistant/add system.html')


@login_required(login_url='/')
def addsystems_action(request):
    systm=request.POST['t1']
    processor=request.POST['t2']
    RAM=request.POST['t3']
    HDD=request.POST['t4']
    SSD=request.POST['t5']
    ob=system_table()
    ob.system_id = systm
    ob.processor = processor
    ob.RAM = RAM
    ob.HDD = HDD
    ob.SSD = SSD

    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert('added');window.location="/mngsystems"</script>''')


@login_required(login_url='/')
def system_search(request):
    name=request.POST['t1']
    ob = system_table.objects.filter(system_id__icontains=name)
    return render(request, 'Lab-assistant/system.html', {'val': ob,'nm':name})


@login_required(login_url='/')
def dlt_system(request, id):
    ob = system_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted');window.location="/mngsystems"</script>''')

@login_required(login_url='/')
def edit_systems(request,id):
    request.session['system_id'] = id
    ob = system_table.objects.get(id=id)
    return render(request, 'Lab-assistant/edit_system.html', {"val": ob, 'dt': str(ob.date)})

@login_required(login_url='/')
def edit_systems_action(request):
    systm=request.POST['t1']
    processor = request.POST['t2']
    RAM = request.POST['t3']
    HDD = request.POST['t4']
    SSD = request.POST['t5']
    ob=system_table.objects.get(id=request.session['system_id'])
    ob.system_id = systm
    ob.processor = processor
    ob.RAM = RAM
    ob.HDD = HDD
    ob.SSD = SSD
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert('updated');window.location="/mngsystems"</script>''')

@login_required(login_url='/')
def system_stud_allocation(request):
    ob = system_stud_allo_table.objects.all()
    return render(request, 'Lab-assistant/stud system allo.html',{'val':ob})
@login_required(login_url='/')
def system_stud_allocation_s(request):
    sys_no=request.POST['t1']

    ob = system_stud_allo_table.objects.filter(SYSTEM__system_id=sys_no)
    return render(request, 'Lab-assistant/stud system allo.html',{'val':ob,'sys_no':sys_no})

@login_required(login_url='/')
def clear_system_stud_allo(request):
    ob=system_stud_allo_table.objects.all()
    for i in ob:
        i.delete()
    return HttpResponse('''<script>alert('clear');window.location="/system_stud_allocation"</script>''')


@login_required(login_url='/')
def system_stud_search(request):
    sys_no=request.POST['t1']
    ob = system_table.objects.filter(system_id__icontains=sys_no)
    return render(request, 'Lab-assistant/system.html', {'val': ob,'nm':sys_no})


@login_required(login_url='/')
def add_system_stud(request,id):
    request.session['StuD_id']=id
    # ob = student_table.objects.all()
    ob1 = system_table.objects.all()
    return render(request, 'Lab-assistant/add stud-sys.html',{'val1':ob1})


@login_required(login_url='/')
def add_system_stud_action(request):
    # stud = request.POST['select']
    system = request.POST['select2']
    ob=student_table.objects.get(id=request.session['StuD_id'])
    print(ob.id)
    print(ob.COURSE.id,"ccccccccccccc")
    print(ob.semester,"ssssssssssss")

    ob=system_stud_allo_table.objects.filter(Q(SYSTEM__id=system,STUDENT__COURSE__id=ob.COURSE.id,STUDENT__semester=ob.semester)|Q(STUDENT_id=ob.id))
    if len(ob) == 0:
        system_stud_obj = system_stud_allo_table()
        system_stud_obj.STUDENT = student_table.objects.get(id=request.session['StuD_id'])
        system_stud_obj.SYSTEM = system_table.objects.get(id=system)
        system_stud_obj.save()
        return HttpResponse('''<script>window.location="/system_stud_allocation#about"</script>''')
    else:
        return HttpResponse('''<script>alert("Already added");window.location="/system_stud_allocation#about"</script>''')


@login_required(login_url='/')
def dlt_system_stud_allo(request, id):
    ob = system_stud_allo_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/system_stud_allocation#about"</script>''')


@login_required(login_url='/')
def edit_system_stud(request,id):
    request.session['sid']=id
    ob = student_table.objects.all()
    ob1 = system_table.objects.all()
    request.session['STRID']=id
    ob2=system_stud_allo_table.objects.get(id=id)
    return render(request, 'Lab-assistant/edit stud-sys.html',{'val':ob,'val1':ob1,'v':ob2})



@login_required(login_url='/')
def edit_system_stud_action(request):
    system_stud_obj = system_stud_allo_table.objects.get(id=request.session['sid'])
    stud = request.POST['select']
    system = request.POST['select2']
    ob = student_table.objects.get(id=stud)


    ob = system_stud_allo_table.objects.filter(Q(SYSTEM__id=system, STUDENT__COURSE__id=ob.COURSE.id, STUDENT__semester=ob.semester) | Q(STUDENT_id=ob.id))
    if len(ob) == 0:
        # system_stud_obj = system_stud_allo_table()
        system_stud_obj.STUDENT = student_table.objects.get(id=stud)
        system_stud_obj.SYSTEM = system_table.objects.get(id=system)
        system_stud_obj.save()
        return HttpResponse('''<script>window.location="/system_stud_allocation#about"</script>''')
    else:
        return HttpResponse('''<script>alert("Already exist");window.location="/system_stud_allocation#about"</script>''')

@login_required(login_url='/')
def view_exam(request):
    ob=exam_table.objects.all()
    return render(request, 'Lab-assistant/view exam.html',{'val':ob})

@login_required(login_url='/')
def view_exam_search(request):
    dt=request.POST['t1']
    ob=exam_table.objects.filter(date=dt)
    return render(request, 'Lab-assistant/view exam.html',{'val':ob,'dt':dt})


@login_required(login_url='/')
def view_students(request):
    ob = student_table.objects.all()
    o = dept_table.objects.all()
    for i in ob:
        i.qualification=i.qualification.split(",")
    oo1 = course_table.objects.all()
    return render(request, 'Lab-assistant/view stud.html',{'val2':ob,'val':o,'val1':oo1})

@login_required(login_url='/')
def view_stud_search(request):
    o = dept_table.objects.all()
    oo1 = course_table.objects.all()
    dep = request.POST['select']
    course = request.POST['select2']
    semester = request.POST['select3']
    print(dep, ",", course, ",", semester, "======================")
    try:
        if dep != "" and course != "" and semester != "":
            ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester, COURSE__id=course)
            for i in ob:
                i.qualification = i.qualification.split(",")
            return render(request, 'Lab-assistant/view stud.html',{'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': int(dep), 'crs': int(course)})
        else:
            try:
                if dep != "" and (course == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',{'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': int(dep), 'crs': 0})
                elif course != "" and (dep == "" and semester == ""):
                    ob = student_table.objects.filter(COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': int(course)})
                elif semester != "" and (dep == "" and course == ''):
                    ob = student_table.objects.filter(semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': 0, 'crs': 0})
                elif (dep != "" and course != ""):
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': int(dep), 'crs': int(course)})
                elif dep != "" and semester != "":
                    ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': int(dep), 'crs': 0})
                elif semester != "" and course != "":
                    ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': semester, 'dp': 0, 'crs': int(course)})
                else:
                    ob = student_table.objects.all()
                    for i in ob:
                        i.qualification = i.qualification.split(",")
                    return render(request, 'Lab-assistant/view stud.html',
                                  {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': 0})

            except:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Lab-assistant/view stud.html',
                              {'val2': ob, 'val1': oo1, 'val': o, 'sem': 0, 'dp': 0, 'crs': 0})

    except:
        try:
            if dep != "" and (course == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request,'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o, })
            elif course != "" and (dep == "" and semester == ""):
                ob = student_table.objects.filter(COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                # ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE=course)
                return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and (dep == "" and course == ''):
                ob = student_table.objects.filter(semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif (dep != "" and course != ""):
                print("kiiiiii")
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, COURSE__id=course)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif dep != "" and semester != "":
                ob = student_table.objects.filter(COURSE__DEPARTMENT=dep, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})
            elif semester != "" and course != "":
                ob = student_table.objects.filter(COURSE__id=course, semester=semester)
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request,'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})
            else:
                ob = student_table.objects.all()
                for i in ob:
                    i.qualification = i.qualification.split(",")
                return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})

        except:
            ob = student_table.objects.all()
            for i in ob:
                i.qualification = i.qualification.split(",")
            return render(request, 'Lab-assistant/view stud.html', {'val2': ob, 'val1': oo1, 'val': o})

# @login_required(login_url='/')
# def view_sub_staff_allocation(request):
#     ob=staff_lab_allocatio.objects.all()
#     return render(request, 'Lab-assistant/viw sub staff allo.html',{'val':ob})

@login_required(login_url='/')
def view_sub_staff_search(request):
    day = request.POST['select']
    ob=staff_lab_allocatio.objects.filter(day=day)
    return render(request, 'Lab-assistant/viw sub staff allo.html',{'val':ob,'day':day})















def studenthome(request):
    return render(request, 'Student/studindex.html',{'sn':request.session['sn'],'im':request.session['img']})


@login_required(login_url='/')
def viewlabsub(request):
    obb=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = labsubject_table.objects.filter(COURSE__id=obb.COURSE.id)
    # ob = staff_lab_allocatio.objects.filter(SUBJECT_STAFF__SUBJECT__COURSE__id=obb.COURSE.id)
    ob2 = labsubject_table.objects.filter(COURSE__id=obb.COURSE.id)
    return render(request, 'Student/view lab sub.html',{'val':ob,'val2':ob2})


@login_required(login_url='/')
def viewlabsub_search(request):
    sub = request.POST['select']
    obb=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = labsubject_table.objects.filter(COURSE__id=obb.COURSE.id)
    # ob = staff_lab_allocatio.objects.filter(SUBJECT_STAFF__SUBJECT__COURSE__id=obb.COURSE.id,SUBJECT_STAFF__SUBJECT__id=sub)
    ob2 = labsubject_table.objects.filter(id=sub)
    return render(request, 'Student/view lab sub.html',{'val':ob,'val2':ob2,'ss':int(sub)})

@login_required(login_url='/')
def std_viewexam(request):
    o = student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = labsubject_table.objects.filter(COURSE__id=o.COURSE.id)
    ob1 = exam_table.objects.filter(SUBJECT__COURSE__id=o.COURSE.id)
    return render(request, 'Student/view exam.html',{'val':ob,'val1':ob1})


@login_required(login_url='/')
def std_viewexam_search(request):
    sub = request.POST['select']
    o = student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = labsubject_table.objects.all()
    ob1 = exam_table.objects.filter(SUBJECT__COURSE=o.COURSE,SUBJECT__id=sub)
    return render(request, 'Student/view exam.html',{'val':ob,'val1':ob1,'val2':sub,'ss':int(sub)})


@login_required(login_url='/')
def view_allocated_system(request):
    ob=system_stud_allo_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request, 'Student/view allocated systems.html',{'val':ob})

@login_required(login_url='/')
def view_system(request):
    ob = system_stud_allo_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request, 'Student/view systems.html',{'val':ob})


@login_required(login_url='/')
def view_doubt_reply(request):
    ob = doubt_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request, 'Student/view doubt nd reply.html',{'val':ob})

@login_required(login_url='/')
def view_doubt_reply_search(request):
    date=request.POST['textfield']
    ob = doubt_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'],date=date)
    return render(request, 'Student/view doubt nd reply.html',{'val':ob})

@login_required(login_url='/')
def add_doubt(request):
    od = student_table.objects.get(LOGIN__id=request.session['lid'])
    dep = od.COURSE.DEPARTMENT.dept_name
    ob = staff_table.objects.filter(COURSE__DEPARTMENT__dept_name=dep)
    return render(request,'Student/add doubt.html',{'val':ob})

@login_required(login_url='/')
def add_doubt_action(request):
    staff=request.POST['select']
    doubt=request.POST['textarea']
    proof = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(proof.name, proof)

    ob=doubt_table()
    ob.doubt=doubt
    ob.image=fsave
    ob.reply='pending'
    ob.STUDENT=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.STAFF=staff_table.objects.get(id=staff)
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>window.location="/view_doubt_reply#about"</script>''')

@login_required(login_url='/')
def view_complaint_reply(request):
    ob = complaint_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request, 'Student/View comp nd reply.html',{'val':ob})

@login_required(login_url='/')
def view_complaint_reply_search(request):
    date=request.POST['textfield']
    ob = complaint_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'],date=date)
    return render(request, 'Student/View comp nd reply.html',{'val':ob})

@login_required(login_url='/')
def add_compl(request):
    od = student_table.objects.get(LOGIN__id=request.session['lid'])
    dep = od.COURSE.DEPARTMENT.dept_name
    ob = staff_table.objects.filter(COURSE__DEPARTMENT__dept_name=dep)
    return render(request,'Student/add compl.html',{'val':ob})


@login_required(login_url='/')
def add_comp_action(request):
    staff=request.POST['select']
    complplaint=request.POST['textarea']
    ob=complaint_table()
    ob.complaint=complplaint
    ob.reply='pending'
    ob.STUDENT=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.STAFF=staff_table.objects.get(id=staff)
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>window.location="/view_complaint_reply#about"</script>''')

@login_required(login_url='/')
def send_feedback(request):
    od=student_table.objects.get(LOGIN__id=request.session['lid'])
    dep=od.COURSE.DEPARTMENT.dept_name
    ob=staff_table.objects.filter(COURSE__DEPARTMENT__dept_name=dep)
    return render(request,'Student/send feedback.html',{'val':ob})

@login_required(login_url='/')
def send_feeds1(request):
    staff=request.POST['select']
    feed=request.POST['textarea']
    ob=student_feedback()
    ob.STUDENT=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.STAFF=staff_table.objects.get(id=staff)
    ob.feedback=feed
    ob.datetime=datetime.now()
    ob.save()
    return HttpResponse('''<script>window.location="/send_feedback#about"</script>''')






@login_required(login_url='/')
def view_sub_staff_allocation(request):
    ls=['Monday',     'Tuesday',    'Wednesday',    'Thursday',    'Friday']
    hr=['1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period',]
    op=[["Day/Hour",'1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period']]
    for i in ls:
        r=[i]
        for j in hr:
            o=staff_lab_allocatio.objects.filter(day=i,period=j)
            if len(o)==0:
                r.append("Free")
            else:
                r.append(o[0].SUBJECT_STAFF.STAFF.name+" - "+o[0].SUBJECT_STAFF.SUBJECT.subject)
        op.append(r)
    ob = student_feedback.objects.all()
    return render(request, 'Lab-assistant/timetable.html',{'val':op})




@login_required(login_url='/')
def stude_view_timetable(request):
    ls=['Monday',     'Tuesday',    'Wednesday',    'Thursday',    'Friday']
    hr=['1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period',]
    op=[["Day/Hour",'1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period']]
    for i in ls:
        r=[i]
        for j in hr:
            u=student_table.objects.get(LOGIN__id=request.session['lid'])
            m=u.COURSE.id
            print(i,"KKKKKKKKKKKKKKKKKKKKKKK")

            o=staff_lab_allocatio.objects.filter(day=i,period=j,SUBJECT_STAFF__SUBJECT__COURSE__id=m)
            print(o,"JJJJJJJJJJJJJJJJ")
            if len(o)==0:
                r.append("Free")
            else:
                r.append(o[0].SUBJECT_STAFF.STAFF.name+" - "+o[0].SUBJECT_STAFF.SUBJECT.subject)
        op.append(r)
    ob = student_feedback.objects.all()
    return render(request, 'Student/timetable.html',{'val':op})


@login_required(login_url='/')
def staff_view_timetable(request):
    ls=['Monday',     'Tuesday',    'Wednesday',    'Thursday',    'Friday']
    hr=['1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period',]
    op=[["Day/Hour",'1st Period',
        '2nd Period',
        '3rd Period',
        '4th Period',
        '5th Period',
        '6th Period']]
    for i in ls:
        r=[i]
        for j in hr:
            u=staff_table.objects.get(LOGIN__id=request.session['lid'])
            m=u.COURSE.id
            print(i,"KKKKKKKKKKKKKKKKKKKKKKK")

            o=staff_lab_allocatio.objects.filter(day=i,period=j,SUBJECT_STAFF__STAFF__id=u.id)
            print(o,"JJJJJJJJJJJJJJJJ")
            if len(o)==0:
                r.append("Free")
            else:
                r.append(o[0].SUBJECT_STAFF.SUBJECT.subject)
        op.append(r)
    ob = student_feedback.objects.all()
    return render(request, 'Staff/timetable.html',{'val':op})



def index(request):
    # if request.method == 'GET':



    sid  = request.POST['staff']
    ob=staff_table.objects.get(id=sid)
    ob1=labsubject_table.objects.filter(COURSE__id=ob.COURSE.id)
    ls=[]
    for i in ob1:
        ls.append({"id":i.id,"sub":i.subject})
    print(ls)
    return JsonResponse(ls,safe=False)






############################################pc monitoring####################3





import os
from datetime import datetime

from django.http import HttpResponse

from .models import *
import base64

# from src.dbcon import *



# def index():
#     return HttpResponse("okk")


def dw(request):
    path = request.GET["p"]
    file_path = "static/" + path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{path}"'
        return response

def select(request):
    path = request.GET["p"]
    result = screenshot.objects.get(sid=path)

    if result:
        result.delete()
        return HttpResponse("ok")
    else:
        return HttpResponse("na")

def insprocess(request):
    lis = ['System Idle Process', 'System', 'Registry', 'smss.exe', 'wininit.exe', 'services.exe', 'lsass.exe', 'wsc_proxy.exe', 'Memory Compression', 'igfxCUIService.exe', 'AvastSvc.exe', 'aswToolsSvc.exe', 'dasHost.exe', 'spoolsv.exe', 'IntelCpHDCPSvc.exe', 'novapdfs.exe', 'SecurityHealthService.exe']
    sid = request.GET["p"]
    pr = request.GET["pr"]

    if pr not in lis:
        process.objects.filter(sid=sid, process=pr).delete()
        # Process.objects.create(sid=sid, process=pr)
        ob=process()
        ob.SYSTEM=system_table.objects.get(id=sid)
        return HttpResponse("ok")
    return HttpResponse("ok")

def processes(request):
    path = request.GET["p"]
    result = command.objects.filter(SYSTEM__id=path)
    res = "#".join([item.process for item in result])
    command.objects.filter(SYSTEM__id=path).delete()
    return HttpResponse(res)

def sd(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def rs(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def bgp(request):
    path = request.GET["p"]
    result = command.objects.filter(sid=path).first()
    res_str = "#".join(result.process)

    command.objects.filter(sid=path).delete()
    return HttpResponse(res_str)

def up(request):
    fn = request.GET["fn"]
    path = request.GET["p"]
    id = request.GET["id"]

    image_string = path.decode('base64')
    file_path = "static/media/screenshot/" + fn

    with open(file_path, "wb") as fh:
        fh.write(image_string)

    screenshot.objects.filter(sid=id).delete()
    ob=screenshot()
    ob.SYSTEM=system_table.objects.get(id=id)
    ob.scrnsht=fn
    ob.date=datetime.today()
    ob.status='pending'


    return HttpResponse("ok")

def up1(request):
    fn = request.GET["fn"]
    path = request.GET["p"]

    image_string = path.decode('base64')
    file_path = "static/media/capture/" + fn

    with open(file_path, "wb") as fh:
        fh.write(image_string)

    return HttpResponse("ok")


