from django.contrib import admin
from .models import Room, Review, ReReview

# Register your models here.
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(ReReview)