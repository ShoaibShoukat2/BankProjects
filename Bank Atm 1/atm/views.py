from django.shortcuts import render, get_object_or_404, redirect
from .models import ATM
from .forms import ATMForm


def atm_list(request):
    atms = ATM.objects.all()
    return render(request, 'atm/atm_list.html', {'object_list': atms})


def atm_detail(request, pk):
    atm = get_object_or_404(ATM, pk=pk)
    return render(request, 'atm/atm_detail.html', {'object': atm})


def atm_create(request):
    if request.method == 'POST':
        form = ATMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atm:atm_list')
    else:
        form = ATMForm()
    return render(request, 'atm/atm_create.html', {'form': form})


def atm_update(request, pk):
    atm = get_object_or_404(ATM, pk=pk)
    if request.method == 'POST':
        form = ATMForm(request.POST, instance=atm)
        if form.is_valid():
            form.save()
            return redirect('atm:atm_detail', pk=pk)
    else:
        form = ATMForm(instance=atm)
    return render(request, 'atm/atm_update.html', {'form': form, 'object': atm})


def atm_delete(request, pk):
    atm = get_object_or_404(ATM, pk=pk)
    if request.method == 'POST':
        atm.delete()
        return redirect('atm:atm_list')
    return render(request, 'atm/atm_confirm_delete.html', {'object': atm})
