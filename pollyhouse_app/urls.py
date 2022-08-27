from django.urls import path
from pollyhouse_app.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="login"),
    path('signup/',SignUp.as_view(), name = "signup")
]
