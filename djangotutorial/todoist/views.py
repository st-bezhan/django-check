from django.shortcuts import render
from django.views import generic

from todoist.models import Todo


# Create your views here.

class IndexView(generic.ListView):
    template_name = "todoist/index.html"

    def get_queryset(self):
        """Return Todo objects ordered by not completed."""
        return Todo.objects.order_by("-completed")