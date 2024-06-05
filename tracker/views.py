from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .filters import TransactionFilter


# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transactions_list(request):
    transactions_filter = TransactionFilter(request.GET,queryset=Transaction.objects.filter(user=request.user).select_related('category'))
    total_expenses = transactions_filter.qs.get_total_expanses()
    total_incomes = transactions_filter.qs.get_total_incomes()
    
    net_income = total_incomes - total_expenses
    
   
    context = {'filter': transactions_filter,
               'total_expenses': total_expenses,
               'total_incomes': total_incomes,
               'net_income': net_income,
               }
    if request.htmx:
        return render(request, 'tracker/partials/transactions-container.html', context)
    return render(request, 'tracker/transactions_list.html', context)
    