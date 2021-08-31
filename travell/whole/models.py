
# from django.db import models
# from django.contrib import messages
# from django.contrib.auth.models import User
# class Product(models.Model):
#     name = models.CharField(max_length=100, null=True)
#
#     Tour_location = models.CharField(max_length=100, null=True)
#     Each_Person = models.CharField(max_length=100, null=True)
#     Hotel_For_Stay = models.CharField(max_length=100, null=True)
#     category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
#
#     image = models.ImageField(upload_to='static/uploads', blank=False, null=True)
#     price = models.CharField(max_length=50, null=True)
#
#     def __str__(self):
#         return self.name