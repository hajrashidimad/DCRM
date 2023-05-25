from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# import local module:
from .forms import *
from .models import *

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          messages.success(request ,'You are logged in!')
          return redirect(home)
        
        else :
          messages.success(request ,'You are Not logged in!, try again')
          return redirect(home)
            
    else:
        return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged Out !')
    return redirect(home)



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Successfully Registred! Welcome!')
            return redirect('home')
    else :
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})


    return render(request, 'register.html', {'form':form})



def customer_records(request, pk):
    if request.user.is_authenticated:
        customer_records = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_records':customer_records})
    
    else:
        messages.success(request, 'Please Login to view this page!!')
        return redirect('home')
    


def delete_record(request, pk):
    if request.user.is_authenticated:
      delete = Record.objects.get(id=pk)
      delete.delete()
      messages.success(request, 'Record is deleted!!')
      return redirect('home')
    else:
        messages.success(request, 'Please Login to view this page!!')
        return redirect('home')
  

def add_record(request):
	form = AddRecord(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
        

def update_record(request, pk):
    if request.user.is_authenticated:
        update = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=update)
        if form.is_valid():
            # form = update
            form.save()
            messages.success(request, "Record Updated...")
            # delete_record(request, pk)
            return redirect('home')
      
        return render(request, 'update_record.html', {'form':form})


    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')