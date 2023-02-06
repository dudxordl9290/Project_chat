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

class Account(models.Model):
    chat_id = models.CharField(max_length=10)
    chat_pw = models.CharField(max_length=20)
    chat_email = models.EmailField()
    chat_info = models.CharField(max_length=1000, default="정보없음.")

    def __str__(self):
        return f"{self.chat_id}, {self.chat_pw}, {self.chat_email}, {self.chat_info} creat!!"