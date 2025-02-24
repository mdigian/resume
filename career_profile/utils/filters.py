def filter_by_role(data, role):

    return [item for item in data if getattr(item, 'title', None) == role]