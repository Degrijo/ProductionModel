from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum, Value, Case, IntegerField, F

import re

from core.models import Inventory, Waybill, Stock, InventoryWaybillStock


class CreateStockView(CreateView):
    template_name = 'core/stock_form.html'
    success_url = reverse_lazy('stock_list')
    model = Stock
    fields = ('name', 'phone_number')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'create stock'
        context['header'] = "Create Stock"
        return context


class CreateInventoryView(CreateView):
    template_name = 'core/inventory_form.html'
    success_url = reverse_lazy('inventory_list')
    model = Inventory
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'create inventory'
        context['header'] = "Create Inventory"
        return context


class CreateWaybillView(CreateView):
    template_name = 'core/waybill_form.html'
    success_url = reverse_lazy('waybill_list')
    model = Waybill
    fields = ('employee_name', 'employee_position', 'incoming')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'create waybill'
        context['header'] = "Create Waybill"
        context['inventories'] = Inventory.objects.all().annotate(
            number=Sum('inventory_waybill_stock__inventory_number'))
        return context

    def post(self, request, *args, **kwargs):
        waybill_data = {}
        inventories = {}
        incoming = request.POST['incoming']
        check = False
        stock_id = self.kwargs['pk']
        for key, value in request.POST.items():
            if key in ['employee_name', 'employee_position']:
                waybill_data[key] = value
            elif key == 'incoming':
                waybill_data[key] = True if value == 'True' else False
            elif re.match(r'inventory_\d+$', key) and int(value) != 0:
                inv_id = int(re.compile(r'\d+$').search(key).group(0))
                if incoming == 'False' and \
                        int(value) > InventoryWaybillStock.objects.filter(inventory_id=inv_id,
                                                                          stock_id=stock_id). \
                        aggregate(number=Sum('inventory_number'))['number']:
                    return self.form_invalid(self.get_form_class()())
                inventories[inv_id] = int(value)
                check = True
        waybill_form = self.get_form_class()(waybill_data)
        if not waybill_form.is_valid() or not check:
            return self.form_invalid(waybill_form)
        waybill = waybill_form.save()
        for key, value in inventories.items():
            InventoryWaybillStock.objects.create(inventory_id=key, waybill=waybill, stock_id=stock_id,
                                                 inventory_number=value if incoming == 'True' else -value)
        return self.form_valid(waybill_form)

    def form_invalid(self, form):
        super().form_invalid()


class InventoryListView(ListView):
    template_name = 'core/inventory_list.html'
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Inventory List"
        context['delete_url'] = reverse_lazy('delete_inventory')
        context['update_url'] = reverse_lazy('update_inventory')
        return context


class WaybillListView(ListView):
    template_name = 'core/waybill_list.html'
    queryset = Waybill.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Waybill List'
        context['header'] = "Waybill List"
        context['delete_url'] = reverse_lazy('delete_waybill')
        context['update_url'] = reverse_lazy('update_waybill')
        return context


class StockListView(ListView):
    template_name = 'core/stock_list.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Stock List"
        context['delete_url'] = reverse_lazy('delete_stock')
        context['update_url'] = reverse_lazy('update_stock')
        return context

    class Meta:
        ordering = ['-name']


class UpdateStockView(UpdateView):
    template_name = 'core/stock_form.html'
    success_url = reverse_lazy('stock_list')
    model = Stock
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'update stock'
        context['header'] = "Update Stock"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


class UpdateInventoryView(UpdateView):
    template_name = 'core/inventory_form.html'
    success_url = reverse_lazy('inventory_list')
    model = Inventory
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'update inventory'
        context['header'] = "Update Inventory"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


class UpdateWaybillView(UpdateView):
    template_name = 'core/waybill_form.html'
    success_url = reverse_lazy('waybill_list')
    model = Waybill
    exclude = ('created_at',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'update waybill'
        context['header'] = "Update Waybill"
        context['delete_url'] = reverse_lazy('delete_stock')
        return context


class StockInventoriesListView(ListView):
    template_name = 'core/stock_inventory_list.html'
    model = Inventory

    def get_queryset(self):
        queryset = super().get_queryset().filter(stocks__id=self.kwargs['pk'])
        if self.kwargs['filter'] != 'all':
            queryset = queryset.filter(type=self.kwargs['filter'])
        return queryset.annotate(number=Sum('inventory_waybill_stock__inventory_number'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Inventory List"
        context['delete_url'] = reverse_lazy('delete_inventory')
        context['update_url'] = reverse_lazy('update_inventory')
        context['types'] = Inventory.TYPE_CHOICES
        return context


def delete_inventory(request, pk):
    obj = get_object_or_404(Inventory, id=pk)
    obj.delete()
    return redirect(reverse_lazy('inventory_list'))


def delete_stock(request, pk):
    obj = get_object_or_404(Stock, id=pk)
    obj.delete()
    return redirect(reverse_lazy('stock_list'))


def delete_waybill(request, pk):
    obj = get_object_or_404(Waybill, id=pk)
    obj.delete()
    return redirect(reverse_lazy('waybill_list'))
