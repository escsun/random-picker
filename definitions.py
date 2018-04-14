import os
import yaml

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is the project root path
LOAD_OPTIONS = yaml.safe_load(open(os.path.join(ROOT_DIR, 'configuration.yml')))  # load options

YOUTUBE_OPTIONS = LOAD_OPTIONS["youtube"]
TWITCH_OPTIONS = LOAD_OPTIONS["twitch"]
GOODGAME_OPTIONS = LOAD_OPTIONS["goodgame"]
