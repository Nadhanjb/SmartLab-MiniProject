from django.db import models


class login_table(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class dept_table(models.Model):
    dept_name=models.CharField(max_length=50)
    details=models.TextField()

class course_table(models.Model):
    DEPARTMENT= models.ForeignKey(dept_table,on_delete=models.CASCADE)
    course=models.CharField(max_length=35)
    details = models.TextField()
    sem=models.IntegerField()

class labsubject_table(models.Model):
    COURSE=models.ForeignKey(course_table, on_delete=models.CASCADE)
    subject=models.CharField(max_length=35)
    syllabus=models.TextField()

class system_table(models.Model):
    system_id=models.IntegerField()
    processor=models.TextField()
    RAM=models.TextField()
    HDD=models.TextField()
    SSD=models.TextField()
    date=models.DateField()


class staff_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    COURSE=models.ForeignKey(course_table,on_delete=models.CASCADE)
    gender=models.CharField(max_length=35)
    dob=models.DateField()
    place=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    qualification=models.TextField()
    programming_lang=models.CharField(max_length=100)
    photo=models.FileField()

class lab_assistant_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender=models.CharField(max_length=35)
    dob=models.DateField()
    place=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    photo=models.FileField()

class student_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    COURSE=models.ForeignKey(course_table,on_delete=models.CASCADE)
    semester=models.CharField(max_length=20)
    gender=models.CharField(max_length=35)
    dob=models.DateField()
    place=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    photo=models.FileField()


class exam_table(models.Model):
    SUBJECT = models.ForeignKey(labsubject_table,on_delete=models.CASCADE)
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    exam_name=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    duration=models.CharField(max_length=50)
    details=models.CharField(max_length=1000)
    syllabus=models.CharField(max_length=1000)


class doubt_table(models.Model):
    STUDENT=models.ForeignKey(student_table,on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    doubt=models.TextField()
    date=models.DateField()
    reply=models.TextField()
    image=models.FileField()


class complaint_table(models.Model):
    STUDENT=models.ForeignKey(student_table,on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    complaint=models.TextField()
    date=models.DateField()
    reply=models.TextField()

class system_stud_allo_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    SYSTEM=models.ForeignKey(system_table, on_delete=models.CASCADE)

class sub_staff_allo_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    SUBJECT = models.ForeignKey(labsubject_table,on_delete=models.CASCADE)

class staff_lab_allocatio(models.Model):
    SUBJECT_STAFF= models.ForeignKey(sub_staff_allo_table, on_delete=models.CASCADE)
    day=models.CharField(max_length=50)
    period=models.CharField(max_length=30)

class student_feedback(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    feedback = models.TextField()
    datetime=models.DateTimeField()


class notification_table(models.Model):
    SYSTEM = models.ForeignKey(system_table, on_delete=models.CASCADE)
    screenshot=models.FileField()
    camera_image=models.FileField()
    timedate=models.DateTimeField()
    status=models.CharField(max_length=50)



class command(models.Model):
    SYSTEM=models.ForeignKey(system_table,on_delete=models.CASCADE)
    process=models.CharField(max_length=100)

class process(models.Model):
    SYSTEM=models.ForeignKey(system_table,on_delete=models.CASCADE)
    process=models.CharField(max_length=100)

class screenshot(models.Model):
    SYSTEM=models.ForeignKey(system_table,on_delete=models.CASCADE)
    scrnsht=models.FileField()
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)