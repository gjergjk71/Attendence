from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from home.models import *
from home.models import *
from django.contrib import messages
from home.templatetags import *
from django.apps import apps
import datetime

def todays_add_attendance(request,prof,semester,prog,sub,date):
    present_students = request.POST.getlist('present[]')
    Facultys_model = apps.get_model('home.Facultys')
    proffeser = Facultys_model.objects.all().filter(username=prof)

    Students_list_model = apps.get_model('home.Students')
    students_list = Students_list_model.objects.all().filter(sem=semester,section=prog)
    for i in students_list:
        Students_model = apps.get_model('home.Students')
        add_student_attendance_model = apps.get_model('home.add_student_attendance')
        add__attendance_model = add_student_attendance_model()
        add__attendance_model.professer_name = proffeser[0]
        add__attendance_model.student_name = i
        add__attendance_model.semester = semester
        add__attendance_model.subject = sub
        add__attendance_model.batch = i.section
        add__attendance_model.date = date
        if i.roll_no in present_students:
            add__attendance_model.attend = 1
        else:
            add__attendance_model.attend = 0
        add__attendance_model.save()      
    messages.success(request, 'Attendance Added Successfully.')
    reder = '/view-attendence/'+str(semester)+'/'+prog+'/'+sub

    return HttpResponseRedirect(reder)

def add_attendance(request):
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)


    semester_1_model = apps.get_model('home.Semester_1')
    sem1 = semester_1_model.objects.all().filter(professer_name=faculty_data)

    semester_2_model = apps.get_model('home.Semester_2') 
    sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
    for obj in sem2:
        pass
    
    semester_3_model = apps.get_model('home.Semester_3')
    sem3 = semester_3_model.objects.all().filter(professer_name=faculty_data)


    semester_4_model = apps.get_model('home.Semester_4')
    sem4 = semester_4_model.objects.all().filter(professer_name=faculty_data)


    semester_5_model = apps.get_model('home.Semester_5')
    sem5 = semester_5_model.objects.all().filter(professer_name=faculty_data)

    semester_6_model = apps.get_model('home.Semester_6')
    sem6 = semester_6_model.objects.all().filter(professer_name=faculty_data)


    semester_7_model = apps.get_model('home.Semester_7')
    sem7 = semester_7_model.objects.all().filter(professer_name=faculty_data)


    semester_8_model = apps.get_model('home.Semester_8')
    sem8 = semester_8_model.objects.all().filter(professer_name=faculty_data)

    
    content = { 'data': faculty_data, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8}
    return render(request, 'dashboard/add_attendance.html', content)
    

def today_attendance(request,prof,semester,prog,sub,date):
    student_model = apps.get_model('home.Students')
    programe_model = apps.get_model('home.Sections')
    programe = programe_model.objects.all().filter(name='CS') 
    students = student_model.objects.all().filter(sem=semester,section=prog) 
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    date = datetime.datetime.today().strftime('%Y-%m-%d')
 
    return render(request, 'dashboard/add_stud_attendance.html', {'students':students, 'sub':sub, "semester":semester,'date':date, 'proff':faculty_data.username, 'programe':prog})

def view_attendance(request):
    if 'faculty' in request.session:
        sessn_val = request.session['faculty']
        faculty_data = Facultys.objects.get(pk=sessn_val)
        sectn_data = Sections.objects.get(name=faculty_data.section)
  
        semester_1_model = apps.get_model('home.Semester_1')
        sem1 = semester_1_model.objects.all().filter(professer_name=faculty_data)

        semester_2_model = apps.get_model('home.Semester_2') 
        sem2 = semester_2_model.objects.all().filter(professer_name=faculty_data)
        
        semester_3_model = apps.get_model('home.Semester_3')
        sem3 = semester_3_model.objects.all().filter(professer_name=faculty_data)


        semester_4_model = apps.get_model('home.Semester_4')
        sem4 = semester_4_model.objects.all().filter(professer_name=faculty_data)

        semester_5_model = apps.get_model('home.Semester_5')
        sem5 = semester_5_model.objects.all().filter(professer_name=faculty_data)


        semester_6_model = apps.get_model('home.Semester_6')
        sem6 = semester_6_model.objects.all().filter(professer_name=faculty_data)


        semester_7_model = apps.get_model('home.Semester_7')
        sem7 = semester_7_model.objects.all().filter(professer_name=faculty_data)


        semester_8_model = apps.get_model('home.Semester_8')
        sem8 = semester_8_model.objects.all().filter(professer_name=faculty_data)

        
        content = { 'data': faculty_data, 'sem1':sem1, 'sem2':sem2, 'value': 10, 'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8}

        return render(request, 'home/view_attendance.html', content)
    elif 'student' in request.session:
        student_data = Students.objects.get(pk=request.session['student'])
        s = str("Semester_"+str(student_data.sem))
        student_subject = list()
        if(s == ("Semester_1")):
           
            student_subject = Semester_1.objects.all()
        elif(s == ("Semester_2")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_3")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_4")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_5")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_6")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_7")):
            student_subject = Semester_1.objects.all()

        elif(s == ("Semester_8")):
            student_subject = Semester_1.objects.all()

        section = Sections.objects.get(name=student_data.section)
        content = {'student_data': student_data, 'data':student_data , 'student_subject':student_subject}
    return render(request, 'home/view_attendance_studnt.html', content)

