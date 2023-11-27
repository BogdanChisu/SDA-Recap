"""
Write a program (or function) that will compare the area/price ratio between
two pizzas. In order to calculate the area of a circle P at a given radius r
"""
from math import pi

dictionary_sizes = {
    32: 15,
    36: 20
}

ratios = []

def circle_area_to_price(dict):
    for item in dict.keys():
        area = pi * dict[item] ** 2
        ratios.append(area / dict[item])

    max_ratio = max(ratios)
    max_index = ratios.index(max_ratio)

    return f'Max area to price ratio for: ' \
           f'{list(dictionary_sizes.items())[max_index]}'

print(circle_area_to_price(dictionary_sizes))