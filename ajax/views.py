import time

from django.contrib.auth.models import User
from django.http import StreamingHttpResponse
import cv2
import threading
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm

data = 0
lower_bound = (0, 0, 0)
upper_bound = (250, 250, 250)


# def contact_form(request):
#     global data
#     global lower_bound
#     global upper_bound
#     form = ContactForm()
#     if request.method == "POST" and request.accepts('media_type'):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # H_high = form.cleaned_data['H_high']
#             # S_high = form.cleaned_data['S_high']
#             # V_high = form.cleaned_data['V_high']
#             # H_low = form.cleaned_data['H_low']
#             # S_low = form.cleaned_data['S_low']
#             # V_low = form.cleaned_data['V_low']
#             # data = {"H_high": H_high, "S_high": S_high, "V_high": V_high,
#             #         "H_low": H_low, "S_low": S_low, "V_low": V_low}
#
#             return JsonResponse(data, status=200)
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({"errors": errors}, status=400)
#
#     H_high = request.GET.get('H_high')
#     S_high = request.GET.get('S_high')
#     V_high = request.GET.get('V_high')
#     H_low = request.GET.get('H_low')
#     S_low = request.GET.get('S_low')
#     V_low = request.GET.get('V_low')
#     if H_high is not None and S_high is not None and V_high is None \
#             and H_low is None and S_low is None and V_low is None:
#         lower_bound = (int(H_low), int(S_low), int(V_low))
#         upper_bound = (int(H_high), int(S_high), int(V_high))
#     return render(request, "contact_form.html", {"form": form})

def contact_form(request):
    global data
    global lower_bound
    global upper_bound

    H_high = request.GET.get('H_high')
    S_high = request.GET.get('S_high')
    V_high = request.GET.get('V_high')
    H_low = request.GET.get('H_low')
    S_low = request.GET.get('S_low')
    V_low = request.GET.get('V_low')
    print(H_high)
    try:
        lower_bound = (int(H_low), int(S_low), int(V_low))
        upper_bound = (int(H_high), int(S_high), int(V_high))
    except:
        lower_bound = (0, 0, 0)
        upper_bound = (250, 250, 250)

    return render(request, "ajax/contact_form.html",)


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

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        # cv2.waitKey(1)
        time.sleep(0.01)
        image_rabota = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # To HSV
        mask = cv2.inRange(image_rabota, lower_bound, upper_bound)
        image_mask = cv2.bitwise_and(image, image, mask=mask)
        _, jpeg = cv2.imencode('.jpg', image_mask)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
