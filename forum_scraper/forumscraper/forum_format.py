from collections import OrderedDict


def create_topics_list(topics_dict: dict) -> list:
    topics_list = []
    for tittle, link in topics_dict.items():
        topics_list_element = '<a href = "{}" > {} < / a >'.format(tittle, link)
        topics_list.append(topics_list_element)
    return topics_list


def sort_and_capitalize_dict(topics_dict: dict) -> OrderedDict:
    topics_dict = {tittle.capitalize(): link for tittle, link in topics_dict.items()}
    return OrderedDict(sorted(topics_dict.items()))


def create_sorted_and_capitalized_topics_list(topics_dict: dict) -> list:
    topics_list = []
    sorted_topics_dict = sort_and_capitalize_dict(topics_dict)
    for tittle, link in sorted_topics_dict.items():
        topics_list_element = '<a href = "{}" > {} < / a >'.format(tittle, link)
        topics_list.append(topics_list_element)
    return topics_list


def create_sorted_and_capitalized_topics_list_forum_format(topics_dict: dict) -> list:
    topics_list = []
    sorted_topics_dict = sort_and_capitalize_dict(topics_dict)
    for tittle, link in sorted_topics_dict.items():
        topics_list_element = '[*][url={}] [color=grey]{}[/color][/url]'.format(link, tittle)
        topics_list.append(topics_list_element)
    topics_list.insert(0, '[list]')
    topics_list.append('[/list]')
    return topics_list
