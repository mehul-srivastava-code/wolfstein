import pygame as pg
import os
import sys

def resource_path(relative_path):
    # Get the absolute path to the resource, works for dev and PyInstaller bundle
    try:
        base_path = sys._MEIPASS  # Only exists in bundled mode
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Sound:
    def __init__(self, game):
        self.game = game
        self.sound_enabled = True

        try:
            pg.mixer.init()
            print("✅ Sound initialized.")
        except pg.error as e:
            print(f"⚠️ Warning: Sound could not be initialized. Reason: {e}")
            self.sound_enabled = False
            return  # Skip loading sounds

        try:
            self.shotgun = pg.mixer.Sound(resource_path('resources/sound/shotgun.wav'))
            self.npc_pain = pg.mixer.Sound(resource_path('resources/sound/npc_pain.wav'))
            self.npc_death = pg.mixer.Sound(resource_path('resources/sound/npc_death.wav'))
            self.npc_shot = pg.mixer.Sound(resource_path('resources/sound/npc_attack.wav'))
            self.npc_shot.set_volume(0.2)
            self.player_pain = pg.mixer.Sound(resource_path('resources/sound/player_pain.wav'))
            pg.mixer.music.load(resource_path('resources/sound/theme.mp3'))
            pg.mixer.music.set_volume(0.3)
        except Exception as e:
            print(f"⚠️ Error loading sound files: {e}")
            self.sound_enabled = False
