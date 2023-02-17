from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 创建名为index的view
# 每个view至少会用到一个参数——一个HttpRequest对象，它存在于django.http模块
# 约定将其命名为request，但如果愿意，可以将其重命名为任何名称
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")


# 每个view必须返回一个HttpResponse对象。一个简单的HttpResponse对象接受一个字符串参数，该参数表示我们希望发送给请求视图的客户端的页面内容
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
