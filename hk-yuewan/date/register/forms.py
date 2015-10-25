#coding:utf-8

from django import forms

class userForm(forms.Form):
	username = forms.CharField(label = u'用户名', max_length = 10, required = True, widget = forms.TextInput())
	realname = forms.CharField(label = u'真实姓名', max_length = 10, required = True, widget = forms.TextInput())
	email = forms.CharField(label = u'邮箱', max_length = 99, required = True, widget = forms.TextInput())
	mobile = forms.CharField(label = u'联系方式', max_length = 11, required = True, widget = forms.TextInput())
	sex = forms.CharField(label = u'性别', max_length = 10, required = True, widget = forms.TextInput())
	password = forms.CharField(label = u'密码', max_length = 10, required = True, widget = forms.TextInput())
	signature = forms.CharField(label = u'个性签名', max_length = 99, required = False, widget = forms.TextInput())