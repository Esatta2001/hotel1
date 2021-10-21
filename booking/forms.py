from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Room, Guest, Employee
from .form import GuestCreateForm

ROOMS = [101,102,103,104]

class GuestCreate(CreateView):
    model = Guest
    template_name = 'booking/guest_create_form.html'
    form_class = GuestCreateForm

class RoomList(ListView):
    model = Room

class EmployeeList(ListView)
    model = Employee

class Guestlist(ListView):
    model = Guest

def home(request):