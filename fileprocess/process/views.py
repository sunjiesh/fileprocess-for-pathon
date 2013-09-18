# Create your views here.

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pic import GeneratePic

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
 
@csrf_exempt
def pic(request):
    """请求处理"""
    #读取请求
    print request.method
    if request.method == 'POST':
        jsonData=request.raw_post_data 
        print jsonData
        jsonData=json.loads(jsonData)
        fieldsData=jsonData["fields"]
        cls=GeneratePic()
        cls.enter(fieldsData)
    return HttpResponse("Hello, world. You're at the pic index.") 
