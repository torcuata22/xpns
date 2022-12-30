from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid:
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount')) #remember: amount is the name of the field in the model
    print(total_expenses)

    expense_form = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form':expense_form, 'expenses': expenses, 'total_expenses': total_expenses})

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


def delete(request,id):
    if request.method == "POST" and 'delete' in request.POST: #only executes if the word "delete" is on the request
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect ('index')
