from django.contrib import admin

# Register your models here.

from .models import Course,Review,Student,CourseZan, ReviewZan, Teacher

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Student)
admin.site.register(CourseZan)
admin.site.register(ReviewZan)
admin.site.register(Teacher)

