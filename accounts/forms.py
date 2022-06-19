from photo.models import User
from django import forms

class RegisterForm(forms.ModelForm):

    # 비밀번호 입력받기 위한 필드를 생성, widget을 다음처럼 지정하면 비밀번호가 *로 표시됨
    # 아래처럼 필드를 별도로 정의하는 것은 Meta class 내의 fields에 추가하는 것과 동일하게 동작함
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput) #다시한번 입력

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'birthdate', 'address', 'postal_code', 'city']

        #clean_필드명() : 필드의 validation 방법 지정
        def clean_password2(self):
            cd = self.clean_data # clean_data : 유효성 검사를 마친 후의 데이터
            if cd['password']!=cd['password2']:
                raise forms.ValidationError
            return cd['password2']  # 해당 필드의 데이터를 return하도록 구현
