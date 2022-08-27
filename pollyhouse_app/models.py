
from django.db import models
from .views import *
# Create your models here.
# class State(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "State"

# class District(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="district")
#     name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "District"

# class Village(models.Model):
#     district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="village")
#     name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Village"
        


class SignUp(models.Model):
    name = models.CharField(max_length=100,default=None)
    phone_number = models.CharField(max_length=10,default=None)
    address = models.CharField(max_length=100,default=None)
    state = models.CharField(max_length=50,default=None)
    district = models.CharField(max_length=50,default=None)
    village = models.CharField(max_length=50,default=None)
    password =models.CharField(max_length=15,default=None)
    confirm_password =models.CharField(max_length=15,default=None)

    class Meta:
        verbose_name_plural = "Sign Up"

