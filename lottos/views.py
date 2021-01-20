from django.shortcuts import render
from django.http.response import HttpResponse
import random

def login_after(req):
    return HttpResponse("세션읽기 & 세션 없으면 리다이렉션") 
    
# Create your views here.
def index(req):
    req.GET.get('num', '')
    if req.method == 'GET':
        lotto = []
        while len(lotto) < 6:
            lotto.append(random.randint(1,45))
            lotto = list(set(lotto))#print(lotto)
        return HttpResponse(f"<h1>lotto 번호 추천 { lotto }</h1>")

    return HttpResponse("post")