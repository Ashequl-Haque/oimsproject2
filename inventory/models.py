from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.
class InventoryTable(models.Model):
	item_name=models.CharField(max_length=100,blank=False,null=False, unique=True, db_index=True)
	quantity_inside=models.IntegerField()
	quantity_outside=models.IntegerField()
	minimum_quantity=models.IntegerField()
	unit_price=models.DecimalField(max_digits=10, decimal_places=5)
	description=models.TextField()
	vendor=models.CharField(max_length=100,blank=False,null=False)

	def update(self):
		self.save()

	def __str__(self):
		return self.item_name

class PendingRequest(models.Model):
	id_no=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	item_name=models.CharField(max_length=100,blank=False,null=False)
	requested_quantity=models.IntegerField()
	requestee=models.CharField(max_length=100,blank=False,null=False)
	store_manager=models.CharField(max_length=100,blank=False,null=False)
	description=models.TextField()
	date_of_request=models.DateField(auto_now=True)

	def update(self):
		self.save()

	def __str__(self):
		return str(self.id_no)


class ProcessedRequest(models.Model):
	id_no=models.UUIDField(primary_key=True,default=0, editable=False)
	item_name=models.CharField(max_length=100,blank=False,null=False)
	requested_quantity=models.IntegerField()
	requestee=models.CharField(max_length=100,blank=False,null=False)
	store_manager=models.CharField(max_length=100,blank=False,null=False)
	description=models.TextField()
	date_of_request=models.DateField()

	processed_by=models.CharField(max_length=100,blank=False,null=False)
	date_of_process=models.DateField(auto_now=True)
	action=models.CharField(max_length=10, blank=False, null=False)
	acknowledgement=models.IntegerField(default=0)

	def update(self):
		self.save()

	def __str__(self):
		return str(self.id_no)


class Vendor(models.Model):
	name = models.CharField(max_length=100,blank=False,null=False)
	address = models.CharField(max_length=200,blank=False,null=False)
	contact = models.CharField(max_length=50,blank=False,null=False)
	email = models.CharField(max_length=100,blank=False,null=False)
	description = models.TextField()
	date_added = models.DateField(auto_now_add= True)
	date_modified = models.DateField(auto_now= True)
	added_by = models.CharField(max_length=50,blank=False,null=False)
	modified_by = models.CharField(max_length=50,blank=False,null=False)
	is_active = models.IntegerField(default=1)
	vendor_id = models.AutoField(primary_key=True)

	def __str__(self):
		return str(self.vendor_id)

	 
