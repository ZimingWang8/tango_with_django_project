from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Meta:
    verbose_name_plural = 'Categories'
    # unique=True ⇒ 字段名设置为唯一，意味着可以使用该字段作为主键

    def __str__(self):
        return self.name
    # 如果没有实现__str__()，它将显示为<Category: Category object>
    # __str__()就是Python中的toString()


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # CASCADE指令Django在类别被删除时删除与该类别相关的页面
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


