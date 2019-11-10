from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class CreateStockView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('stock_form')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'stock form'
        context['header'] = "Create Stock"
        context['submit'] = "stock"
        return context


class CreateInventoryView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_form')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'inventory form'
        context['header'] = "Create Inventory"
        context['submit'] = "inventory"
        return context


class CreateWaybillView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_form')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'waybill form'
        context['header'] = "Create Waybill"
        context['submit'] = "waybill"
        return context


class InventoryListView(ListView):
    template_name = 'core/listview.html'
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Inventory List"
        return context


class WaybillListView(ListView):
    template_name = 'core/listview.html'
    model = Waybill

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Waybill List'
        context['header'] = "Waybill List"
        return context


class StockListView(ListView):
    template_name = 'core/listview.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Stock List"
        return context


class UpdateStockView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('stock_form')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'stock form'
        context['header'] = "Update Stock"
        context['submit'] = "stock"
        return context


class UpdateInventoryView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_form')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'inventory form'
        context['header'] = "Update Inventory"
        context['submit'] = "inventory"
        return context


class UpdateWaybillView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_form')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'waybill form'
        context['header'] = "Update Waybill"
        context['submit'] = "waybill"
        return context


class DeleteStockView(DeleteView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('stock_form')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'stock form'
        context['header'] = "Delete Stock"
        context['submit'] = "stock"
        return context


class DeleteInventoryView(DeleteView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_form')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'inventory form'
        context['header'] = "Delete Inventory"
        context['submit'] = "inventory"
        return context


class DeleteWaybillView(DeleteView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_form')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'waybill form'
        context['header'] = "Delete Waybill"
        context['submit'] = "waybill"
        return context
