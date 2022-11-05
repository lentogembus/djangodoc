from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, we're at the polls index.")

