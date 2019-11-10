from django.urls import path

from core.views import CreateStockView, CreateInventoryView, CreateWaybillView, \
                       InventoryListView, WaybillListView, StockListView, \
                       UpdateStockView, UpdateInventoryView, UpdateWaybillView, \
                       DeleteStockView, DeleteInventoryView, DeleteWaybillView


urlpatterns = [
    path('stock_form/', CreateStockView.as_view(), name='stock_form'),
    path('inventory_form/', CreateInventoryView.as_view(), name='inventory_form'),
    path('waybill_form/', CreateWaybillView.as_view(), name='waybill_form'),
    path('stock_list/', StockListView.as_view(), name='stock_list'),
    path('inventory_list/', InventoryListView.as_view(), name='inventory_list'),
    path('waybill_list/', WaybillListView.as_view(), name='waybill_list'),
]
