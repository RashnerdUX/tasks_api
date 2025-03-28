from rest_framework.pagination import PageNumberPagination

class TodoPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "size"
    max_page_size = 100
