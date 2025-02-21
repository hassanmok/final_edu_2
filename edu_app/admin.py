from django.contrib import admin
from .models import User, Course, Comment, Random_problem

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Random_problem)
# Register your models here.
