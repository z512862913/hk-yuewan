from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def submit(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if (user is not None):
		login(request, user)
	else:
		HttpResponseRedirect('login/index.html')