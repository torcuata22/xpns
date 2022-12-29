from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid:
            expense.save()

    expenses = Expense.objects.all()

    expense_form = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form':expense_form, 'expenses': expenses})

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense) #instance is an attribute of the model form

    if request.method == "POST":
        expense = Expense.objects.get(id=id) #yes, this is the same expense variable as above, it could be refactored
        form = ExpenseForm(request.POST, instance=expense) #because we want the new data that got passed to the form
        
        if form.is_valid:
            form.save()
            return redirect('index')
    
    return render(request, 'myapp/edit.html', {'expense_form': expense_form})