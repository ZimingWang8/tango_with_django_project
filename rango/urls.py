from django.urls import path
from rango import views  # 允许我们调用函数url并指向urlpatterns中映射的index view

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
