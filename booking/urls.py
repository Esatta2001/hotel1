from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/' , views.about, name='about'),
    path('roomlist', view.RoomList.as_view(), name='room_list'),
    path('guestlist', views.GuestList.as_view(), name='guest_list'),
    path('guestcreate', views.GuestCreate.as_view(), name='guest_create'),
    path('employee', views.Employee.as_view(), name='employee'),
]
