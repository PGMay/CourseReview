# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

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

def list(request):
    course_list = Course.objects.order_by('-pub_date')
    context = {'course_list': course_list}
    return render(request, 'course/pml/list1.html', context)


def listType(request, type):
    course_list = Course.objects.filter(course_type=type).order_by('-pub_date')
    context = {'course_list': course_list, 'course_type':type}
    return render(request, 'course/pml/list1.html', context)


@login_required
def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/pml/detail.html', {'course': course})

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

def courseZan(request):
    if request.is_ajax():
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except:
            return HttpResponse(u"你不是一个学生")

        course_id = request.POST.get("course_id")
        course = Course.objects.get(pk=course_id)
        if course is None:
            return  HttpResponse(u"无效的课程")

        zan = CourseZan.objects.get(course=course,student=student)

        like = request.POST.get('like')
        if zan is None:
            zan = CourseZan(course=course,student=student,like=like)
            zan.save()
        else:
            zan.like = like
            zan.save()
        return HttpResponse(json.dumps(True),content_type="application/json")

    return HttpResponse("")


def reviewZan(request):
    if request.is_ajax():
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except:
            return HttpResponse(u"你不是一个学生")

        review_id = request.POST.get("review_id")
        review = Review.objects.get(pk=review_id)
        if review is None:
            return  HttpResponse(u"无效的评论")

        zan = ReviewZan.objects.get(review=review,student=student)

        like = request.POST.get('like')
        if zan is None:
            zan = CourseZan(review=review,student=student,like=like)
            zan.save()
        else:
            zan.like = like
            zan.save()
        return HttpResponse(json.dumps(True),content_type="application/json")

    return HttpResponse("")


