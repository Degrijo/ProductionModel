from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce

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
            number=Coalesce(Sum('inventory_waybill_stock__inventory_number', filter=Q(stocks__id=self.kwargs['pk'])), 0))
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
                        int(value) > int(request.POST['max_' + key]):
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
        return redirect(reverse_lazy('create_waybill', kwargs={'pk': self.kwargs['pk']}))


class InventoryListView(ListView):
    template_name = 'core/inventory_list.html'
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory list'
        context['header'] = "Inventory List"
        return context


class WaybillListView(ListView):
    template_name = 'core/waybill_list.html'
    queryset = Waybill.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Waybill List'
        context['header'] = "Waybill List"
        return context


class StockListView(ListView):
    template_name = 'core/stock_list.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'stock list'
        context['header'] = "Stock List"
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
        return context


class UpdateWaybillView(UpdateView):
    template_name = 'core/update_waybill_form.html'
    success_url = reverse_lazy('waybill_list')
    model = Waybill
    fields = ('employee_name', 'employee_position')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'update waybill'
        context['header'] = "Update Waybill"
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
        context['types'] = Inventory.TYPE_CHOICES
        return context


class InventoryDetailView(DetailView):
    template_name = 'core/inventory_detail.html'
    model = Inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'inventory detail'
        context['header'] = "Inventory Detail"
        context['waybills'] = self.get_object().inventory_waybill_stock.values('waybill__created_at', 'inventory_number',
                                                                               'waybill__id')
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
