import datetime
from Blog.models import *
from Blog.forms import *
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required




def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username,password=password)
    if user is not None:
        auth_login(request,user)
        return True
    return rtvalue

def login(request):
	error = []
	form = LoginForm()
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			password = data['password']
			if login_validate(request,username,password):
			    return render(request,'welcome.html',{'user':username})
			else:
				error.append('Please input the correct password')
		else:
			error.append('Please input both username and password')
	else:
		form = LoginForm()
	return render(request,'login.html',{'error':error,'form':form})		

def register(request):
	error=[]
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			email = data['email']
			password = data['password']
			password2 = data['password2']
			if not User.objects.all().filter(username=username):
				if not  User.objects.all().filter(email=email):
					if form.pwd_validate(password, password2):
						user = User.objects.create_user(username, email, password)
						user.save()
						login_validate(request,username,password)
						return render(request,'welcome.html',{'user':username})
					else:
						error.append('Please input the same password')
				else:
					error.append('The email has existed,please change your email.')
			else:
				error.append('The username has existed,please change your username.')
		else:
			form = RegisterForm()	
	return render(request,'register.html',{'form':form,'error':error})

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/blog/login/')

def changepassword(request,username):
	error = []
	form = ChangepwdForm()
	if request.method == 'POST':
		form = ChangepwdForm(request.POST.copy())
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username=username,password=data['old_pwd'])
			if user is not None:
				if data['new_pwd'] == data['new_pwd2']:
					newuser = User.objects.get(username__exact=username)
					newuser.set_password(data['new_pwd'])
					newuser.save()
					return HttpResponseRedirect('/blog/login/')
				else:
					error.append('Please input the same password.')
			else:
				error.append('Please correct the old password.')
		else:
			error.append('Please input the required domain.')
	else:
		form = ChangepwdForm()
	return render(request,'changepassword.html',{'form':form,"error":error})

def post(request,uname):
	error=[]
	form = BlogText()
	if request.method == 'POST':
		form = BlogText(request.POST.copy())
		if form.is_valid():
			data = form.cleaned_data
			title = data['title']
			content = data['content']
			StartTime = data['StartTime']
			EndTime = data['EndTime']
			if not Msg.objects.all().filter(title=title):
				msg = Msg.objects.create(title=title,content=content,author=uname,ip=request.META['REMOTE_ADDR'],StartTime=StartTime,EndTime=EndTime)
				return render(request,'af_post.html')
			else:
				error.append('This title has been used.')
	else:
		form = BlogText()
	return render(request,'post.html',{'error':error,'form':form})

def index(request):
	bloglist = Msg.objects.all()
	return render(request,'index.html',locals())

def detail(request,post_id):
	msg = get_object_or_404(Msg,id = post_id)
	return render(request,'detail.html',{'msg':msg})

def delete(request,post_id,uname):
	b = Msg.objects.get(id=post_id)
	if uname == b.author:
		Msg.objects.get(id=post_id).delete()
		return HttpResponseRedirect('/blog/')
	else:
		return render(request,'fail_del.html')

def edit(request,post_id,uname):
	error = []
	b = Msg.objects.get(id = post_id)
	form = Edit()
	if uname == b.author:
		if request.method=='POST':
			form = Edit(request.POST.copy())
			if form.is_valid():
				data = form.cleaned_data
				a = Msg.objects.get(id = post_id)
				a.title = data['title']
				a.content = data['content']
				a.save()
				return render(request,'af_edit.html')
			else:
				error.append('Pls input valid edit!!!')
		else:
			form = Edit(initial={'title':b.title,'content':b.content})
	else:
		return render(request,"fail_edit.html")
	return render(request,'edit.html',{'form':form})

def join(request,post_id,uname):
	b = Msg.objects.get(id=post_id)
	if uname != b.author:
		b.people += 1
		b.peoplelist += uname
		b.peoplelist += ','
		b.save()
		return HttpResponseRedirect('/blog/')
	else:
		return render(request,'fail_del.html')


