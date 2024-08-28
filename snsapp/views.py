from django.shortcuts import render
from django.http import HttpResponse
# Djangoが準備してくれているユーザーモデルを読み込み
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def index(request):
    return HttpResponse('SNSのTOPページ')

# 新規登録画面
def signupfunc(request):
    # ページのデータ
    template = 'signup.html'
        
    # 登録フォームから受け取ったときの処理
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password) 
        except IntegrityError:
            data = {'error':'このユーザーは既に登録されています'}
            return render(request, template, data)
    
    data = {}
    return render(request, template, data)

# ログイン画面
def loginfunc(request):
    
    # ページのデータ
    template = 'login.html'
    data = {}
    return render(request, template, data)