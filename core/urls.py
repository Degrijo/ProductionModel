from django.urls import path

from core.views import CreateStockView, CreateInventoryView, CreateWaybillView, InventoryListView, WaybillListView, \
    StockListView, UpdateStockView, UpdateInventoryView, UpdateWaybillView, StockInventoriesListView, delete_stock, \
    delete_inventory, delete_waybill


urlpatterns = [
    path('create_stock/', CreateStockView.as_view(), name='create_stock'),
    path('create_inventory/', CreateInventoryView.as_view(), name='create_inventory'),
    path('stock_list/', StockListView.as_view(), name='stock_list'),
    path('inventory_list/', InventoryListView.as_view(), name='inventory_list'),
    path('waybill_list/', WaybillListView.as_view(), name='waybill_list'),
    path('update_stock/<int:pk>', UpdateStockView.as_view(), name='update_stock'),
    path('update_inventory/<int:pk>', UpdateInventoryView.as_view(), name='update_inventory'),
    path('update_waybill/<int:pk>', UpdateWaybillView.as_view(), name='update_waybill'),
    path('delete_inventory/<int:pk>', delete_inventory, name='delete_inventory'),
    path('delete_stock/<int:pk>', delete_stock, name='delete_stock'),
    path('delete_waybill/<int:pk>', delete_waybill, name='delete_waybill'),
    path('stock_<int:pk>/inventories', StockInventoriesListView, name='stock_inventories_list'),
    path('stock_<int:pk>/waybills', CreateWaybillView.as_view(), name='create_waybill'),
]
