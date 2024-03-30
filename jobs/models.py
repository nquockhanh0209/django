from base.base_model import *
from major.models import Major
from base.enum import  Level
# Create your models here.
class Jobs(Base):
    name = models.CharField(max_length=128, null=False)
    expired_time = models.DateTimeField(null= False)
    salary = models.DecimalField(max_digits=3, null=False)
    description = models.CharField(max_lenght = 2000)
    level= models.CharField(
        choices=Level.choices,
        null=False
    )
    major = models.ManyToManyField(Major)  


