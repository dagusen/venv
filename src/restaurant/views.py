import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function based view

# def home_old(request):
#  	#f strings
#  	html_var = 'Louis gwapo'
#  	html_ = f"""<!DOCTYPE html>
#  	<html lang=en>
#  	<head>
#  	</head>
#  	<body>
#  	<h1>Hello World!</h1>
#  	<p>This is {html_var} coming through</p>
#  	</body>
#  	</html>
#  	"""
#  	return HttpResponse(html_)

def home(request):
	num = random.randint(0, 1000000)
	return render(request,"base.html",{"html_var": True, "num" : num})#response