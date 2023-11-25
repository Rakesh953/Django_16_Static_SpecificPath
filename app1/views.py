from django.shortcuts import render

# Create your views here.
def Static_File(request):
    return render(request,'Static_File.html')   