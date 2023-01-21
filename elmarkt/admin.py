from django.contrib import admin

from .models import Contact, Product, Participant, Supplier
from django_admin_relation_links import AdminChangeLinksMixin


@admin.action(description='Обнулить долги')
def debts_to_zero(modeladmin, request, queryset):
    queryset.update(debt=0)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "number")
    search_fields = ("email", "country", "city", "street", "number")
    list_editable = ("country", "city", "street", "number")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "model", "issued", "show_sellers")
    search_fields = ("title", "model", "issued", "show_sellers")
    list_editable = ["model"]

    def show_sellers(self, obj):
        return "\n".join([a.title for a in obj.sellers.all()])


class ParticipantAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ("title", "level", "contact", "show_products", "created")
    search_fields = ("title", "level", "contact", "show_products", "created")
    list_editable = ("level", "contact")
    list_filter = ['contact__city']
    changelist_links = [
        ('buyer', {
            'label': 'Поставщик',  # Used as label for the link
            'model': 'Supplier'  # Specify a different model, you can also specify an app using `app.Member`
        })
    ]

    def show_products(self, obj):
        return "\n".join([a.title for a in obj.products.all()])


class SupplierAdmin(admin.ModelAdmin):
    list_display = ("seller", "buyer", "debt")
    search_fields = ("seller", "buyer", "debt")
    list_editable = ("buyer", "debt")
    actions = [debts_to_zero]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Supplier, SupplierAdmin)
