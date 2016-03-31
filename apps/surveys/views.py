from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request,'surveys/index.html')
def process_form(request):
	return redirect('/result')
def result(request):
	return render(request, 'surveys/result.html')
