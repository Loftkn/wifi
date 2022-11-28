from pygame import mixer


def beep():
    mixer.init()
    sound = mixer.Sound('sound.wav')
    sound.play()

beep()
