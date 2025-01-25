from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_document = models.TextField()


