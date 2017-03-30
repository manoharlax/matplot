from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
	return render(request, 'myapp/index.html')



'''
def index(request):

	template = loader.get_template('myapp/index.html')
	context = None
	return render(request,'index.html',context=None)
	return HttpResponse(template.render(context, request))

def index(request):
    return HttpResponse("Bar Chart !!!!")
'''