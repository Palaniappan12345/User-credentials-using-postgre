

# Note: This is just a hack until we figure out the perfect solution
def serialize_db_objects(_list):

    new_list = []
    for item in _list:
        new_list.append(item.as_dict())

    return new_list