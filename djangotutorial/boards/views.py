from django.http import HttpResponse  # added by me
from django.shortcuts import render

from .models import Board  # added by me

# Create your views here.


def home(request):  # added by me
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})
