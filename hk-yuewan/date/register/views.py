from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
# from date.models import Account
from .forms import userForm
from account.models import ProFile
# from django.contrib.auth.models import AbstractUser, User

# Create your views here.
def index(request):
	if (request.method == 'POST'):
		form = userForm(request.POST)
		if (form.is_valid()):
			user = User()
			user.username = form.cleaned_data['username']
			user.email = form.cleaned_data['email']
			user.set_password(form.cleaned_data['password'])

			profile = ProFile()
			profile.realname = form.cleaned_data['realname']
			profile.mobile = form.cleaned_data['mobile']
			profile.sex = form.cleaned_data['sex']
			profile.signature = form.cleaned_data['signature']

			user.set_profile(profile)
			user.save()

			newUser = authenticate(user.username, user.password)
			if (newUser is not None):
				login(request, newUser)
				return HttpResponseRedirect('main/index.html')
	else:
		form = userForm()
		return render(request, 'register/index.html', {'form': form})

def submit(request):
	user = Account()
	user.username = request.POST['username']
	user.realname = request.POST['realname']
	user.email = request.POST['email']
	user.mobile = request.POST['mobile']
	user.sex = request.POST['sex']
	user.set_password(request.POST['password'])
	if (request.POST['signature']):
		user.signature = request.POST['signature']
	else:
		user.signature = ''
	user.save()

	newUser = authenticate(user.username, user.password)
	if (newUser is not None):
		login(request, newUser)
		return HttpResponseRedirect('main/index.html')