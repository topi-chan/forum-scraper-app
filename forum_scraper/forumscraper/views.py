from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .scrap import Scraper
from .forum_format import create_sorted_and_capitalized_topics_list


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


# def render_link(request):
#     scraper = Scraper("http://saabotage.pl/" + request.POST['subforum'].lstrip("."))
#     response = scraper.get_response()
#     scraper.get_subpages_from_request(response, "a", "topictitle")
#     topics_dict = scraper.get_tittles_and_links()
#     for topic, link in topics_dict.items():
#         topics_dict[topic] = ("http://saabotage.pl" + link.lstrip("."))
#     context = {"topics_list": create_sorted_and_capitalized_topics_list(topics_dict)}
#     return render(request, "index.html", context)


def render_link(request):
    scraper = Scraper("http://saabotage.pl/" + request.POST['subforum'].lstrip("."))
    full_topics_dict = {}
    while True:
        response = scraper.get_response()
        scraper.get_subpages_from_request(response, "a", "topictitle")
        topics_dict = scraper.get_tittles_and_links()
        full_topics_dict |= topics_dict
        scraper.paragraphs = []
        scraper.get_subpages_from_request(response, "a")
        link_lib = scraper.get_tittles_and_links()
        for tittle, link in link_lib.items():
            match tittle:
                case "Następna strona":
                    next_page = "http://saabotage.pl" + link.lstrip(".")
                    print(next_page)
                    scraper.url = next_page
                    print(full_topics_dict)
                    continue
                case _:
                    print('x')
        break
    for topic, link in full_topics_dict.items():
        full_topics_dict[topic] = ("http://saabotage.pl" + link.lstrip("."))
    context = {"topics_list": create_sorted_and_capitalized_topics_list(full_topics_dict)}
    return render(request, "index.html", context)
