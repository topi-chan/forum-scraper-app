from django.urls import path
from .views import IndexPageView, AdvancedScrapedSubforum, AdvancedScrapedSubSubforum, make_redirect_advanced, \
    render_link, make_redirect_advanced2

app_name = 'advanced_forumscraper'
urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('scrap_and_render_subforums', make_redirect_advanced, name='scrap_subforums'),
    path('subfora', AdvancedScrapedSubforum.as_view(), name='scraped'),
    path('scrap_and_render_subsubforums', make_redirect_advanced2, name='scrap_subforums'),
    path('subsubfora', AdvancedScrapedSubSubforum.as_view(), name='subscraped'),
    path('links', render_link, name='links'),
]
