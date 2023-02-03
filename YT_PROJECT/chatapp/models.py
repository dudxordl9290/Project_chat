from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Room(models.Model):
    #room_name, room_subject, limit_people, limit_date
    room_name = models.CharField(max_length=30)
    room_subject = models.CharField(max_length=100)
    limit_people = models.IntegerField(validators=[MinLengthValidator(2),MaxLengthValidator(20)])
    limit_date = models.IntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(10)])
    
    def __str__(self):
        return f"{self.room_name}, {self.room_subject}, {self.limit_people}, {self.limit_date} creat!!"