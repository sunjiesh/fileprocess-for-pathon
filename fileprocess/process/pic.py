import commands

class GeneratePic():
    """
    文件生成图片列表
    """

    def enter(self, fieldsData):
        """
        处理程序入口，根据附件的类型，调用不同的方法
        """
        fileType=fieldsData["fileType"]
        picPath=fieldsData["picPath"]
        filePath=fieldsData["filePath"]
        fileType=fileType.lower()
        if fileType=="doc":
            print "文件类型为DOC文件"
            pdfFilePath=self.docToPdf(picPath, filePath)
            print "pdfFilePath="+pdfFilePath
        else:
            print "文件暂时不支持转换为图片"

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
                status, output = commands.getstatusoutput("libreoffice --headless --convert-to pdf %s --outdir %s" %(file, pdfFileDir))
                if status==0:
                    print "convert doc to pdf success"
                    return pdfFileDir+docFileName
                else:
                    print output
            except Exception, e:
                print e
            print "转换文件结束"
