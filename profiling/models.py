from django.db import models

class Person(models.Model):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )

    name = models.CharField(max_length=255, verbose_name='Name')
    gender = models.CharField(max_length=255, verbose_name='Gender', choices=GENDER_CHOICES)
    birthdate = models.DateField(verbose_name="Birthdate")
    course = models.CharField(max_length=255, verbose_name='Course')