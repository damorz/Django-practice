from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=60)
    subject_code = models.CharField(max_length=10)

class Todo(models.Model):
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField('date deadline')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

