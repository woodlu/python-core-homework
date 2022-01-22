def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    result = {"categories": []}

    for i in mapping["categoryIdsSorted"]:
        tempCategory = mapping["categories"][i]
        category = {"id": "category-" + i, "text": tempCategory["name"], "items": []}
        for r in tempCategory["roleIds"]:
            tempRole = mapping["roles"][r]
            role = {"id": tempRole["id"], "text": tempRole["name"]}
            category["items"].append(role)
        result["categories"].append(category)

    return result
#    pass

