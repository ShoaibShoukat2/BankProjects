from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Transaction
from .forms import TransactionForm


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'object_list'


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction_create.html'
    success_url = reverse_lazy('transaction:transaction_list')


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/transaction_detail.html'
    context_object_name = 'object'


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction_update.html'
    context_object_name = 'object'

    def get_success_url(self):
        return reverse_lazy('transaction:transaction_detail', args=[self.object.pk])


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction/transaction_confirm_delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('transaction:transaction_list')
