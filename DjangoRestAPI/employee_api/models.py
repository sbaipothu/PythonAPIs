# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employees(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Course(models.Model):
    courseid = models.IntegerField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits')  # Field name made lowercase.
    departmentid = models.ForeignKey('Department', models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Courseinstructor(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CourseInstructor'
        unique_together = (('courseid', 'personid'),)


class Department(models.Model):
    departmentid = models.IntegerField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    budget = models.DecimalField(db_column='Budget', max_digits=19, decimal_places=4)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    administrator = models.IntegerField(db_column='Administrator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Department'


class Officeassignment(models.Model):
    instructorid = models.OneToOneField('Person', models.DO_NOTHING, db_column='InstructorID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    timestamp = models.TextField(db_column='Timestamp')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OfficeAssignment'


class Onlinecourse(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineCourse'


class Onsitecourse(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnsiteCourse'


class Person(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    enrollmentdate = models.DateTimeField(db_column='EnrollmentDate', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Studentgrade(models.Model):
    enrollmentid = models.AutoField(db_column='EnrollmentID', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.
    studentid = models.ForeignKey(Person, models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    grade = models.DecimalField(db_column='Grade', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentGrade'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
