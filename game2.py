import subprocess
import RPi.GPIO as GPIO
import time

Models = 'Matrix'

arguements = ['/opt/fpp/src/fppmm', '-m', 'a' , '-o', 'on']

#Start and stop race list.
race_play = ['/opt/fpp/src/fpp', '-p', 'fill']
race_stop = ['/opt/fpp/src/fpp', '-c', 'stop']
attract_sequence = ['/opt/fpp/src/fpp', '-p', 'attract']

#List of programs to cycle attract and during race.
attract_programs = ['attract1', 'attract2', 'attract3', 'attract4',]
play_programs = ['fill1', 'fill2', 'fill3', 'fill4', ]
winner_programs = ['winner1', 'winner2', 'winner3', 'winner4',]


enable_sequence = ['/opt/fpp/src/fpp', '-p', 'enable']
winner_sequence = ['/opt/fpp/src/fpp', '-P', 'winner']

class PlayerState:
    ATTRACT = 1
    ENABLED = 2
    DISABLED = 3
    WINNER = 4
    NOT_WINNER = 5

class GameState:
    NOT_PLAYING = 6
    PLAYING = 7


class RacePins:
    ATTRACT_PIN = 5
    ENABLED_PIN = 6
    PLAY_PIN = 20
    NOT_PLAYING_PIN = 4
    WINNER_PIN = 16
    NOT_WINNER_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(fill_trigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.PLAY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.ATTRACT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.ENABLED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.WINNER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.NOT_WINNER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(game_increment, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RacePins.NOT_PLAYING_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


player_state = PlayerState.ATTRACT

game_state = GameState.NOT_PLAYING

while True:
    if (player_state == PlayerState.ATTRACT and game_state == GameState.NOT_PLAYING):
        subprocess.run(attract_sequence)
