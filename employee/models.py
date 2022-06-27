from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=30)
    employee_id=models.IntegerField()

    def __str__(self):
        return self.firstname


