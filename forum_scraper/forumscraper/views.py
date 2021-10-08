from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):

    template_name = "index.html"

# Generate list of forum tittles by scrap.py and place them here with jinja2, html drop-down list and redirect method
