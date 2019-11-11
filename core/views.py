from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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
    success_url = reverse_lazy('stock_list')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'create stock'
        context['header'] = "Create Stock"
        context['submit'] = "stock"
        return context


class CreateInventoryView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_list')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'create inventory'
        context['header'] = "Create Inventory"
        context['submit'] = "inventory"
        return context


class CreateWaybillView(CreateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_list')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'create waybill'
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
        context['delete_url'] = reverse_lazy('delete_inventory')
        context['update_url'] = reverse_lazy('update_inventory')
        print(context['delete_url'], context['update_url'])
        return context


class WaybillListView(ListView):
    template_name = 'core/listview.html'
    model = Waybill

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Waybill List'
        context['header'] = "Waybill List"
        context['delete_url'] = reverse_lazy('delete_waybill')
        context['update_url'] = reverse_lazy('update_waybill')
        return context


class StockListView(ListView):
    template_name = 'core/listview.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Stock List"
        context['delete_url'] = reverse_lazy('delete_stock')
        context['update_url'] = reverse_lazy('update_stock')
        return context


class UpdateStockView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('stock_list')
    model = Stock
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'update stock'
        context['header'] = "Update Stock"
        context['submit'] = "stock"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


class UpdateInventoryView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('inventory_list')
    model = Inventory
    fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'updateinventory'
        context['header'] = "Update Inventory"
        context['submit'] = "inventory"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


class UpdateWaybillView(UpdateView):
    template_name = 'core/formview.html'
    success_url = reverse_lazy('waybill_list')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'update waybill'
        context['header'] = "Update Waybill"
        context['submit'] = "waybill"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


def delete_inventory(request, pk):
    obj = get_object_or_404(Inventory, id=pk)
    obj.delete()
    return reverse_lazy('inventory_list')


def delete_stock(request, pk):
    obj = get_object_or_404(Stock, id=pk)
    obj.delete()
    return reverse_lazy('stock_list')


def delete_waybill(request, pk):
    obj = get_object_or_404(Waybill, id=pk)
    obj.delete()
    return reverse_lazy('waybill_list')
