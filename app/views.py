from django.shortcuts import render
def forloop(request):
    d={'Name':'Govardhan'}
    return render(request,'forloop.html',d)
# Create your views here.
