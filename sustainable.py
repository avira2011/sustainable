import pgzrun
import random

WIDTH = 800
HEIGHT = 650

items = ["bag","bottle","chips","battery"]
background = Actor('bground')
 
def draw():
    background.draw()

def make_items(current_level):
    items_to_create = get_items_to_create(current_level)
    draw_items = create(items_to_create)

def get_items_to_create(current_level):
    items_to_create = ["paper"]
    for i in range(0,current_level):
        random_items = random.choice(items)
        items_to_create.append(random_items)
    return items_to_create






pgzrun.go()