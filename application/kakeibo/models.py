from django.db import models
from datetime import datetime

class Category(models.Model):

    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'

    category_name = models.CharField(verbose_name='カテゴリ', max_length=255, unique=True)

    def __str__(self):
        return self.category_name
    

class Kakeibo(models.Model):

    class Meta:
        verbose_name = '家計簿'
        verbose_name_plural = '家計簿'

    def _default_category():
        category, _ = Category.objects.get_or_create(category_name='その他')
        return category

    date = models.DateField(verbose_name='日付', default=datetime.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', default=_default_category, on_delete=models.SET_DEFAULT)
    money = models.IntegerField(verbose_name='金額', help_text='単位(円)')
    memo = models.CharField(verbose_name='用途', max_length=500)

    def __str__(self):
        return self.memo