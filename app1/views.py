from django.shortcuts import render , redirect
from .forms import ClientRegistrationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request) : 

  context = {}
  return render(request,"app1/home.html" , context)

def test2(request) : 

  context = {}
  return render(request,"app1/test2.html" , context)


def loginPage(request): #knt smitha login walakin ghatkhlet m3A login dyal django li kandiro biha login

    if request.method == 'POST' :
      username = request.POST.get('username') #input smito usename f login.html
      password = request.POST.get('password') #input smito password f login.html
      user = authenticate(request , username=username , password = password) #kat9lb f database
      if user is not None : 
        login(request,user)  #kan3tiwha objet user li rj3ato authenticate
        print("login suceded")
        return redirect('client')
      else:
        messages.info(request,'username or passwrod is incorect')
        
    context ={}
    return render(request , 'app1/login.html',context)

def register(request): #knt smitha login walakin ghatkhlet m3A login dyal django li kandiro biha login

    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to another page
            messages.success(request,'Account created for '+user)
            return redirect('login')
    else:
        form = ClientRegistrationForm()

    return render(request, 'app1/register.html', {'form': form})

@login_required(login_url='home') #ila makanch mconecti aymchi l home
def ClientPage(request): 
        
    context ={}
    return render(request , 'app1/ClientPage.html',context)

def logoutUser(request):
  logout(request) #defauLt method dyal django
  return redirect('login')