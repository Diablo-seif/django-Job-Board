from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.name

class Job(models.Model):
        JOB_TYPE = (
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        )
        title= models.CharField(max_length=50)
        # location
        job_type= models.CharField(max_length=50,choices=JOB_TYPE)
        description= models.TextField(max_length=10000 )
        responsibility= models.TextField(max_length=10000 )
        qualifications= models.TextField(max_length=10000 )
        benefits= models.TextField(max_length=10000 )
        published_at = models.DateTimeField(auto_now=True)
        vacancy= models.IntegerField(default=1)
        salary= models.IntegerField(default=0)
        experience= models.IntegerField(default=1)
        category= models.ForeignKey(Category,on_delete=models.PROTECT)
        image=models.ImageField(upload_to='job/%Y/%m/%d')
        def __str__(self):
            return self.title


