import subprocess
from beep import track
from os import remove


MONINTERFACE = 'wlp0s20f3mon'


def clean():
    try:
        remove('general-01.csv')
    except FileNotFoundError:
        pass
    try:
        remove('single-01.csv')
    except FileNotFoundError:
        pass


def single_scan(mac, channel):
    clean()
    subprocess.Popen(['airodump-ng',
                      '-w', 'single',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      '--bssid', mac,
                      '-c', channel,
                      MONINTERFACE])
    track()


def general_scan():
    clean()
    subprocess.Popen(['airodump-ng',
                      '-w', 'general',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      MONINTERFACE])
