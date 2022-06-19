from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Photo
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic


# Create your views here.

# class 형 뷰에서 decorator 를 사용할 때 오류가 나지 않도록 바꾸어줌.
# @login_required
@method_decorator(login_required, name='dispatch')
class PhotoListView(ListView):
    def get(self, request):
        photos = Photo.objects.all()
        return render(request, 'photo/list.html', {'photos': photos})




class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 현재 로그인한 사용자로 설정
        if form.is_valid():  # 입력된값검증
            form.instance.save()  # 이상 없으면 데이터베이스에 저장
            return redirect('photo:photo_list')   # community 메인으로 이동
        else:
            return self.render_to_response({'form': form})  # 이상이 있다면 작성된 내용을 그대로 작성페이지에 표시


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:photo_list')   # community 메인으로 이동
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


# 회원정보 뷰
# Generic 뷰 중 조건에 맞는 여러개의 객체를 보여주는 ListView 사용
@method_decorator(login_required, name='dispatch')
class informationView(generic.ListView):
    model = User  # User 을 model 값으로 지정
    fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'birthdate', 'address', 'postal_code', 'city']
    template_name = 'photo/information.html'  # information 페이지 경로


