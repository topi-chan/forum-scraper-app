import random

import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url: str):
        self.url = url
        self.paragraphs = []
        self.headers = {
            "User-Agent": self.get_random_user_agent("user-agent-list.txt"),
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
    def get_random_user_agent(user_agent_list_file: str) -> str:
        user_agent = random.choice(open(user_agent_list_file).readlines())
        return user_agent.strip()

    def get_response(self) -> requests.Response:
        response = requests.get(
            self.url, headers=self.headers
        )  # for IP read add: stream=True
        # for IP read: print(request.raw._connection.sock.getsockname())
        return response

    def get_subpages_from_request(
        self, response: requests.Response, class_type: str, class_name: str = None
    ) -> list:
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup(class_type, class_name)
        for elem in div:
            self.paragraphs.append(elem)
        # for paragraph in self.paragraphs:
        #     print(paragraph.get_text(), ":   ", paragraph.get("href"))
        return self.paragraphs

    def get_tittles_and_links(self) -> dict:
        return {paragraph.get_text(): paragraph.get("href") for paragraph in self.paragraphs}

    @staticmethod
    def list_to_string(bs4_content: BeautifulSoup) -> str:
        str1 = " "
        return str1.join(bs4_content)


# example: Saab forum
scraper = Scraper("http://saabotage.pl/")
response = scraper.get_response()
scraper.get_subpages_from_request(response, "a", "forumlink")
d = scraper.get_tittles_and_links()
print(d)