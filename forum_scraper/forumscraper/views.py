from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .scrap import Scraper


class IndexPageView(TemplateView):

    template_name = "index.html"


class ScrapedSubforum(IndexPageView):

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        scraper = Scraper("http://saabotage.pl/")
        response = scraper.get_response()
        scraper.get_subpages_from_request(response, "a", "forumlink")
        context['subforum_dict'] = scraper.get_tittles_and_links()
        return context


def make_redirect(request):
    return redirect('scraped')


def render_link(request):
    # scraper = Scraper("http://saabotage.pl/" + request.POST['subforum']) TODO
    # response = scraper.get_response()
    # scraper.get_subpages_from_request(response, "a", "forumlink")
    #context['subforum_dict'] = scraper.get_tittles_and_links()
    print(request.POST['subforum'])
    return render(request, "index.html")