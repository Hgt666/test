import time
import os
import unittest
import HTMLTestRunner

def all_case():
    casePath=os.getcwd()+"\\case"
    discover=unittest.defaultTestLoader.discover(casePath,pattern="test*.py")
    return discover

if __name__=="__main__":
    nowtime=time.strftime("%Y%m%d%H%M%S")
    reportPath=os.getcwd()+"\\report"+"report_"+nowtime+".html"
    ff=open(reportPath,"wb")
    HTMLTestRunner.HTMLTestRunner(ff,title="号码管理系统接口自动化测试",description="详情如下:").run(all_case())