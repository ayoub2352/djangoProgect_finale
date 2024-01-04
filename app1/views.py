from django.shortcuts import render , redirect
from .forms import ClientRegistrationForm , AdminstrateurRegistrationForm , ClientSettingsForm , VoyageForm , categorieForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .decorators import user_authenticated , allowed_users
from django.http import HttpResponse
from .models import Voyage , Categorie
# Create your views here.
def home(request) : 
    voyages = Voyage.objects.all()
    context = {'voyages': voyages}
    return render(request,"app1/home.html" , context)


def test2(request) : 

  context = {}
  return render(request,"app1/test2.html" , context)

@user_authenticated  #makatkhlich user li loged in i3aawd irje3 l login page wla ay view kat7t fo9ha had decorator
def loginPage(request): #knt smitha login walakin ghatkhlet m3A login dyal django li kandiro biha login
  if request.method == 'POST':
      username = request.POST.get('username') #input smito usename f login.html
      password = request.POST.get('password') #input smito password f login.html
      user = authenticate(request, username=username, password=password) #kat9lb f database
      if user is not None:
          login(request, user)  #kan3tiwha objet user li rj3ato authenticate
          if user.groups.filter(name='admin').exists():
              return redirect('AdminPage')
          elif user.groups.filter(name='client').exists():
              return redirect('client')
          else:
              return HttpResponse('This user should be associated with a group')
      else:
          messages.info(request, 'Username or password is incorrect')

  context = {}
  return render(request, 'app1/login.html', context)

@user_authenticated 
def register(request): #

    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') #to get user name from the form
            messages.success(request,'Account created for '+user)
            return redirect('login')
    else:
        form = ClientRegistrationForm()

    return render(request, 'app1/register.html', {'form': form})

@login_required(login_url='home') #ila makanch mconecti aymchi l home
@allowed_users(allowed_roles=['client']) #katkhli ghir clients homa li ydkhlo t9dr tbdl roles kima bghiti 3la 7sab groups 
def ClientPage(request): 
        
    context ={}
    return render(request , 'app1/ClientPage.html',context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def AdminPage(request):      
    context ={}
    return render(request , 'app1/AdminPage.html',context)

def logoutUser(request):
  logout(request) #defauLt method dyal django
  return redirect('login')

@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def registerAdmin(request): #
    if request.method == 'POST':
        form = AdminstrateurRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage')
    else:
        form = AdminstrateurRegistrationForm()

    return render(request, 'app1/registerAdmin.html', {'form': form})

@login_required(login_url='home') 
@allowed_users(allowed_roles=['client'])
def ClientSettings(request) :  
  client = request.user.client
  form = ClientSettingsForm(instance=client)

  if request.method == 'POST':
      form = ClientSettingsForm(request.POST, request.FILES,instance=client)
      if form.is_valid():
        form.save()
  context={'form':form}
  return render(request,'app1/ClientSettings.html',context)

@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def voyages(request) : 
    voyages = Voyage.objects.all()
    context = {'voyages':voyages}
    return render(request,"app1/voyages.html" , context)

@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def createvoyage(request):
    if request.method == 'POST':
        form = VoyageForm(request.POST , request.FILES) #🔥🔥🔥🔥🔥request.FILES zdtha bach doz image tahia
        if form.is_valid():
            form.save()
            print("voyage tzad")
            return redirect('voyages')  
        else : 
            print("form addvoyage fiha mochkil ")
            #return redirect('addvoyage')

    else:
        # If the request method is GET, render the form
        form = VoyageForm()

    context = {'form': form}
    return render(request, 'app1/addvoyage.html', context)

@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def updatevoyage(request , pk):
  voyage = Voyage.objects.get(id=pk)
  form = VoyageForm(instance=voyage)
  if request.method == 'POST' : 
      form = VoyageForm(request.POST , request.FILES ,instance=voyage) #🔥🔥🔥🔥🔥request.FILES zdtha bach doz image tahia
      if form.is_valid :
        form.save()
        return redirect('voyages')
  context={'form' : form}
  return render(request, "app1/addvoyage.html",context)

@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def deletevoyage(request , pk) : 
  item = Voyage.objects.get(id=pk)
  if request.method == "POST" :
    item.delete()
    return redirect('voyages')

  context={'item':item }
  return render(request , 'app1/deletevoyage.html' , context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def categories(request) : 
    categories = Categorie.objects.all()
    context = {'categories':categories}
    return render(request,"app1/categories.html" , context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def addcategorie(request):
    if request.method == 'POST':
        form = categorieForm(request.POST) 
        if form.is_valid():
            form.save()
            print("categorie tzadt")
            return redirect('categories')  
        else : 
            print("form addcategorie fiha mochkil ")
            #return redirect('addvoyage')

    else:
        # If the request method is GET, render the form
        form = categorieForm()

    context = {'form': form}
    return render(request, 'app1/addcategorie.html', context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def updatecategorie(request , pk):
  categorie = Categorie.objects.get(id=pk)
  form = categorieForm(instance=categorie)
  if request.method == 'POST' : 
      form = categorieForm(request.POST ,instance=categorie)
      if form.is_valid :
        form.save()
        return redirect('categories')
  context={'form' : form}
  return render(request, "app1/addcategorie.html",context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def deletecategorie(request , pk) : 
  item = Categorie.objects.get(id=pk)
  if request.method == "POST" :
    item.delete()
    return redirect('categories')

  context={'item':item }
  return render(request , 'app1/deletecategorie.html' , context)


