from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration_success.html')
    else: 
        form  = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    
def login(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # Log the user in
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
                auth_login(request, user)
                return render(request, 'login_success.html')
    else:
        form  = AuthenticationForm()
        return render(request, 'login.html',{'form': form})