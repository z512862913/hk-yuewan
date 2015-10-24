from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label=('username'),max_length=200)
    password = forms.CharField(label=('password'),max_length=200,widget=forms.PasswordInput)
    password2 = forms.CharField(label=('confirm'),max_length=200,widget=forms.PasswordInput)
    email = forms.EmailField(label=('email'),max_length=200)
    def pwd_validate(self,p1,p2):
        return p1==p2

class LoginForm(forms.Form):
	username = forms.CharField(label=('Username'))
	password = forms.CharField(label=('Password'),widget=forms.PasswordInput)

class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label=('old password'),max_length=200,widget=forms.PasswordInput)
    new_pwd = forms.CharField(label=('new password'),max_length=200,widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label=('confirm new password'),max_length=200,widget=forms.PasswordInput)

class BlogText(forms.Form):
	title = forms.CharField(label=('title'))
	content = forms.CharField(label=('content'),widget=forms.Textarea)
	StartTime = forms.DateTimeField(label=('StartTime'))
	EndTime = forms.DateTimeField(label=('EndTime'))	

class Edit(forms.Form):
	title = forms.CharField(label=('title'))
	content = forms.CharField(label=('content'),widget=forms.Textarea)
