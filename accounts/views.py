from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from photo.models import User
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':  # 회원가입 데이터 입력 완료 상황
        user_form = RegisterForm(request.POST)  # request.POST-사용자가 입력한 값
        if user_form.is_valid():  # 데이터 형식이 맞는지 확인, validation 호출
            new_user = user_form.save(commit=False)  # 해당 form 모델의 인스턴스를 얻어옴
            new_user.set_password(user_form.cleaned_data['password'])  # password
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:  # 회원가입 내용을 입력
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})

## 회원정보 수정
def member_modify(request):
    if request.method == "POST":
        id = request.user.id
        user = User.objects.get(pk=id)
        user = request.user
        user.username = request.POST["username"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.birthdate = request.POST["birthdate"]
        user.address = request.POST["address"]
        user.postal_code = request.POST["postal_code"]
        user.city = request.POST["city"]
        user.save()
        return redirect('photo:information')
    return render(request, 'registration/member_modify.html')



## 회원 탈퇴
def member_del(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'registration/member_del.html')