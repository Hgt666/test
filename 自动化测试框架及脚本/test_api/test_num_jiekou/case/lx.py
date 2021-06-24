import os
import xlrd
import xlwt
from faker import Faker
import pytest

# ff=Faker("zh_CN")
# l = []
# for i in range(10):
#     l.append(ff.phone_number())
#     print("电话号码",ff.phone_number())
#
# print(l)

def data_1():
    ff=Faker("zh_CN")
    l=[]
    for i in range(10):
        l.append(ff.phone_number())
        print("电话",ff.phone_number())

    a=xlwt.Workbook()
    sheet1=a.add_sheet("号码表",cell_overwrite_ok=True)
    row0=["序号","号码"]
    col0=["1",l]
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])

    for i in range(0,len(col0)):
        sheet1.write(i+1,0,col0[i])
    a.save("t0e_data.xlsx")

if __name__=="__main__":
    data_1()