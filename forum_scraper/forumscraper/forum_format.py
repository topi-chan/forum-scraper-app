from collections import OrderedDict


def create_topics_list(topics_dict: dict) -> list:
    topics_list = []
    for tittle, link in topics_dict.items():
        topics_list_element = '<a href = "{}" > {} < / a >'.format(tittle, link)
        topics_list.append(topics_list_element)
    return topics_list


def create_sorted_and_capitalized_topics_list(topics_dict: dict) -> list:
    topics_list = []
    topics_dict = {tittle.capitalize(): link for tittle, link in topics_dict.items()}
    sorted_topics_dict = OrderedDict(sorted(topics_dict.items()))
    for tittle, link in sorted_topics_dict.items():
        topics_list_element = '<a href = "{}" > {} < / a >'.format(tittle, link)
        topics_list.append(topics_list_element)
    return topics_list

