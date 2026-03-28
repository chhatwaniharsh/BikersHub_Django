from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created. You are now able to log in.')
            return redirect('login')
    template_name = 'AuthAPP/register.html'
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_index')
            else:
                return redirect('customer_index')
        else:
            messages.error(request, 'Username OR Password is incorrect')
            return redirect('login')
    template_name = 'AuthAPP/login.html'
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('login')