from django.contrib import admin

# Register your models here.
from .models import InventoryTable, PendingRequest, ProcessedRequest,Vendor

admin.site.register(InventoryTable)
admin.site.register(PendingRequest)
admin.site.register(ProcessedRequest)
admin.site.register(Vendor)