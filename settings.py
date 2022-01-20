from dataclasses import dataclass


@dataclass
class Settings:
    FPS: int = 100
    proportions_game_screen: tuple = (880, 640)
    fields_size: int = 80

    proportions_for_map: tuple = (80, 80)
    proportions_for_map_of_chest_and_heal: tuple = (50, 50)

    proportions_of_goblin: tuple = (50, 80)
    proportions_of_goblin_in_fight: tuple = (150, 180)
    positions_goblin_in_fight: tuple = (600, 400)

    proportions_of_knight_in_fight: tuple = (350, 300)
    proportions_knight_in_fight: tuple = (10, 300)

    proportions_of_ent_in_fight: tuple = (350, 380)
    proportions_ent_in_fight: tuple = (500, 250)

    proportions_of_slime_in_fight: tuple = (350, 380)
    proportions_slime_in_fight: tuple = (500, 250)

    proportions_of_dark_knight_in_fight: tuple = (350, 300)
    proportions_dark_knight_in_fight: tuple = (500, 210)