from django import forms

class MakeRoomForm(forms.Form):
    room_name = forms.CharField()
    room_suject = forms.CharField()
    limit_people = forms.ChoiceField()
    limit_date = forms.DateField()