from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from network.models import Product, NetworkLink


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date',)
    search_fields = ('name', 'model',)
    list_filter = ('release_date',)


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'email', 'country', 'city', 'street', 'house_number', 'purveyor_link', 'debt',
        'hierarchy',
    )
    list_filter = ('city',)
    search_fields = ('name',)
    actions = ('clear_debt',)

    def purveyor_link(self, obj):
        if obj.purveyor:
            url = reverse("admin:network_networklink_change", args=[obj.purveyor.pk])
            link = '<a href="%s">%s</a>' % (url, obj.purveyor)
            return mark_safe(link)
        return '-'

    purveyor_link.short_description = _('Purveyor')

    @admin.action(description=_('Clear debt to purveyor'))
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
