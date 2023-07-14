from django.contrib import admin
from .models import *


class OrderItemInLine(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	inlines = [OrderItemInLine]


# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Rented)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Reserved)
