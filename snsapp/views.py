from django.shortcuts import render, redirect
from django.http import HttpResponse
# Djangoが準備してくれているユーザーモデルを読み込み
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import PostModel

# Create your views here.
def index(request):
    return HttpResponse('SNSのTOPページ作らなくてはな。')

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
            return redirect('login')
        except IntegrityError:
            data = {'error':'このユーザーは既に登録されています'}
            return render(request, template, data)
    
    data = {}
    return redirect('login')

# ログイン画面
def loginfunc(request):
    # ページのデータ
    template = 'login.html'
    
    # ログイン処理
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 認証？
        user = authenticate(request, username=username, password=password)
        # ユーザがいるかいないか
        if user is not None:
            login(request, user)
            return redirect('top')
            # data = {'context':'ログイン完了！'}
            # return render(request, template, data)
        else:
            data = {'context':'ログインができませんでした'}
            return render(request, template, data)
        
    return redirect('top')

# ログアウト
def logoutfunc(request):
    HttpResponse('ログアウト')
    
# 一覧表示
def listfunc(request):
    # ページのデータ
    template = 'list.html'
    
    object_list = PostModel.objects.all()
    
    # データの読み込み
    data={'object_list':object_list}
    return render(request, template, data)