from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from core.forms import StockForm, InventoryForm, WaybillForm
from core.models import Inventory, Waybill, Stock


class StockFormView(FormView):
    template_name = 'core/formview.html'
    form_class = StockForm

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'stock form'
        context['header'] = "Let's work with stock form"
        return context


class InventoryFormView(FormView):
    template_name = 'core/formview.html'
    form_class = InventoryForm

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'inventory form'
        context['header'] = "Let's work with inventory form"
        return context


class WaybillFormView(FormView):
    template_name = 'core/formview.html'
    form_class = WaybillForm

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'waybill form'
        context['header'] = "Let's work with waybill form"
        return context


class InventoryListView(ListView):
    template_name = 'core/listview.html'
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Let's see list of inventories"
        return context


class WaybillListView(ListView):
    template_name = 'core/listview.html'
    model = Waybill

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'waybill list'
        context['header'] = "Let's see list of waybills"
        return context


class StockListView(ListView):
    template_name = 'core/listview.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Let's see list of stocks"
        return context
