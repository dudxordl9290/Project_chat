from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from chatapp.models import Room, Review
from datetime import datetime

@login_required
def make_review(request, pk):
    if request.method == 'POST':
        review_content = request.POST['review_content']
        review_date = datetime.today().strftime("%Y/%m/%d %H:%M:%S")

        Review.objects.create(review_room=pk, review_content=review_content, review_creater=request.user, review_date=review_date)
    
    return redirect(f'/detail_room/{pk}/')

def delete_review(request, pk, id):
    review_info = Review.objects.filter(review_room=pk, id=id)
    review_info.delete()

    return redirect(f'/detail_room/{pk}/')