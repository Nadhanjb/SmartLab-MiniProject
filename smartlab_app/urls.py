"""smart_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from smartlab_app import views

urlpatterns = [
    path('',views.main,name='main'),
    path('login',views.login,name='login'),
    path('ahome',views.ahome,name='ahome'),
    path('mngdept', views.mngdept, name='mngdept'),
    path('adddept', views.adddept, name='adddept'),
    path('view_allo_sub_staff', views.view_allo_sub_staff, name='view_allo_sub_staff'),
    path('add_dept_action', views.add_dept_action, name="add_dept_action"),
    path('edit_dept/<int:dept_id>', views.edit_dept, name="edit_dept"),
    path('edit_dept_action', views.edit_dept_action, name="edit_dept_action"),
    path('dlt_depart/<int:id>', views.dlt_depart, name="dlt_depart"),
    path('mngcourse',views.mngcourse,name='mngcourse'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('add_course_action', views.add_course_action, name='add_course_action'),
    path('edit_course/<int:course_id>', views.edit_course, name="edit_course"),
    path('edit_course_action', views.edit_course_action, name="edit_course_action"),
    path('dlt_course/<int:id>', views.dlt_course, name="dlt_course"),
    path('mngcourse_search', views.mngcourse_search, name='mngcourse_search'),
    path('mnglabsubj', views.mnglabsubj, name='mnglabsubj'),
    path('mnglabsubj_search', views.mnglabsubj_search, name='mnglabsubj_search'),
    path('addlabsubj', views.addlabsubj, name='addlabsubj'),
    path('add_labsubj_action', views.add_labsubj_action, name='add_labsubj_action'),
    path('edit_labsub/<int:id>', views.edit_labsub, name='edit_labsub'),
    path('edit_labsubj_action', views.edit_labsubj_action, name='edit_labsubj_action'),
    path('dlt_labsub/<int:id>', views.dlt_labsub, name="dlt_labsub"),
    path('mngstaff', views.mngstaff, name='mngstaff'),
    path('viewstud_search', views.viewstud_search, name='viewstud_search'),
    path('addstaff', views.addstaff, name='addstaff'),
    path('add_staff_action', views.add_staff_action, name='add_staff_action'),
    path('editstaff/<int:staff_id>', views.editstaff, name="editstaff"),
    path('edit_staff_action', views.edit_staff_action, name="edit_staff_action"),
    path('dlt_staff/<int:id>', views.dlt_staff, name="dlt_staff"),
    path('mng_staff_sch', views.mng_staff_sch, name='mng_staff_sch'),
    path('mnglabassist', views.mnglabassist, name='mnglabassist'),
    path('addlabassist', views.addlabassist, name='addlabassist'),
    path('add_labassi_action', views.add_labassi_action, name='add_labassi_action'),
    path('edit_lab_assi/<int:id>', views.edit_lab_assi, name='edit_lab_assi'),
    path('edit_labassi_action', views.edit_labassi_action, name='edit_labassi_action'),
    path('dlt_labassi/<int:id>', views.dlt_labassi, name="dlt_labassi"),
    path('mnglabassi_search', views.mnglabassi_search, name='mnglabassi_search'),
    path('mngstud', views.mngstud, name='mngstud'),
    path('addstud', views.addstud, name='addstud'),
    path('addstud_action', views.addstud_action, name='addstud_action'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('edit_stud_action', views.edit_stud_action, name='edit_stud_action'),
    path('dlt_student/<int:id>', views.dlt_student, name='dlt_student'),
    path('stud_search', views.stud_search, name='stud_search'),
    path('mngexam', views.mngexam, name='mngexam'),
    path('addexam', views.addexam, name='addexam'),
    path('add_exam_action', views.add_exam_action, name='add_exam_action'),
    path('edit_exam/<int:exam_id>', views.edit_exam, name='edit_exam'),
    path('edit_exam_action', views.edit_exam_action, name='edit_exam_action'),
    path('dlt_exam/<int:id>', views.dlt_exam, name="dlt_exam"),
    path('searchexm', views.searchexm, name='searchexm'),
    path('allocatesub_staff', views.allocatesub_staff, name='allocatesub_staff'),
    path('addsub_staff', views.addsub_staff, name='addsub_staff'),
    path('addsub_staff_action', views.addsub_staff_action, name='addsub_staff_action'),
    path('editsub_staff/<int:id>', views.editsub_staff, name='editsub_staff'),
    path('editsub_staff_action', views.editsub_staff_action, name='editsub_staff_action'),
    path('dlt_sub_staff/<int:id>', views.dlt_sub_staff, name="dlt_sub_staff"),
    path('time_shedule_staff/<int:id>', views.time_shedule_staff, name='time_shedule_staff'),
    path('add_time_schedule_staff', views.add_time_schedule_staff, name='add_time_schedule_staff'),
    path('add_time_schedule_action', views.add_time_schedule_action, name='add_time_schedule_action'),
    path('dlt_time_schedule/<int:id>', views.dlt_time_schedule, name="dlt_time_schedule"),
    path('upgrade/<int:id>', views.upgrade, name="upgrade"),
    # path('viewstud', views.viewstud, name='viewstud'),
    # path('viewstud_search', views.viewstud_search, name='viewstud_search'),
    path('viewsystem', views.viewsystem, name='viewsystem'),
    path('viewsystem_search', views.viewsystem_search, name='viewsystem_search'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewfeedback_search', views.viewfeedback_search, name='viewfeedback_search'),
    path('searchexm', views.searchexm, name='searchexm'),
    path('logout', views.logout, name='logout'),




    path('staffhome', views.staffhome, name='staffhome'),
    path('staff_view_timetable', views.staff_view_timetable, name='staff_view_timetable'),
    # path('mngstud', views.mngstud, name='mngstud'),
    # path('addstud', views.addstud, name='addstud'),
    # path('addstud_action', views.addstud_action, name='addstud_action'),
    # path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    # path('edit_stud_action', views.edit_stud_action, name='edit_stud_action'),
    # path('edit_stud_action', views.edit_stud_action, name='edit_stud_action'),
    # path('student_search', views.student_search, name='student_search'),
    # path('dlt_student/<int:id>', views.dlt_student, name='dlt_student'),
    path('viewstud', views.viewstud, name='viewstud'),
    path('viewstud_search', views.viewstud_search, name='viewstud_search'),
    path('view_allocated_lab', views.view_allocated_lab, name='view_allocated_lab'),
    path('view_allocated_lab_search', views.view_allocated_lab_search, name='view_allocated_lab_search'),
    path('viewexam', views.viewexam, name='viewexam'),
    path('viewexam_search', views.viewexam_search, name='viewexam_search'),
    path('viewcomplaint', views.viewcomplaint, name='viewcomplaint'),
    path('viewdoubt', views.viewdoubt, name='viewdoubt'),
    path('sendreply/<int:id>', views.sendreply, name='sendreply'),
    path('sendreplyco/<int:id>', views.sendreplyco, name='sendreplyco'),
    path('senddoubtreply', views.senddoubtreply, name='senddoubtreply'),
    path('sendcomplntreply', views.sendcomplntreply, name='sendcomplntreply'),
    path('view_syst_stud_allocation', views.view_syst_stud_allocation, name='view_syst_stud_allocation'),
    path('view_syst_stud_allocation_search', views.view_syst_stud_allocation_search, name='view_syst_stud_allocation_search'),
    path('view_notifi', views.view_notifi, name='view_notifi'),
    path('view_notifi_search', views.view_notifi_search, name='view_notifi_search'),
    path('detailed_view_notifi', views.detailed_view_notifi, name='detailed_view_notifi'),
    path('viewdoubt_s', views.viewdoubt_s, name='viewdoubt_s'),
    path('viewcomplaint_search', views.viewcomplaint_search, name='viewcomplaint_search'),
    path('view_sys', views.view_sys, name='view_sys'),
    path('check_system/<int:id>', views.check_system, name='check_system'),
    path('kill_sy', views.kill_sy, name='kill_sy'),




    path('labassistanthome', views.labassistanthome, name='labassistanthome'),
    path('mngsystems', views.mngsystems, name='mngsystems'),
    path('addsystems', views.addsystems, name='addsystems'),
    path('addsystems_action', views.addsystems_action, name='addsystems_action'),
    path('dlt_system/<int:id>', views.dlt_system, name='dlt_system'),
    path('system_search',views.system_search,name='system_search'),
    path('edit_systems/<int:id>',views.edit_systems,name='edit_systems'),
    path('edit_systems_action',views.edit_systems_action,name='edit_systems_action'),
    path('view_students',views.view_students,name='view_students'),
    path('view_stud_search',views.view_stud_search,name='view_stud_search'),
    path('system_stud_allocation', views.system_stud_allocation, name='system_stud_allocation'),
    path('add_system_stud/<int:id>', views.add_system_stud, name='add_system_stud'),
    path('add_system_stud_action', views.add_system_stud_action, name='add_system_stud_action'),
    path('system_stud_search', views.system_stud_search, name='system_stud_search'),
    path('dlt_system_stud_allo/<int:id>', views.dlt_system_stud_allo, name='dlt_system_stud_allo'),
    path('edit_system_stud/<int:id>', views.edit_system_stud, name='edit_system_stud'),
    path('clear_system_stud_allo', views.clear_system_stud_allo, name='clear_system_stud_allo'),


    path('view_exam', views.view_exam, name='view_exam'),
    path('view_exam_search', views.view_exam_search, name='view_exam_search'),
    # path('view_students', views.view_students, name='view_students'),
    path('view_sub_staff_allocation', views.view_sub_staff_allocation, name='view_sub_staff_allocation'),
    path('view_sub_staff_search', views.view_sub_staff_search, name='view_sub_staff_search'),
    path('system_stud_allocation_s', views.system_stud_allocation_s, name='system_stud_allocation_s'),





    path('studenthome', views.studenthome, name='studenthome'),
    path('viewlabsub', views.viewlabsub, name='viewlabsub'),
    path('viewlabsub_search', views.viewlabsub_search, name='viewlabsub_search'),
    path('std_viewexam', views.std_viewexam, name='std_viewexam'),
    path('std_viewexam_search', views.std_viewexam_search, name='std_viewexam_search'),
    path('view_allocated_system', views.view_allocated_system, name='view_allocated_system'),
    path('view_system', views.view_system, name='view_system'),
    path('view_doubt_reply', views.view_doubt_reply, name='view_doubt_reply'),
    path('add_doubt', views.add_doubt, name='add_doubt'),
    path('add_doubt_action', views.add_doubt_action, name='add_doubt_action'),
    path('view_doubt_reply_search', views.view_doubt_reply_search, name='view_doubt_reply_search'),
    path('view_complaint_reply', views.view_complaint_reply, name='view_complaint_reply'),
    path('add_compl', views.add_compl, name='add_compl'),
    path('add_comp_action', views.add_comp_action, name='add_comp_action'),
    path('view_complaint_reply_search', views.view_complaint_reply_search, name='view_complaint_reply_search'),
    path('send_feedback', views.send_feedback, name='send_feedback'),
    path('send_feeds1', views.send_feeds1, name='send_feeds1'),
    path('stude_view_timetable', views.stude_view_timetable, name='stude_view_timetable'),
    path('logincode', views.logincode, name='logincode'),
    path('index', views.index, name='index'),






    path('dw', views.dw, name='dw'),
    path('select', views.select, name='select'),
    path('insprocess', views.insprocess, name='insprocess'),
    path('process', views.process, name='process'),
    path('sd', views.sd, name='sd'),
    path('rs', views.rs, name='rs'),
    path('bgp', views.bgp, name='bgp'),
    path('up', views.up, name='up'),
    path('up1', views.up1, name='up1'),


    path('kill_sy', views.kill_sy, name='kill_sy'),
    path('kill_pro/<int:id>/<str:pr>', views.kill_pro, name='kill_pro'),
    path('process_list/<int:id>', views.process_list, name='process_list'),
    path('screenshot', views.screenshot, name='screenshot'),
    path('restart', views.restart, name='restart'),
    path('shutdown', views.shutdown, name='shutdown'),




]
