from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
import datetime
from django.db.models import Sum
# Create your views here.
def index(request):
    if request.method =="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
            
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
    
    #Logic to calculate 365 days expenses (1 year)
    last_year = datetime.date.today() - datetime.timedelta(days=365) #calculates when last year ends
    data = Expense.objects.filter(date__gt=last_year) #filters info so only this year is added
    yearly_sum = data.aggregate(Sum('amount')) #adds data
    
    #Logic to calculate expenses in last 30 days 
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
     #Logic to calculate expenses in last 7 days
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))
    
    #logic to calculate expenses per day
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    
    #logic to calculate expenses by category
    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    print(categorical_sums)
    
    expense_form = ExpenseForm()
    return render(request,'myapp/index.html',{
        'expense_form':expense_form,
        'expenses':expenses,
        'total_expenses':total_expenses,
        'yearly_sum':yearly_sum,
        'weekly_sum':weekly_sum,
        'monthly_sum':monthly_sum,
        'daily_sums':daily_sums,
        'categorical_sums':categorical_sums,
        })

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
