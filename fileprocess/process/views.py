#coding=utf-8
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
    return HttpResponse("Hello, world. You're at the pic index,Please use post method") 

@csrf_exempt
def getPic(request):
    """Get Pic File"""
    if request.method=='POST':
        jsonData=request.raw_post_data 
        print jsonData
        jsonData=json.loads(jsonData)
        requestId=jsonData["requestId"]
        requestId=str(requestId)
        fieldsData=jsonData["fields"]
        picPath=fieldsData["picPath"]
        if picPath!="":
            try:
                def readFile(fn, buf_size=262144):
                    f = open(fn, "rb")
                    while True:
                        c = f.read(buf_size)
                        if c:
                            yield c
                        else:
                            break
                    f.close()
                response = HttpResponse(readFile(picPath), mimetype='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' %picPath
                return response
            except Exception, e:
                print e
        
    return HttpResponse("Hello, world. You're at the getPic ,Please use post method") 
        
