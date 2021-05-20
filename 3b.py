def first_repeating_symbol(list_):
    """
    Get the first repeating symbol in the given list of symbols.

    :param list_: list of symbols.
    :return: the first repeating element in the list.
    """
    new_list = []
    for symbol in list_of_symbols:
        if symbol not in new_list:
            new_list.append(symbol)
        else:
            return symbol


if __name__ == '__main__':
    list_of_symbols = [1, 2, 4, {2: 'a', 3: 'b'}, [1, 2], 6, 's', [1, 2], 2]
    print(first_repeating_symbol(list_of_symbols))
