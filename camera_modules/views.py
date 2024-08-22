from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from . import camera
from datetime import datetime
import cv2
import re
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
    return render(request, "application.html")

def sanitize(filename):
    # not_of(\w\s.-), \w = alphanumeric+_ \s = space, . = pullstop, - = hyphen
    filename = re.sub(r'[^\w\s.-]*',"", filename).strip().lower()
    filename = re.sub(r'[-\s]+',"_", filename)
    filename = re.sub(r'(\.)+',".", filename)
    return filename

def upload_handler(request):
    print("SAVING FILES...")
    if request.method == "POST" and request.FILES.get("files"):
        file_urls = []
        file_names = []
        fss = FileSystemStorage(location=settings.MEDIA_ROOT)
        for uploaded_file in request.FILES.getlist("files"):
            # %d for date %m form month %Y for year %M for minute ... read the references
            # our file must not contain :/\* symbols
            current_date_time = str(datetime.now().strftime("%d_%m_%Y_%H%M%S_"))
            file_name = current_date_time+sanitize(uploaded_file.name)
            file_names.append(file_name)
            saved_file = fss.save(file_name, uploaded_file)
            url = fss.url(saved_file)
            file_names.append(url)

        #debug
        print(fss.base_url)
        print(fss.base_location)
        print(fss.location)
        print(file_names)
        return render(request, "done.html", {"file_urls":file_urls, "file_names":file_names})
    return render(request, "application.html")