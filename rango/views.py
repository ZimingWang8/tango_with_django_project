from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 创建名为index的view
# 每个view至少会用到一个参数——一个HttpRequest对象，它存在于django.http模块
# 约定将其命名为request，但如果愿意，可以将其重命名为任何名称
def index(request):
    # 构造一个字典，作为上下文传递给模板引擎
    # context dictionary是一个将模板变量名boldmessage与Python变量映射在一起的Python字典
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # 返回一个render的响应发送给客户端，第一个参数是我们希望使用的模板
    # render()接受用户的请求、模板文件名和context dictionary作为输入。
    # render()函数将获取这些数据，并将其与模板结合在一起，以生成一个完整的HTML页面，该页面由一个HttpResponse返回。然后这个响应被返回并发送到用户的web浏览器。
    return render(request, 'rango/index.html', context=context_dict)


# 每个view必须返回一个HttpResponse对象。一个简单的HttpResponse对象接受一个字符串参数，该参数表示我们希望发送给请求视图的客户端的页面内容
def about(request):
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    context_dict = {'boldmessage': 'This tutorial has been put together by Ziming Wang'}
    return render(request, 'rango/about.html', context=context_dict)
