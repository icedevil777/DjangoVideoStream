from django.urls import path
from .views import contact_form, video_one

urlpatterns = [
    path('', contact_form, name='contact_form'),
    path('video_one', video_one, name='video_one'),
]