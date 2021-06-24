#coding=utf-8
import requests

url_code="http://{{dev}}/api/validation-code"
data={}
resp_code=requests.get(url_code,data=data)
a=print(resp_code.text)

# """url="http://39.97.99.199:80/api/user/captcha-login"
# data={
# "password":"5c0632515afb4f9fa7f9f60f964f2a5d",
# "remember":"0",
# "code":"8426",
# "phone":"12345678910"
#  "cookies"：“”
# }
# resp=requests.post(url,data=data)
# print(resp.text)
#
#
# import"""






