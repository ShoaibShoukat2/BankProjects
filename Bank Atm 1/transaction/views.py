from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.all()
    print(transactions)
    return render(request, 'transaction/transaction_list.html', {'object_list': transactions})

def transaction_create(request):
    print(request.method)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction:transaction_list')
        else:
            print(form.errors)
    else:
        form = TransactionForm()
    return render(request, 'transaction/transaction_create.html', {'form': form})

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction/transaction_detail.html', {'object': transaction})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction:transaction_detail', pk=pk)
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction/transaction_update.html', {'form': form, 'object': transaction})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction:transaction_list')
    return render(request, 'transaction/transaction_confirm_delete.html', {'object': transaction})
