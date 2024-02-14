import django_filters

from network.models import NetworkLink


class LinkCountryFilter(django_filters.FilterSet):
    """
    Custom Filter for searching links in Country.
    """
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains",)

    class Meta:
        model = NetworkLink
        fields = ('country',)
