#coding: utf-8
from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def index(request):
	# return render_to_response('main/index.html', {}, context_instance = RequestContext(request))
	return render(request, 'main/index.html')