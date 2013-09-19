# coding=utf-8
# Create your views here.

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from filepic import GeneratePic

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
 
@csrf_exempt
def filetopic(request):
    """请求处理"""
    #读取请求
    print request.method
    if request.method == 'POST':
        jsonData=request.raw_post_data 
        print jsonData
        jsonData=json.loads(jsonData)
        requestId=jsonData["requestId"]
        requestId=str(requestId)
        fieldsData=jsonData["fields"]
        cls=GeneratePic()
        resultJson=cls.enter(fieldsData)
        resultJson["responseId"]=requestId
        print resultJson
        return HttpResponse(str(resultJson)) 
    return HttpResponse("Hello, world. You're at the pic index.") 
