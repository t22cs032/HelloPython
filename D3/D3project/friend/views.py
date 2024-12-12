# friend/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import SeniorUser

def login_view(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = authenticate(request, userid=userid, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # ログイン後のリダイレクト先
        else:
            messages.error(request, 'Invalid userid or password')
    return render(request, 'friend/login.html')

def login_senior_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # パスワード確認の処理
        if password != confirm_password:
            messages.error(request, "パスワードが一致しません。")
            return redirect('login_senior')  # パスワード不一致時にリダイレクト

        # ユーザー認証または新規ユーザー作成処理
        try:
            senior_user = SeniorUser.objects.get(name=name, phone=phone, dob=dob)
            # ここでパスワードの検証などを行います
            if senior_user.password == password:
                messages.success(request, "ログイン成功！")
                # 必要なリダイレクト処理（例: ダッシュボード画面へ）
                return redirect("dashboard")
            else:
                messages.error(request, "パスワードが間違っています。")
        except SeniorUser.DoesNotExist:
            messages.error(request, "ユーザーが見つかりません。")

    return render(request, "friend/login_senior.html")