from django.urls import path
from .views import IndexPageView, make_redirect, ScrapedSubforum, render_link

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('scrap_and_render_subforums', make_redirect, name='scrap_subforums'),
    path('subfora', ScrapedSubforum.as_view(), name='scraped'),
    path('links', render_link, name='links'),
]
