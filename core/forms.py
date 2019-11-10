from django import forms
from core.models import Stock, Inventory, Waybill


'''- Добавление/редактирование/удаление информации о рабочем инвентаре.
- Добавление/редактирование/удаление информации о складах.
- Добавление/редактирование/удаление информации о приходе и расходе рабочего инвентаря.
- Просмотр списка инвентаря заданного типа на заданном складе и его количество на текущую дату.
- Просмотр списка всех приходов и расходов инвентаря заданного наименования на всех складах 
    – дата, название инвентаря, список - дата прихода, количество, дата расхода, количество.
- Просмотр списка всех складов, отсортированных по названию на текущую дату.'''


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'


class WaybillForm(forms.ModelForm):
    class Meta:
        model = Waybill
        exclude = ('created_at',)
