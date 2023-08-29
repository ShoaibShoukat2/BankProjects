from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer
from .forms import CustomerForm


class CustomerListView(View):
    template_name = 'customer/customer_list.html'

    def get(self, request):
        customers = Customer.objects.all()
        return render(request, self.template_name, {'object_list': customers})


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'object'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_create.html'
    success_url = reverse_lazy('customer:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_update.html'
    context_object_name = 'object'

    def get_success_url(self):
        return self.object.get_absolute_url()


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_confirm_delete.html'
    success_url = reverse_lazy('customer:customer_list')
