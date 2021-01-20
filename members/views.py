from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def git(req):
    return HttpResponse("<h2>git version</h2>")
def gu(req):
    num = req.GET.get('num','')

    return HttpResponse(f"<h1> gugu : {num_gugu(num)} </h1>")

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i + 1)} <br>"
    return str

def login_after(req):
    user_id = req.session.get('user')

    if user_id:
        return HttpResponse(f"로그인 유저 {user_id}")

    return redirect("/login")

def logout(req):
    if req.session.get('user'):
        del(req.session['user'])

    return redirect("/")

def login(req):
    print(dir(req))
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username', None)
        useremail = req.POST.get('useremail', None)

    err = {}

    if not(useremail and username) :
        err['err'] = '유효성이 잘못되었습니다.'
        return render(req, 'login.html', err)

    else:
        member = Members.objects.get(username=username)

        if useremail == member.useremail :
            req.session['user'] = member.id
            return redirect('/members')
        else:
            err['err'] = "비밀번호가 잘못되었습니다."
            return render(req,"login.html", err)

        return HttpResponse(f"<h1>{member.useremail}</h1>")

    return redirect('/')

def index(request):
    return HttpResponse("<h1>version 1: dynamic page</h1>")

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
