from django.db import models

class SeniorUser(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()  # 生年月日
    phone = models.CharField(max_length=15)  # 電話番号
    password = models.CharField(max_length=255)  # パスワード（仮）
    
    def __str__(self):
        return self.name