def faculty_view_attendence(request, sem, prog, sub):
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    student_attendance_model = apps.get_model('home.add_student_attendance')
    Students_list_model = apps.get_model('home.Students')
    students_list = Students_list_model.objects.all().filter(sem=sem,section=prog)
    l_student = list()
    for i in students_list:
        l = list()
        student_attendance_model = apps.get_model('home.add_student_attendance')
        student_present = student_attendance_model.objects.all().filter(semester=sem, student_name = i, subject=sub,attend=1)
        student_absent = student_attendance_model.objects.all().filter(semester=sem, student_name = i, subject=sub,attend=0)
        l.append(i.name)
        l.append(i.roll_no)
        l.append(len(student_present))
        l.append(len(student_absent))
        l_student.append(l)
    return render(request, 'dashboard/view_student_attendance.html',{'l_student':l_student,'prof':faculty_data.username,'sem':sem, 'prog':prog, 'sub':sub})


def faculty_search_view_attendence(request, sem, prog, sub):
    present_students = request.POST.getlist('present[]')
    select_value = int(present_students[0])
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    student_attendance_model = apps.get_model('home.add_student_attendance')
    Students_list_model = apps.get_model('home.Students')
    students_list = Students_list_model.objects.all().filter(sem=sem,section=prog)
    l_student = list()
    for i in students_list:
        l = list()
        student_attendance_model = apps.get_model('home.add_student_attendance')
        student_present = student_attendance_model.objects.all().filter(semester=sem, student_name = i, subject=sub,attend=1)
        student_absent = student_attendance_model.objects.all().filter(semester=sem, student_name = i, subject=sub,attend=0)
        total = len(student_present) + len(student_absent)
        if(len(student_present)/total<select_value):
            l.append(i.name)
            l.append(i.roll_no)
            l.append(len(student_present))
            l.append(len(student_absent))
            l_student.append(l)
    return render(request, 'dashboard/view_student_attendance.html',{'l_student':l_student,'prof':faculty_data.username,'sem':sem, 'prog':prog, 'sub':sub})

def view_my_attendance_sem(request,roll,sem,sub):
    student_data = Students.objects.get(pk=request.session['student'])
    add_student_attendance_model = apps.get_model('home.add_student_attendance')
    attendance_of_student_present = add_student_attendance_model.objects.all().filter(student_name=student_data,semester=sem,subject=sub,attend=1)
    attendance_of_student_absent = add_student_attendance_model.objects.all().filter(student_name=student_data,semester=sem,subject=sub,attend=0)
    return render(request,'dashboard/my_attendance.html',{"data":student_data,'sem':sem, 'sub':sub,'present':len(attendance_of_student_present),'absent':len(attendance_of_student_absent)})


def day_attendance(request, attendance_date):
    if 'faculty' in request.session:
        faculty_data = Facultys.objects.get(pk = request.session['faculty'])
        section = Sections.objects.get(name=faculty_data.section)
        attendance_data = daily_attendance.objects.filter(faculty = faculty_data.pk, attendance_date = attendance_date )
        content = {  'data': faculty_data, 'attendance_data' : attendance_data, 'section_data': section }
        return render(request, 'attendance/day_attendance.html', content)
    return render(request, 'attendance/day_attendance.html', content)

def student_profile(request, slug):
    sessn_val = request.session['faculty']
    faculty_data = Facultys.objects.get(pk=sessn_val)
    sectn_data = Sections.objects.get(name=faculty_data.section)
    studnt_data = Students.objects.get(slug=slug)
    attendance_data = daily_attendance.objects.filter(faculty=faculty_data.pk, section_id = sectn_data.pk)
    content = {'data': faculty_data, 'studnt_data':studnt_data, 'sectn_data': sectn_data, 'attendance_data':attendance_data}
    return render(request, 'attendance/student_profile.html', content)



def student_list(request, sem, prog, sub):
    student_model = apps.get_model('home.Students')
    students = student_model.objects.all().filter(sem=sem,section=prog) 
    return render(request, 'dashboard/student_list.html',{'students':students,'sem':sem,'prog':prog,'sub':sub})