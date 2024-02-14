from rest_framework import pagination


class NetworkPagination(pagination.PageNumberPagination):
    """
    Custom class for pagination for Network Link.
    """
    page_size = 5  # Number of elements per page
    page_size_query_param = 'page_size'  # Query parameter to specify the number of elements on the page
    max_page_size = 50  # Maximum number of elements per page


class ProductPagination(pagination.PageNumberPagination):
    """
    Custom class for pagination for Product.
    """
    page_size = 5  # Number of elements per page
    page_size_query_param = 'page_size'  # Query parameter to specify the number of elements on the page
    max_page_size = 50  # Maximum number of elements per page
