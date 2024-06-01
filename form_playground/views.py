from django.shortcuts import render
from .forms import PlayFrom

# Create your views here.
def home(request):
    form = PlayFrom()
    return render(request, 'home.html', {'form': form})