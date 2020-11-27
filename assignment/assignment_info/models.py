from django.db import models
from django.conf import settings
from django.urls import reverse




class Course(models.Model):
    name=models.CharField(max_length=30,blank=False)
    code=models.CharField(max_length=10,unique=True)
    question=models.TextField(blank=False)
    question_file=models.FileField(blank=True,null=True)
    deadline_date=models.DateField(null=True)
    deadline_time =models.TimeField(null=True)

    def __str__(self):
        return "{}-{}".format(self.code,self.name)



class Submissions(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=1,related_name='submission')
    answer=models.FileField(upload_to='assignments')
    submitted_at=models.DateTimeField(auto_now=True,blank=False)


    def get_absolute_url(self):
        return reverse('assignments:list')

    def __str__(self):
        return "{}-{}".format(self.user.username,self.user.first_name+' '+self.user.last_name)
