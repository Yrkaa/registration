from django.shortcuts import render

from ipware import get_client_ip

from app0.models import User

# Create your views here.
def index(request): 
    have_ip = User.objects.filter(ip=get_client_ip(request)[0])
    if not have_ip:
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            ip = get_client_ip(request)[0]
            new_user = User(name=name, password=password, ip=ip)
            new_user.save()
            
        return render(request, "reg.html")
    else:
        data = {"name": User.objects.get(ip=get_client_ip(request)[0]).name}
        return render(request, "main.html", context=data)