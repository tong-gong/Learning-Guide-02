#!/usr/bin/env python3

# Created by: Tong Gong
# Created time: November 2020
# This is the hello world program

import ugame
import stage

def game_scene():
    # This function is the main game_scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layer = [background]
    game.render_block()
    # REPEAT FOREVER, game loop
    while True:
        pass

if __name__ == "__main__":
    game_scene()
