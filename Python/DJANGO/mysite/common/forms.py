from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('username','password1','password2','email')

# UserForm은 django.contrib.auth.forms 모듈의 UserCreationForm 상속하여 만든다.
# email 속성을 추가했다. 부가 속성을 추가/변경하여 사용하기 위해서는 상속을 사용한다. 






