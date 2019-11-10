from django.urls import path

from core.views import StockFormView, InventoryFormView, WaybillFormView, InventoryListView, WaybillListView, StockListView


urlpatterns = [
    path('stock_form/', StockFormView.as_view(), name='stock_form'),
    path('inventory_form/', InventoryFormView.as_view(), name='inventory_form'),
    path('waybill_form/', WaybillFormView.as_view(), name='waybill_form'),
    path('stock_list/', StockListView.as_view(), name='stock_list'),
    path('inventory_list/', InventoryListView.as_view(), name='inventory_list'),
    path('waybill_list/', WaybillListView.as_view(), name='waybill_list'),
]
