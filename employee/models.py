from base.base_model import *
from base.enum import Gender, Level
from jobs.models import Jobs
from major.models import Major
# Create your models here.
class Employee(Base):
    name = models.CharField(max_length=128, null=False)
    number = models.CharField(max_length=128, null=False)
    gender = models.CharField(
        choices=Gender.choices,
        null=False
    )
    age = models.IntegerField(null=False,)
    email = models.EmailField(max_length=254,null=False,)
    address = models.OneToOneField(Address, null=False, blank=False,
                                           on_delete=models.CASCADE, related_name='address')
    

    personal_introduction = models.CharField(max_lenght = 2000)

    level= models.CharField(
        choices=Level.choices,
        null=False
    )

    min_salary = models.DecimalField(max_digits=3, null=False)

    max_salary = models.DecimalField(max_digits=3, null=False)

    major = models.ManyToManyField(Major)

    prefer_jobs = models.ManyToManyField(Jobs)
