from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def gu(req):
    num = req.GET.get('num','')

    return HttpResponse(f"<h1> gugu : {num_gugu(num)} </h1>")

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i + 1)} <br>"
    return str
        



def index(request):
    return HttpResponse("<h1>version 1: dynamic page</h1>");

def test(req):
    return HttpResponse("<h2>Test</h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        #username == exit
        #h2로 나가기를 출력
        #if username == exit :
           # return HttpResponse("나가기")
        #elif username == 'codingon' :
            #return render(req, 'login.html')

        member = Members(
            username = username,
            useremail = email
        )

        member.save()
        res_data = {}

        
        res_data['res'] = '등록성공'

        return render(req, 'index.html', res_data)
    return render(req, 'index.html')
