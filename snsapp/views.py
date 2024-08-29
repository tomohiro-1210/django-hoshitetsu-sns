from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Djangoが準備してくれているユーザーモデルを読み込み
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PostModel
from django.views.generic import CreateView
from django.urls import reverse_lazy


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
    return render(request, template, data)

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
            return redirect('list')
            # data = {'context':'ログイン完了！'}
            # return render(request, template, data)
        else:
            data = {'context':'ログインができませんでした'}
            return render(request, template, data)
        
    data = {}
    return render(request, template, data)

# ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')
    
# 一覧表示
@login_required
def listfunc(request):
    # ページのデータ
    template = 'list.html'
    
    # DBからの読み込み
    object_list = PostModel.objects.all()
    
    # データの読み込み
    data={'object_list':object_list}
    return render(request, template, data)

# 詳細表示
@login_required
def detailfunc(request, pk):
    # ページのデータ
    template = 'detail.html'
    
    # モデル
    object = get_object_or_404(PostModel, pk=pk)
    
    # データの読み込み
    data={'object':object}
    return render(request, template, data)

# いいね
@login_required
def goodfunc(request, pk):
    # データの読み込み
    object = PostModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')
    
# 既読
@login_required
def readfunc(request, pk):
    # データの読み込み
    object = PostModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readname:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readname = object.readname + ', ' + username
        object.save()
        return redirect('list')
    
# 投稿画面
class PostCreateView(CreateView):
    model = PostModel
    template_name = 'create.html'
    fields = ['title' ,'text', 'author', 'thumbnail']
    success_url = reverse_lazy('list')
    