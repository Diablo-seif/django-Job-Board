from django.db import models
from django.utils.text import slugify


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
        job_type = models.CharField(max_length=50,choices=JOB_TYPE)
        description = models.TextField(max_length=10000 )
        responsibility = models.TextField(max_length=10000 )
        qualifications = models.TextField(max_length=10000 )
        benefits = models.TextField(max_length=10000 )
        published_at = models.DateTimeField(auto_now=True)
        vacancy = models.IntegerField(default=1)
        salary = models.IntegerField(default=0)
        experience = models.IntegerField(default=1)
        category = models.ForeignKey('Category',on_delete=models.PROTECT)
        image =models.ImageField(upload_to='job/%Y/%m/%d')
        slug = models.SlugField(blank=True, null=True)

        def save(self, *args, **kwargs):
             self.slug=slugify(self.title)
             super(Job, self).save(*args, **kwargs)
        def __str__(self):
            return self.title


class Apply (models.Model):
        job= models.ForeignKey(Job, related_name='apply_job', on_delete=models.PROTECT)
        name= models.CharField(max_length=50)
        email= models.EmailField(max_length=100)
        website= models.URLField()
        cv= models.FileField(upload_to='apply')
        letter= models.TextField(max_length=500 )
        caret_add = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
