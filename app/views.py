from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.


def index(request):
    return render(request, 'app.html')


def login(request):
    json_obj = json.loads(request.body)
    user = json_obj['username']
    pwd = json_obj['password']
    if(user == 'user1' or user == 'user2' or user== 'user3'):
        if(pwd == 'abc123321'):

            return JsonResponse({"Status" : "OK"}, safe=False)


    return JsonResponse({"Status": "ERROR"}, safe=False)