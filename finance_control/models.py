from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Доход'),
        ('expense', 'Расход'),
    ]

    CATEGORY_CHOICES = [
        ('salary', 'Зарплата'),
        ('deposit', 'Проценты по вкладу'),
        ('transfer', 'Перевод'),
        ('business', 'Бизнес'),

        ('food', 'Продукты'),
        ('transport', 'Транспорт'),
        ('utilities', 'Коммунальные услуги'),
        ('rent', 'Аренда'),
        ('clothes', 'Одежда'),
        ('fun', 'Развлечения'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
