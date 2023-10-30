from django.db import models

# Create your models here.

class Position(models.Model):
    SENIOR_DEVELOPER = ''
    DATA_ANALYST = ''
    MANAGER = ''

    TITLE_CHOICES = [
        (SENIOR_DEVELOPER, 'Senior Developer'),
        (DATA_ANALYST, 'Data Analyst'),
        (MANAGER, 'Manager'),
    ]

    title = models.CharField(max_length=100, choices=TITLE_CHOICES)

    def __str__(self):
        return self.title




class Emoplyee(models.Model):
    FullName= models.CharField(max_length=100)
    emp_code= models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
