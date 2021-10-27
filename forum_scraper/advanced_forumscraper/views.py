from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render
from django.views.generic import View
from forumscraper.views import IndexPageView, ScrapedSubforum
from forumscraper.scrap import Scraper
from forumscraper.forum_format import create_sorted_and_capitalized_topics_list


def make_redirect_advanced(request):
    return redirect(reverse('advanced_forumscraper:scraped'))


# class AdvancedScrapedSubforumChoose(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Here subforum list goes')

class AdvancedScrapedSubforumChoose(ScrapedSubforum):

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        scraper = Scraper("http://saabotage.pl/")
        response = scraper.get_response()
        scraper.get_subpages_from_response(response, "h4")
        context['subforum_dict'] = scraper.get_tittles_and_links()
        context['sub_level'] = 1
        return context


class AdvancedScrapedSubforum(ScrapedSubforum):

    # def __init__(self):
    #     self.subforum_address = ""
    #     super().__init__()
    #
    # def post(self, request, *args, **kwargs):
    #     self.subforum_address = request.POST['subforum']
    #     return self.subforum_address

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        scraper = Scraper("http://saabotage.pl/" + self.request.POST['subforum'].lstrip("."))
        response = scraper.get_response()
        scraper.get_subpages_from_response(response, "a", "forumlink")
        context['subforum_dict'] = scraper.get_tittles_and_links()
        return context


def make_redirect_advanced2(request):
    return redirect(reverse('advanced_forumscraper:subscraped'))


def render_link(request):
    scraper = Scraper("http://saabotage.pl/" + request.POST['subforum'].lstrip("."))
    full_topics_dict = {}
    while True:
        response = scraper.get_response()
        scraper.get_subpages_from_response(response, "a", "topictitle")
        topics_dict = scraper.get_tittles_and_links()
        full_topics_dict |= topics_dict
        scraper.paragraphs = []
        scraper.get_subpages_from_response(response, "a")
        link_lib = scraper.get_tittles_and_links()
        if link_lib.get('Następna strona') is None:
            break
        for tittle, link in link_lib.items():
            match tittle:
                case "Następna strona":
                    next_page = "http://saabotage.pl" + link.lstrip(".")
                    scraper = Scraper(next_page)
    for topic, link in full_topics_dict.items():
        full_topics_dict[topic] = ("http://saabotage.pl" + link.lstrip("."))
    context = {"topics_list": create_sorted_and_capitalized_topics_list(full_topics_dict)}
    return render(request, "index.html", context)