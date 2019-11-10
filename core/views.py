from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from core.models import Inventory, Waybill, Stock

'''- Добавление/редактирование/удаление информации о рабочем инвентаре.
- Добавление/редактирование/удаление информации о складах.
- Добавление/редактирование/удаление информации о приходе и расходе рабочего инвентаря.
- Просмотр списка инвентаря заданного типа на заданном складе и его количество на текущую дату.
- Просмотр списка всех приходов и расходов инвентаря заданного наименования на всех складах 
    – дата, название инвентаря, список - дата прихода, количество, дата расхода, количество.
- Просмотр списка всех складов, отсортированных по названию на текущую дату.'''


class StockFormView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('stock_form')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'stock form'
        context['header'] = "Let's work with stock form"
        context['submit'] = "stock"
        return context


class InventoryFormView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_fo0rm')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'inventory form'
        context['header'] = "Let's work with inventory form"
        context['submit'] = "inventory"
        return context


class WaybillFormView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_form')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'waybill form'
        context['header'] = "Let's work with waybill form"
        context['submit'] = "waybill"
        return context


class InventoryListView(ListView):
    template_name = 'core/listview.html'
    model = Inventory
    success_url = reverse_lazy('inventory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Let's see list of inventories"
        return context


class WaybillListView(ListView):
    template_name = 'core/listview.html'
    model = Waybill
    success_url = reverse_lazy('waybill_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'waybill list'
        context['header'] = "Let's see list of waybills"
        return context


class StockListView(ListView):
    template_name = 'core/listview.html'
    model = Stock
    success_url = reverse_lazy('stock_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Let's see list of stocks"
        return context
