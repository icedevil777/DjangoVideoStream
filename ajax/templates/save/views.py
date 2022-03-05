from django.http import StreamingHttpResponse
import cv2
import threading
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm
import numpy as np

def contact_form(request):
    form = ContactForm()
    if request.method == "POST" and request.accepts('media_type'):  #.accepts(), is_ajax()
        form = ContactForm(request.POST)
        if form.is_valid():
            S_high = form.cleaned_data['S_high']
            H_high = form.cleaned_data['H_high']
            V_high = form.cleaned_data['V_high']
            H_low = form.cleaned_data['H_low']
            S_low = form.cleaned_data['S_low']
            V_low = form.cleaned_data['V_low']
            # form.save()
            data = {"S_high": S_high, "H_high": H_high, "V_high": V_high,
                    "H_low": H_low, "S_low": S_low, "V_low": V_low}
            print(data)
            return JsonResponse(data, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "contact_form.html", {"form": form})


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_one(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

        _f = cv2.medianBlur(self.frame, 15)
        _f = cv2.cvtColor(_f, cv2.COLOR_BGR2HSV)  # To HSV

        # define range of color in HSV
        # data = contact_form()


        # lower_bound = np.array([self.H_low, self.S_low, self.V_low])
        # upper_bound = np.array([self.H_high, self.S_high, self.V_high])

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
