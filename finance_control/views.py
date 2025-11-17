from django.shortcuts import render, redirect
from finance_control.models import Transaction

def index(request):
    transaction = Transaction.objects.all()
    return render(request, 'index.html', {'transaction': transaction} )

def view_all(request):
    transaction = Transaction.objects.filter(user=request.user)
    return render(request, 'view_all.html', {'transaction': transaction})

def transaction_create_view(request):
    if request.method == 'POST':
        amount = request.POST.get("amount")
        type_value = request.POST.get("type")
        category_value = request.POST.get("category")
        description = request.POST.get("description")

        Transaction.objects.create(
            user=request.user,       
            amount=amount,
            type=type_value,
            category=category_value,
            description=description
        )

        return redirect("index")    

    return render(request, "transaction_create.html")

def transaction_update_view(request, pk):
    transactions = Transaction.objects.get(id = pk)
    if request.method == 'POST':
        transactions.amount = request.POST.get("amount")
        transactions.type = request.POST.get("type")
        transactions.category = request.POST.get("category")
        transactions.description = request.POST.get("description")
        transactions.save()
        return redirect("index")    

    return render(request, "transaction_update.html", {'transactions': transactions})
        

def transaction_delete_view(request, pk):
    transactions = Transaction.objects.get(id = pk)
    if request.method == "POST":
        transactions.delete()
        return redirect('view_all') 
    return render(request, 'transaction_delete.html', {'transactions': transactions}) 

def analytics_view(request):
    transactions = Transaction.objects.filter(user=request.user)

    incomes = transactions.filter(type='income')
    expenses = transactions.filter(type='expense')

    total_income = 0
    for total in incomes:
        total_income += total.amount

    total_expense = 0
    for total in expenses:
        total_expense += total.amount

    balance = total_income - total_expense

    return render(request, 'analytics.html', {'total_income': total_income, 'total_expense': total_expense, 'balance': balance })     
