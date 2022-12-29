from django.shortcuts import render
from .models import Expense

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')