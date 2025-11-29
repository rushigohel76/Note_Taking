from django.db import connection
from Notes.models import MyModel

def my_view(request):
    data = MyModel.objects.filter(some_field='value')
    # The query is executed here when data is evaluated (e.g., iterated over)
    print(connection.queries)
    # ... further processing and rendering...