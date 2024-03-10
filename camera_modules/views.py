from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from . import camera
import cv2

__globalconfig = {"fps":30}

def home(request):
    if request.method == "POST":
        try:
            option = int(request.POST["performance"])
            # highfps
            if option == 0:
                __globalconfig["fps"] = 1000
            # balance
            elif option == 1: 
                __globalconfig["fps"] = 20
            # accurate
            elif option == 2: 
                __globalconfig["fps"] = 10
        except ValueError as e:
            pass
        return render(request, "index.html")
    else:
        return render(request, "index.html")


def __get_timing(fps):
    if fps > 1000 or fps <= 0:
        return 1
    return int(1000 / fps)


def __gen(camera: camera.webcam):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


def video(request):
    print(__globalconfig['fps'])
    mycam = camera.webcam(__globalconfig["fps"])
    return StreamingHttpResponse(
        __gen(mycam), content_type="multipart/x-mixed-replace; boundary=frame"
    )


def analyse(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        fss = FileSystemStorage(location=settings.MEDIA_ROOT)
        print(settings.MEDIA_ROOT)
        filename = fss.save(uploaded_file.name, uploaded_file)
        file_url = fss.url(filename)
        print(file_url)
        return render(request, "application.html", {"filename": "file_url"})
    return render(request, "application.html")
