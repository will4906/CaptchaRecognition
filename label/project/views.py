import os
import shutil

# import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


ab_path = "G:\Core\python\workspace\CaptchaRecognition\sipo2\source"
result_path = r"G:\Core\python\workspace\CaptchaRecognition\sipo2\result"


def index(request):
    if request.method == 'GET':
        file_name = os.listdir(ab_path)[0]
        whole_len = len(os.listdir(result_path))

    else:
        file_name = request.POST.get('file_name')
        value = request.POST.get('result')
        target_path = str(os.path.join(result_path, str(value).upper() + str('.png')))
        if os.path.exists(target_path):
            target_path = target_path.split('.')[0] + '_' + time.strftime('%Y%m%d',time.localtime(time.time())) + 'png'
        shutil.move(os.path.join(ab_path, file_name), target_path)
        file_name = os.listdir(ab_path)[0]
        whole_len = len(os.listdir(result_path))
    return render(request, 'index.html', context={'file_name': file_name, 'whole_len': whole_len})


def image(request):
    file_name = request.GET.get('file_name')
    with open(os.path.join(ab_path, file_name), 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')