
import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from word2number import w2n

from .forms import RegistrationForm,LoginForm
from django.contrib import messages

from .models import Loguser, Numconversion

# Create your views here.

def hello(request):
    return render(request,'hello.html')

def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                obj=Loguser.objects.get(username=username)
                if obj.password==password:
                    messages.success(request,' ')
                    return redirect('hello')
                else:
                    messages.error(request,'invalid password')
                    return redirect('login')
            except Loguser.DoesNotExist:
                messages.error('not a user')
                return redirect('login')

    else:
        form=LoginForm()  
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            obj=Loguser.objects.create(username=username,email=email,password=password)
            obj.save()
            messages.success(request,'registration was successfull')
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})


def converting(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get('text','').strip()
        if not text:
            return JsonResponse({'error': 'Please enter a number:'},status=400)
        try:
            result=w2n.word_to_num(text)
            conv=Numconversion.objects.create(textitem=text,numberres=result)
            return JsonResponse({"result":result})
        except ValueError:
            return JsonResponse({"error":"invalid input"},status=400) 
    return JsonResponse({"error":"invalid method"},status=400)



        
        
 