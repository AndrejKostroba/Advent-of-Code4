import math

with open('14.txt', 'r') as data:
    data = data.read().strip().split('\n')


def parse(data):
    reactions = {}
    for row in data:
        left, right = row.split(' => ')
        r_amount, r_name = right.split(' ')
        ingredients = {}
        for l_items in left.split(', '):
            amount, name = l_items.split(' ')
            ingredients[name] = int(amount)
        reactions[r_name] = (int(r_amount), ingredients)
    return reactions


def ore_needed(reactions):
    stock = {k: 0 for k in reactions.keys()}
    needed = {k: 0 for k in reactions.keys()}
    needed['FUEL'] = reactions['FUEL'][0]
    stock['ORE'] = needed['ORE'] = 0
    amount_needed = reactions['FUEL'][0]

    while amount_needed:
        for ingr in needed:
            if ingr == 'ORE' or not needed[ingr]:
                continue
            more_needed = needed[ingr] - stock[ingr]
            if more_needed:
                coeff = math.ceil(more_needed / reactions[ingr][0])
                stock[ingr] += coeff * reactions[ingr][0]
                for ingr2, need in reactions[ingr][1].items():
                    needed[ingr2] += coeff * need
                    if ingr2 != 'ORE':
                        amount_needed += coeff * need
            stock[ingr] -= needed[ingr]
            amount_needed -= needed[ingr]
            needed[ingr] = 0

    return needed['ORE']


reactions = parse(data)
print(f'Part 1: {ore_needed(reactions)}')  # 97422
