from django.shortcuts import render, redirect

# Create your views here.
def index(request):


	return render(request,'surveys/index.html')

def process_form(request):
	try:
		request.session['count'] += 1
	except:
		request.session['count'] = 1
	request.session['info'] =  request.POST
	return redirect('/result')

def result(request):
	context = {
		'count': request.session['count'],
		'info': request.session['info']
	}
	return render(request, 'surveys/result.html', context)
