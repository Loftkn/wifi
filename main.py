import subprocess
from beep import track
from os import remove
from time import sleep


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
    sleep(2)
    track()


def general_scan():
    clean()
    subprocess.Popen(['airodump-ng',
                      '-w', 'general',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      MONINTERFACE])


single_scan('AA:34:6A:2D:6C:C0', '6')
