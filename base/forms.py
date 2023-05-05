from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, required=True, label='Tài khoản')
    password = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')

    def clean(self):
        super(LoginForm, self).clean()


        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        auth = authenticate(username=username, password=password)
        if auth == None:
            self._errors['username'] = self.error_class(['Tài khoản hoặc mật khẩu sai'])
        return self.cleaned_data
    

class RegisterForm (forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='Tên')
    last_name = forms.CharField(max_length=50, required=True, label='Họ')
    username = forms.CharField(max_length=100, required=True, label='Tài khoản')
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100, label='Mật khẩu')
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100, label='Mật khẩu xác nhận')

    def clean(self):
        super(RegisterForm, self).clean()

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if len(username) < 3:
            self._errors['username'] = self.error_class(['Ký tự tài khoản không thể ít hơn 3'])
        if len(password) < 6:
            self._errors['password'] = self.error_class(['Mật khẩu có ít nhất 6 ký tự trở lên'])
        if self.cleaned_data.get('confirm_password') != self.cleaned_data.get('password'):
            self._errors['confirm_password'] = self.error_class(['Mật khẩu xác nhận phải giống với mật khẩu'])
        if User.objects.all().filter(username=username):
            self._errors['username'] = self.error_class(['Tài khoản đã được sử dụng'])
        try:
            int(password)
            self._errors['password'] = self.error_class(['Mật khẩu phải có it nhất một ký tự'])
        except:
            pass
        return self.cleaned_data
