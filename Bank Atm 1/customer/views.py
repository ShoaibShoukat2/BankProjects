from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'object_list': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_create.html', {'form': form})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    print(customer)
    return render(request, 'customer/customer_detail.html', {'object': customer})

def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(customer.get_absolute_url())
    else:
        form = CustomerForm(instance=customer)
    print(customer)
    return render(request, 'customer/customer_update.html', {'form': form, 'object': customer})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:customer_list')
    return render(request, 'customer/customer_confirm_delete.html', {'object': customer})
