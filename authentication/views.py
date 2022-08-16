from django.shortcuts import render


# Create your views here.
def login(request):
    name = request.POST['name']
    passw = request.POST['pass']
    if name == 'rakeeb' and passw == 'dana123':
        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'index.html', {'err': "password and user name doesn't match"})
