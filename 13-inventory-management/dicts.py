"""
Exercise 13 - Inventory Management
"""

def create_inventory (items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return add_items ({}, items)


def add_items (inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    return add_or_decrement_items (inventory, items, 'add')


def decrement_items (inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    return add_or_decrement_items (inventory, items, 'minus')


def remove_item (inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item not in inventory:
        return inventory

    inventory.pop (item)
    return inventory


def list_inventory (inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    result = []

    for element, quantity in inventory.items():
        if quantity > 0:
            result.append ((element, quantity))

    return result


def add_or_decrement_items (inventory, items, operation):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :param operation: string - 'add' or 'minus'.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        if not item in inventory:
            if operation == 'add':
                inventory[item] = 1
        else:
            if operation == 'add':
                inventory[item] += 1
            else:
                if inventory[item] > 0:
                    inventory[item] -= 1

    return inventory