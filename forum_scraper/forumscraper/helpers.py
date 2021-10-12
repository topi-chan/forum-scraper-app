from functools import wraps


def link_reformat(function):
    #@wraps(function)
    def wrapper(dict):
        for topic, link in dict.items():
            dict[topic] = ("http://saabotage.pl/" + link.lstrip("."))
        return dict
    return wrapper
