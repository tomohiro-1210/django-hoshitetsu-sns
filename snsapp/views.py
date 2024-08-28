from django.shortcuts import render
from django.http import HttpResponse
# Djangoが準備してくれているユーザーモデルを読み込み
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse('SNSのTOPページ')

# 新規登録画面
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
    
    # ページのデータ
    template = 'signup.html'
    data = {}
    return render(request, template, data)

# ログイン画面
def loginfunc(request):
    
    # ページのデータ
    template = 'login.html'
    data = {}
    return render(request, template, data)