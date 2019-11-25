from django.urls import path, re_path
import re

from core.views import CreateStockView, CreateInventoryView, CreateWaybillView, InventoryListView, WaybillListView, \
    StockListView, UpdateStockView, UpdateInventoryView, UpdateWaybillView, StockInventoriesListView, delete_stock, \
    delete_inventory, delete_waybill


urlpatterns = [
    path(r'create_stock/', CreateStockView.as_view(), name='create_stock'),
    path(r'create_inventory/', CreateInventoryView.as_view(), name='create_inventory'),
    path(r'stock_list/', StockListView.as_view(), name='stock_list'),
    path(r'inventory_list/', InventoryListView.as_view(), name='inventory_list'),
    path(r'waybill_list/', WaybillListView.as_view(), name='waybill_list'),
    path(r'update_stock/<int:pk>', UpdateStockView.as_view(), name='update_stock'),
    path(r'update_inventory/<int:pk>', UpdateInventoryView.as_view(), name='update_inventory'),
    path(r'update_waybill/<int:pk>', UpdateWaybillView.as_view(), name='update_waybill'),
    path(r'delete_inventory/<int:pk>', delete_inventory, name='delete_inventory'),
    path(r'delete_stock/<int:pk>', delete_stock, name='delete_stock'),
    path(r'delete_waybill/<int:pk>', delete_waybill, name='delete_waybill'),
    path(r'stock_<int:pk>/inventories/<str:filter>', StockInventoriesListView.as_view(), name='stock_inventories_list'),
    path(r'stock_<int:pk>/waybills', CreateWaybillView.as_view(), name='create_waybill'),
]
