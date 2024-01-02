from django.shortcuts import render

# Create your views here.
def home(request) : 

  context = {}
  return render(request,"app1/home.html" , context)

def test2(request) : 

  context = {}
  return render(request,"app1/test2.html" , context)