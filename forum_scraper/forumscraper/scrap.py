import random

import requests
from bs4 import BeautifulSoup


def get_random_user_agent(user_agent_list_file):
    user_agent = random.choice(open(user_agent_list_file).readlines())
    return user_agent.strip()


class Scraper:
    def __init__(self, url):
        self.url = url
        self.paragraphs = []
        self.headers = {
            "User-Agent": get_random_user_agent("user-agent-list.txt"),
            "Accept-Language": "en-gb",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com",
            "Pragma": "no-cache",
        }
        # self.proxies = {
        #     'http': 'http://10.10.1.10:example',
        #     'https': 'http://10.10.1.10:example',
        # }

    @staticmethod
    def list_to_string(bs4_content):
        str1 = " "
        return str1.join(bs4_content)

    def get_subpages(self, class_type, class_name=None, recursive=None):
        request = requests.get(self.url, headers=self.headers)  # for IP read add: stream=True
        # for IP read: print(request.raw._connection.sock.getsockname())
        soup = BeautifulSoup(request.text, "html.parser")
        div = soup(class_type, class_name)
        for elem in div:
            self.paragraphs.append(elem)
        for paragraph in self.paragraphs:
            print(paragraph.get_text(), ":   ", paragraph.get("href"))


# example: Saab forum
scraper = Scraper("http://saabotage.pl/")
scraper.get_subpages("a", "forumlink")
