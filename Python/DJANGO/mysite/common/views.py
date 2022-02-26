from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.


def signup(request):
    """
    계정 생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)#사용자 인증
            login(request, user) # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})




# signup함수는 POST 요청인 경우 화면에서 입력한 데이터로 사용자를 생성하고
# get 요청인 경우는 계정 생성 화면을 리턴한다. 

# 신규 사용자를 생성한 후에 자동 로그인이 될수 있도록 한다. 
# authenticate 함수는 사용자명과 비번이 정확히 일치하는지 확인