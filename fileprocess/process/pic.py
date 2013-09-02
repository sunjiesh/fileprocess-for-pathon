
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
            self.docToPic(picPath, filePath)
        else:
            print "文件暂时不支持转换为图片"

    def docToPic(self,picPath,  file):
        """
            doc文件转换图片
        """
        if not (file is None):
            print "开始转换文件"
            print "转换文件结束"
