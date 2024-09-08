import pgzrun
import random

WIDTH = 800
HEIGHT = 650

ITEMS = ["bag","bottle","chips","battery"]
items = []
background = Actor('bground')
current_level = 1


def draw():
    background.draw()
    for i in items:
        i.draw()


def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(current_level):
    items_to_create = get_items_to_create(current_level)
    draw_items = create(items_to_create)
    layout_items(draw_items)
    return draw_items

def get_items_to_create(current_level):
    items_to_create = ["paper"]
    for i in range(0,current_level):
        random_items = random.choice(ITEMS)
        items_to_create.append(random_items)
    return items_to_create

def create(items_to_create):
    things = []
    for i in items_to_create:
        item = Actor(i)
        things.append(item)
    return things


def layout_items(items_to_layout):
    gaps = len(items_to_layout) + 1
    gap_size = WIDTH/gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate (items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos



pgzrun.go()
