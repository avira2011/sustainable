import pgzrun
import random

WIDTH = 800
HEIGHT = 650

ITEMS = ["blue-star","green-star","orange-star","purple-star", "red-star"]
items = []
background = Actor('bground')
current_level = 1
animations = []
game_over = False
START_SPEED = 10

def display_message(i):
    screen.draw.text(i,fontsize = 60, center = (400,325), color = "black")
    
def draw():
    background.draw()
    if game_over:
        display_message("GAME OVER, TRY AGAIN")
    else:
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
    animates(draw_items)
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

def animates(animations_to_create):
    global animations
    for i in animations_to_create:
        duration = START_SPEED - current_level
        i.anchor = ("center", "bottom")
        animation = animate(i,duration = duration, on_finished = handle_game_over, y=HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True


pgzrun.go()
