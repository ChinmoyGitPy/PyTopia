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
    "cloud_fog": "cloud.webp",
    "gold_coin": "gold coin.png",
    "plain": "plain.png",
    "treasure_ruins": "treasure ruins.jpg"
}

font_filenames = {
    "bold":"Highcrest.ttf",
    "body":"GoudyMediaevalRegualar.ttf"
}

music_filename = "september.mp3"
music_path = r"C:\Users\Chinmoy\OneDrive\Documents\GitHub\PyTopia\Assets\september.mp3"


default_tile_width = 314
 
def load_assets(dir=asset_dir):
    if not py.get_init():
        py.init()
 
    if py.display.get_surface() is None:
        py.display.set_mode((1, 1))
 
    images = {}
 
    for key, filename in asset_filenames.items():
        path = os.path.join(dir, filename)
        if not os.path.isfile(path):
            print(f"{key} not loaded, file not found {path}")
            continue
        try:
            images[key] = py.image.load(path).convert_alpha()
        except Exception as e:
            print(f"{key} failed to load {filename}")
            continue
 
    return images

def load_fonts(dir=asset_dir,bold_size=28, body_size=20):
    if not py.get_init():
        py.init()
    if not py.font.get_init():
        py.font.inti()

    fonts = {}

    bold_path = os.path.join(dir, font_filenames["bold"])
    if os.path.isfile(bold_path):
        fonts["bold"] = py.font.Font(bold_path,bold_size)
    else:
        print(f"bold font not found at {bold_path}, using system default instead")
        fonts["bold"] = py.font.SysFont(None,bold_size)

    body_path = os.path.join(dir,font_filenames["body"])
    if os.path.isfile(body_path):
        fonts["bold"] = py.font.Font(body_path,body_size)
    else:
        print(f"body font not found at {body_path}, using system default instead")
        fonts["body"] = py.font.SysFont(None,body_size)

    return fonts

def load_and_play_music(path=music_path,volume=0.5):
    try:
        if not py.mixer.get_init():
            py.mixer.init()
        if not os.path.isfile(path):
            print(f"music file not found at {path}, continuing without music")
            return False
        py.mixer.music.load(path)
        py.mixer.music.set_volume(volume)
        py.mixer.music.play(loops=-1)
        return True

    except Exception as e:
        print(f"music falied to load/play: {e}")
        return False


    