# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import  AbstractBaseUser
from django.db.models.signals import post_save

class Student(models.Model):
    user = models.OneToOneField(User,unique=True)
    name = models.CharField(default="student",max_length=100)

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name




#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Student.objects.create(user=instance)

#post_save.connect(create_user_profile, sender=User)




class Course(models.Model):
    COM_NEED = 0
    COM_OPTION = 1
    PRO_NEED = 2
    PRO_OPTION = 3

    COURSE_TYPE =(
        (COM_NEED, u"公必"),
        (COM_OPTION, u"公选"),
        (PRO_NEED, u"专必"),
        (PRO_OPTION, u"专选"),
    )

    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    teacher = models.ForeignKey(Teacher)
    course_type = models.IntegerField(choices=COURSE_TYPE)

    def __unicode__(self):
        return self.course_name

    def like_set(self):
        return self.coursezan_set.filter(like=1)

class CourseZan(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    pub_date = models.DateTimeField('date publish', auto_now_add=True, blank=True)
    like = models.BooleanField(default=False)

    def __unicode__(self):
        if self.like:
            return self.student.name + " like " + self.course.course_name
        else:
            return self.student.name + " no like " + self.course.course_name


class Review(models.Model):
    course = models.ForeignKey(Course)
    review_text = models.CharField(max_length=200)
    student = models.ForeignKey(Student)
    pub_date = models.DateTimeField('date publish', auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.review_text

    def like_set(self):
        return self.reviewzan_set.filter(like=1)


class ReviewZan(models.Model):
    review = models.ForeignKey(Review)
    student = models.ForeignKey(Student)
    pub_date = models.DateTimeField('date publish', auto_now_add=True, blank=True)
    like = models.BooleanField(default=False)





