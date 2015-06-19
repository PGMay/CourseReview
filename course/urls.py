from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^index/$', views.index, name="index"),
    url(r'^list/$', views.list, name="list"),
    url(r'^list/(?P<type>[0-9]+)/$', views.listType, name="listType"),
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'bye/$',views.bye, name="bye"),


    url(r'^addReview/$', views.addReview, name="addReview"),

    url(r'^courseZan/$', views.courseZan, name="courseZan"),
    url(r'^reviewZan/$', views.reviewZan, name="reviewZan"),

     # url(r'^([0-9]+)/$','django.contrib.auth.views.login')
]