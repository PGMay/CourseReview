# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db.models import  Count

import  json


from .models import Course, Review, Student, CourseZan, ReviewZan

# Create your views here.

def index(request):
    if request.is_ajax():
        if not request.POST.get("username"):
            return HttpResponse(u"请输入学号")
        username = request.POST.get("username")
        if not request.POST.get("password"):
            return HttpResponse(u"请输入密码")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {}
            data['url'] = "/course/list";
            return HttpResponse(json.dumps(data),content_type="application/json")
        else:
            return HttpResponse(u"账号密码错误")

    return render(request, 'course/pml/index.html')
@login_required
def list(request):
    course_list = Course.objects.order_by('-pub_date')
    user = request.user
    try:
        student = Student.objects.get(user=user)
    except:
        return HttpResponse('system error')
    course_list_user = []
    for i in range(0,len(course_list)):
        like = course_list[i].coursezan_set.filter(student=student,like=1).count()
        course_list_user.append([course_list[i],like])
    getHotCourse()
    hotCourse = getHotCourse()
    context = {
        'course_list': course_list_user,
        'cc':student,
        'hotCourse':hotCourse
    }
    return render(request, 'course/pml/list1.html', context)

def getHotCourse():
    top_courses = Course.objects.annotate(num_hot=Count('review')).order_by('-num_hot')[:5]
    return top_courses


@login_required
def listType(request, type):
    course_list = Course.objects.filter(course_type=type).order_by('-pub_date')
    user = request.user
    try:
        student = Student.objects.get(user=user)
    except:
        return HttpResponse('system error')
    course_list_user = []

    for course in course_list:
        like = course.coursezan_set.filter(student=student,like=1).count()
        course_list_user.append([course, like])
    hotCourse = getHotCourse()
    context = {'course_list': course_list_user, 'course_type':type,'hotCourse':hotCourse}
    return render(request, 'course/pml/list1.html', context)


@login_required
def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    try:
        student = Student.objects.get(user=user)
    except:
        return HttpResponse('system error')
    review_list_user = []
    for review in course.review_set.all():
        like = review.reviewzan_set.filter(student=student,like=1).count()
        review_list_user.append([review,like])
    return render(request, 'course/pml/detail.html', {'course': course,'reviewList':review_list_user,'hotCourse':getHotCourse()})

@login_required
def bye(request):
    logout(request)
    return HttpResponseRedirect("/course")

@login_required
def addReview(request):
    if request.is_ajax():
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except:
           return HttpResponse(u"你不是一个学生")

        review_text = request.POST.get("review_text")
        if review_text is None:
            return HttpResponse(u"评论不能为空")

        course_id = request.POST.get("course_id")
        course = Course.objects.get(pk=course_id)
        if course is None:
            return HttpResponse(u"无效的课程")
        a = Review(course=course,student=student,review_text=review_text)
        a.save()
        data = {}
        data['username'] = a.student.name
        desired_format = '%Y年%m月%d日%H:%M'
        data['pub_date'] = a.pub_date.strftime(desired_format)
        data['review_text'] = a.review_text
        return HttpResponse(json.dumps(data),content_type="application/json")

    return HttpResponse("nothing")

@login_required
def courseZan(request):
    if request.is_ajax():
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except:
            return HttpResponse(u"你不是一个学生")

        course_id = request.POST.get("course_id")
        course = Course.objects.get(pk=course_id)
        like = request.POST.get('like')
        if course is None:
            return  HttpResponse(u"无效的课程")

        zanList = CourseZan.objects.filter(course=course,student=student)

        if len(zanList) == 0 :
            zan = CourseZan(course=course,student=student,like=like)
            zan.save()
        else:
            zan = zanList[0]
            if like == '1':
                zan.like = True
            else:
                zan.like = False
            zan.save()



        return HttpResponse(json.dumps(True),content_type="application/json")

    return HttpResponse("")

@login_required
def reviewZan(request):
    if request.is_ajax():
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except:
            return HttpResponse(u"你不是一个学生")

        review_id = request.POST.get("review_id")
        review = Review.objects.get(pk=review_id)
        like = request.POST.get('like')
        if review is None:
            return  HttpResponse(u"无效的评论")

        zanList = ReviewZan.objects.filter(review=review,student=student)

        if len(zanList) == 0 :
            zan = ReviewZan(review=review,student=student,like=like)
            zan.save()
        else:
            zan = zanList[0]
            if like == '1':
                zan.like = True
            else:
                zan.like = False
            zan.save()
        return HttpResponse(json.dumps(True),content_type="application/json")

    return HttpResponse("")


