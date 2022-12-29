from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid:
            expense.save()
            
    expense_form = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form':expense_form})