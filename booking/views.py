from django.shortcuts import render


ROOMS = [101,102,103,104]

# Create your views here.
def home(request):
    # templates folder is already assumed since this app is registered in templates.py
    return render(request, 'booking/home.html')
name = "Homer"
loggedin=False
context = {"user_first_name": name, "room": ROOMS, "loggedin":loggedin}

def about(request):
    return render(request, 'booking/about.html')
