import csv
from time import sleep
from pygame import mixer


def beep():
    mixer.init()
    sound = mixer.Sound("sound.wav")
    sound.play()


def show_data():
    with open('single-01.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)
        next(reader)

        return abs(int(next(reader)[8].strip()))


def track():
    MAX_TIME = 2.85
    MIN_TIME = 0.15
    MAX_POWER = 60
    MIN_POWER = 10

    last_pw = show_data()
    delay = ((last_pw - MIN_POWER)/(MAX_POWER-MIN_POWER))*(MAX_TIME-MIN_TIME) + MIN_TIME

    while True:
        beep()
        sleep(delay)
        current_pw = show_data()
        delay = delay + ((current_pw - last_pw) * (MAX_TIME-MIN_TIME)) / (MAX_POWER-MIN_POWER)
        if delay < MIN_TIME or current_pw < MIN_POWER:
            current_pw = MIN_POWER
            delay = MIN_TIME
        if delay > MAX_TIME or current_pw > MAX_POWER:
            current_pw = MAX_POWER
            delay = MAX_TIME
        last_pw = current_pw


if __name__ == '__main__':
    track()
