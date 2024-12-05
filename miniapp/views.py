
import json
from django.http import JsonResponse
from django.shortcuts import render
from word2number import w2n

from .models import Numconversion

# Create your views here.

def hello(request):
    return render(request,'hello.html')


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
        
    return JsonResponse({"error":"invalid method"})

