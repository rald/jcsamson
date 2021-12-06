from django.urls import path

from . import views

from contactus.views import classv

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('functionv&id=<int:id>', views.functionv, name='functionv'),
    path('classv&id=<int:id>', classv.as_view(), name='classv'),
]
