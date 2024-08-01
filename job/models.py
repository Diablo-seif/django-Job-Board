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
        description= models.TextField(max_length=1000)
        published_at= models.DecimalField(max_digits=5, decimal_places=2)
        vacancy= models.IntegerField(default=1)
        salary= models.IntegerField(default=0)
        experience= models.IntegerField(default=1)
        category= models.ForeignKey(Category,on_delete=models.PROTECT)
        def __str__(self):
            return self.title


