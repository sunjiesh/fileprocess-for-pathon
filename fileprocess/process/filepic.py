﻿# coding=utf-8

import commands
import os
import uuid

class GeneratePic():
    """
    文件生成图片列表
    """

    def enter(self, fieldsData):
        """
        处理程序入口，根据附件的类型，调用不同的方法
        """
        
        resultJson={}
        imageJsonArray=[]
        errorMsg=""
        
        picPath=fieldsData["picPath"]
        filePath=fieldsData["filePath"]
        
        if picPath=="":
            picPath="/tmp/"+str(uuid.uuid1()).replace("-", "")+"/"
        print "picPath="+picPath
        
        d = os.path.dirname(picPath)
        print(d)
        if not os.path.exists(d):
            print "mkdir "+picPath
            os.makedirs(d)
        
        
        fileType=filePath[filePath.rfind(".")+1:]
        fileType=fileType.lower()
        if fileType=="doc" or fileType=="docx":
            print "文件类型为DOC文件"
            pdfFilePath=self.docToPdf(picPath, filePath)
            if pdfFilePath!="":
                try:
                    print "convert image to dir %s"%pdfFilePath
                    exeCmd="convert %s %s/convert.png" %(pdfFilePath, picPath)
                    print "execute cmd "+exeCmd
                    status, output = commands.getstatusoutput(exeCmd)
                    if status==0:
                        for imageFile in os.listdir(picPath):
                            print picPath+"/"+imageFile
                            imageJsonArray.append(picPath+"/"+imageFile)
                except Exception, e:
                    print e
                    errorMsg="文件转换失败"
        else:
            errorMsg="文件暂时不支持转换为图片"
            print errorMsg
        
        resultJson["imageList"]=imageJsonArray
        resultJson["errorMsg"]=errorMsg
        print resultJson
        return resultJson
        
    def docToPdf(self,picPath,  file):
        """
            convert doc to pdf
        """
        if not (file is None):
            print "开始转换文件"
            try:
                pdfFileDir=file
                pdfFileDir=pdfFileDir.replace("\\", "/")
                pdfFileDir=pdfFileDir[0:pdfFileDir.rfind("/")]
                print "pdfFileDir="+pdfFileDir
                docFileName=file[file.rfind("/"):]
                print "docFileName="+docFileName
                pdfFileName=docFileName.replace(".docx", ".pdf")
                pdfFileName=pdfFileName.replace(".doc", ".pdf")
                status, output = commands.getstatusoutput("libreoffice --headless --convert-to pdf %s --outdir %s" %(file, pdfFileDir))
                if status==0:
                    print output
                    pdfFilePath=pdfFileDir+pdfFileName
                    print "pdfFilePath="+pdfFilePath
                    print "convert doc to pdf success"
                    return pdfFilePath
                else:
                    print output
            except Exception, e:
                print e
            print "转换文件结束"
            return ""