from django.urls import path

from core.views import CreateStockView, CreateInventoryView, CreateWaybillView, \
                       InventoryListView, WaybillListView, StockListView, \
                       UpdateStockView, UpdateInventoryView, UpdateWaybillView, \
                       delete_stock, delete_inventory, delete_waybill


urlpatterns = [
    path('create_stock/', CreateStockView.as_view(), name='create_stock'),
    path('create_inventory/', CreateInventoryView.as_view(), name='create_inventory'),
    path('create_waybill/', CreateWaybillView.as_view(), name='create_waybill'),
    path('stock_list/', StockListView.as_view(), name='stock_list'),
    path('inventory_list/', InventoryListView.as_view(), name='inventory_list'),
    path('waybill_list/', WaybillListView.as_view(), name='waybill_list'),
    path('update_stock/', UpdateStockView.as_view(), name='update_stock'),
    path('update_inventory/', UpdateInventoryView.as_view(), name='update_inventory'),
    path('update_waybill/', UpdateWaybillView.as_view(), name='update_waybill'),
    path('delete_inventory/', delete_inventory, name='delete_inventory'),
    path('delete_stock/', delete_stock, name='delete_stock'),
    path('delete_waybill/', delete_waybill, name='delete_waybill'),
]
