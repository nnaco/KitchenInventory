# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

available_eggs = make_fried_egg(available_eggs)

#
def use_flour(available_flour, flour_to_use):
    if flour_to_use > available_flour:
        print('The kitchen does not have enough flour.')
        return available_flour

    print(f'{flour_to_use} flour used out of {available_flour} available.')
    return available_flour - flour_to_use

use_flour(available_flour, 1)
print(available_flour)

def make_dough(available_flour):
    has_enough_flour = available_flour >= 1

    if has_enough_flour:
        available_flour = use_flour(available_flour, 1)
        print('Made a Loaf of bread. Yippy!')
    else:
        print('Could not make bread. Not enough flour!')

    return available_flour

available_flour = make_dough(available_flour)


check_kitchen_stock()
