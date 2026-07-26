import os
import pygame as py

asset_dir = r"C:\Users\Chinmoy\OneDrive\Documents\GitHub\PyTopia\Assets"
asset_filenames = {
    
    "forest": "forest.png",
    "mine": "mine.png",
    "metal_ores": "metal ores.png",
    "fisherman": "fisherman.png",
    "lake": "lake.png",
    "barn": "barn.png",
    "animal": "animal.jpg",
    "animal_2": "animal 2.png",
    "sawmill": "sawmill.png",
    "capital": "capital.jpg",
    "city": "city.jpg",
    "village": "village.jpg",
    "fog": "fog.jpg",
    "gold_coin": "gold coin.png",
    "plain": "plain.png",
    "treasure_ruins": "treasure ruins.jpg"
}

default_tile_width = 314

def load_assets(dir = asset_dir):
    if not py.get_init():
        py.init()

    if py.display.get_surface() is None:
        py.display.set_mode((1,1))

    images = {}

    for key,filename in asset_dir.items():
        path = os.path.join(dir,filename)
        if not os.path.isfile(path):
            print(f"{key} not loaded, file not found {path}")
            continue
        try:
            images[key] = py.image.load(path).convert_alpha()
        except Exception as e:
            print(f"{key} failed to load {filename}")
            continue

    return images 