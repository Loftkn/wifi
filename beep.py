from pygame import mixer


def beep():
    mixer.init()
    sound = mixer.Sound('beep.wav')
    sound.play()

beep()
