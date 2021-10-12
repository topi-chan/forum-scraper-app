def create_topics_list(topics_dict: dict) -> list:
    topics_list = []
    for link, tittle in topics_dict.items():
        topics_list_element = '<a href = "{}" > {} < / a >'.format(link, tittle)
        topics_list.append(topics_list_element)
    return topics_list

