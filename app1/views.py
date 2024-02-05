from django.shortcuts import render , redirect
from .forms import ClientRegistrationForm , AdminstrateurRegistrationForm , ClientSettingsForm , VoyageForm , categorieForm , hotelForm , volForm , notificationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .decorators import user_authenticated , allowed_users
from django.http import HttpResponse
from .models import Voyage , Categorie , Client_voyage ,Hotel , Vol , Client , Adminstrateur , Client
import stripe
from datetime import date
from .filters import VoyageFilter


stripe.api_key = "sk_test_51MxJ30AhdCO5CiRyKgfCeJhC1y2i1iXTiUBS9YpKaQYtSp5ZmMpJ2Y8yIRtQUMzmvJHZtCIt0xkYmBO7NslpAqkx00PZKLjYrT"

# Create your views here.
def home(request) : 
    categories = Categorie.objects.all()
    print(categories)
    voyages = Voyage.objects.all()
    myfilter = VoyageFilter(request.GET,queryset=voyages)
    voyages=myfilter.qs
    context = {'voyages': voyages,'myfilter':myfilter,'categories':categories}
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
    voyages = Voyage.objects.all()
    print(voyages)    
    context ={'voyages':voyages}
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
        form = categorieForm(request.POST, request.FILES) 
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
      form = categorieForm(request.POST ,request.FILES,instance=categorie)
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


@login_required(login_url='home') 
@allowed_users(allowed_roles=['client'])
def reservationclient(request,pk) : 
    reservations =Client_voyage.objects.filter(fk_client=pk)
    context = {'reservations':reservations}
    return render(request,"app1/reservationclient.html" , context)

@login_required(login_url='home') 
@allowed_users(allowed_roles=['client'])
def reserve(request,pk) : 
    voyageid = pk
    voyage = Voyage.objects.get(id=pk)
    userid = request.user.id 
    client = Client.objects.get(fk_user=userid)
    client_id = client.id
    if request.method == 'POST' : 
        # print('data : ',request.POST)
        customer = stripe.Customer.create(
            email = client.fk_user.email,
            name = client.fk_user.username,
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = voyage.prix*100, #stripe kayst3ml cent so khask dreb f 100
            currency = 'mad',
            description = voyage.description
        )

        reservation = Client_voyage.objects.create(
                fk_client_id=client_id,
                fk_voyage=voyage,
                date_reservation=date.today(),
                amountPaid=voyage.prix,
                paymentStatus=True  # Set to True since the payment was successful
            )

        voyage.nbr_places -= 1
        voyage.save()

        
        context = {'prix' : voyage.prix}
        return render(request,"app1/succes.html",context)


    context = {'voyageid' : voyageid}
    return render(request,"app1/reserve.html" , context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def hotels(request) : 
    hotels = Hotel.objects.all()
    context = {'hotels':hotels}
    return render(request,"app1/hotels.html" , context)



@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def addhotel(request):
    if request.method == 'POST':
        form = hotelForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            print("hotel tzad")
            return redirect('hotels')  
        else : 
            print("form addhotel fiha mochkil ")
            #return redirect('addvoyage')

    else:
        # If the request method is GET, render the form
        form = hotelForm()

    context = {'form': form}
    return render(request, 'app1/addhotel.html', context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def updatehotel(request , pk):
  hotel = Hotel.objects.get(id=pk)
  form = hotelForm(instance=hotel)
  if request.method == 'POST' : 
      form = hotelForm(request.POST ,request.FILES,instance=hotel)
      if form.is_valid :
        form.save()
        return redirect('hotels')
  context={'form' : form}
  return render(request, "app1/addhotel.html",context)



@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def deletehotel(request , pk) : 
  item = Hotel.objects.get(id=pk)
  if request.method == "POST" :
    item.delete()
    return redirect('hotels')

  context={'item':item }
  return render(request , 'app1/deletehotel.html' , context)



@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def vols(request) : 
    vols = Vol.objects.all()
    context = {'vols':vols}
    return render(request,"app1/vols.html" , context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def addvol(request):
    if request.method == 'POST':
        form = volForm(request.POST) 
        if form.is_valid():
            form.save()
            print("vol tzad")
            return redirect('vols')  
        else : 
            print("form addvol fiha mochkil ")
            #return redirect('addvoyage')

    else:
        # If the request method is GET, render the form
        form = volForm()

    context = {'form': form}
    return render(request, 'app1/addvol.html', context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def updatevol(request , pk):
  vol = Vol.objects.get(id=pk)
  form = volForm(instance=vol)
  if request.method == 'POST' : 
      form = volForm(request.POST ,instance=vol)
      if form.is_valid :
        form.save()
        return redirect('vols')
  context={'form' : form}
  return render(request, "app1/addvol.html",context)


@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def deletevol(request , pk) : 
  item = Vol.objects.get(id=pk)
  if request.method == "POST" :
    item.delete()
    return redirect('vols')

  context={'item':item }
  return render(request , 'app1/deletevol.html' , context)



@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def admins(request) : 
    admins = Adminstrateur.objects.all()
    context = {'admins':admins}
    return render(request,"app1/admins.html" , context)



def detailsvoyage(request,pk) : 

    voyage = Voyage.objects.get(id=pk)
    context = {'voyage':voyage}

    return render(request,"app1/detailsvoyage.html",context)


def categorievoyage(request,pk) : 

    voyages = Voyage.objects.filter(categorie__nom=pk)
    context = {'voyages':voyages}
    return render(request,"app1/categorievoyage.html",context)



@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def clients(request) : 
    clients = Client.objects.all()
    print(clients)
    context = {'clients':clients}
    return render(request,"app1/clients.html" , context)





@login_required(login_url='home') 
@allowed_users(allowed_roles=['admin'])
def sendnotification(request, pk):

    if request.method == 'POST':
        form = notificationForm(request.POST) 
        if form.is_valid():
            form.save()
            print("message tseft tzad")
            return redirect('clients')  
        else : 
            print("form addhotel fiha mochkil ")
            #return redirect('addvoyage')

    else:
        # If the request method is GET, render the form
        form = notificationForm()

    context = {'form': form}
    return render(request, 'app1/sendnotification.html', context)