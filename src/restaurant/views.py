from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function based view

def home(request):
	html_ = """<!DOCTYPE html>
	<html lang=en>
	<head>
	</head>
	<body>
	<h1>Hello World!</h1>
	<p>This is html coming through</p>
	</body>
	</html>

	"""
	return HttpResponse(html_)
	#return render(request,"home.html",{})#response