from django.db import models

# Create your models here.
class Room(models.Model):
    #room_name, room_subject, limit_people, limit_date
    room_title = models.CharField(null=False, max_length=30)
    room_content = models.CharField(null=False, max_length=2000)
    room_image = models.ImageField(null=True, upload_to="media")
    room_creater = models.CharField(null=False, max_length=100)
    room_date = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return f"{self.room_title}, {self.room_content}, {self.room_image}, {self.room_creater}, {self.room_date} creat!!"
    
class Review(models.Model):
    review_content = models.CharField(null=False, max_length=2000)
    review_creater = models.CharField(null=False, max_length=100)
    review_date = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f"{self.review_content}, {self.review_creater}, {self.review_date} creat!!"