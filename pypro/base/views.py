from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    raise ValueError()
    return HttpResponse('<html><body>Hello Django</body></html>', content_type='text/html')
