# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment - Unit0-04
# This program is the Hello, World! program, but as a GUI with 3 buttons

import ui

def english_touch_up_inside(sender):
    # displays the English version
    view['hello_world_label'].text = ('Hello, World!')

def french_touch_up_inside(sender):
    # displays the French version
    view['hello_world_label'].text = ('Bonjour, Monde!')

def spanish_touch_up_inside(sender):
    # displays the Spanish version
    view['hello_world_label'].text = ('iHola, Mundo!')

view = ui.load_view()
view.present('full_screen')
