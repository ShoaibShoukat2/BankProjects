from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ATM
from .forms import ATMForm


class AtmListView(View):
    template_name = 'atm/atm_list.html'

    def get(self, request):
        atms = ATM.objects.all()
        return render(request, self.template_name, {'object_list': atms})


class AtmDetailView(DetailView):
    model = ATM
    template_name = 'atm/atm_detail.html'
    context_object_name = 'object'


class AtmCreateView(CreateView):
    model = ATM
    form_class = ATMForm
    template_name = 'atm/atm_create.html'
    success_url = reverse_lazy('atm:atm_list')


class AtmUpdateView(UpdateView):
    model = ATM
    form_class = ATMForm
    template_name = 'atm/atm_update.html'
    context_object_name = 'object'

    def get_success_url(self):
        return reverse_lazy('atm:atm_detail', kwargs={'pk': self.object.pk})


class AtmDeleteView(DeleteView):
    model = ATM
    template_name = 'atm/atm_confirm_delete.html'
    success_url = reverse_lazy('atm:atm_list')
