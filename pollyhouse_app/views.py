from audioop import add
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *

class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")


class SignUp(View):
    def get(self, request):
        return render(request,"signup.html")

    def post(self, request):
        if request.method=="POST":
            #avatar = request.FILES.get('user_image')
            name = request.POST.get("name")
            phone_number = request.POST.get("phone_number")
            address = request.POST.get("address")
            state = request.POST.get('state')
            district = request.POST.get('district')
            village = request.POST.get('village')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            # user = SignUp.objects.all()
            print(name,phone_number,address)
            
            SignUp(name=name, phone_number=phone_number, address=address, state=state, district=district, village=village, password=password ,confirm_password=confirm_password).save()
            SignUp.save()
        # user.name=name
        # user.phone_number=phone_number
        # user.address=address
        # # user_save = state=state
        # # user_save = district=district
        # # user_save = village=village
        # # user_save = password=password
        # # user_save = confirm_password=confirm_password
        # user.save()
    
        return redirect(request, "login.html")

   