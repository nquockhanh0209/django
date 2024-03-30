from base.base_model import *
from jobs.models import Jobs
# Create your models here.
class Major(Base):
    name = models.CharField(max_length=128, null=False)
    jobs = models.ManyToManyField(Jobs)
    


