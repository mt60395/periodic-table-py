#!/usr/bin/env python
import json
import os
import urllib.request as urllib


def main():
    symbol = format_symbol(input("Element symbol: "))
    element = find_element_by_symbol(symbol)
    if element:
        find = {  # Properties to find and print
                "Name":"name",  # [To print]:[Property in the .json]
                "Atomic number": "number",
                "Period": "period",
                "Category": "category"
        }
        for attribute in find:
            print(attribute + ": " +
                  str(get_element_property(element, find[attribute])))
    else:
        print("Element does not exist.")


def get_dictionary():  # fetches the periodic table dictionary
    if not os.path.isfile('periodic-table-lookup.json'):
        urllib.urlretrieve(
            'https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/periodic-table-lookup.json',
            'periodic-table-lookup.json')
    f = open('periodic-table-lookup.json')
    return json.loads(f.read())


dictionary = get_dictionary()


def format_symbol(symbol):  # formats symbol property. Upper, then lower
    symbol = symbol.upper()
    if len(symbol) > 1:
        return symbol[0] + symbol[1].lower()
    return symbol


def find_element_by_symbol(symbol):
    for e in dictionary:
        for a in dictionary[e]:
            if a == "symbol" and dictionary[e][a] == symbol:
                return dictionary[e]


def get_element_property(element, attribute):
    for a in element:
        if a == attribute:
            return element[a]


if __name__ == "__main__":
    main()
