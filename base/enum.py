from django.db import models

class Gender(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"


class Level(models.TextChoices):
    INTERN = "Intern"
    FRESHER = "Fresher"
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    MANAGER = "Manager"
    CHIEF = "Chief"
