import subprocess
from beep import track


MONINTERFACE = 'wlp0s20f3mon'


def single_scan(mac, channel):
    subprocess.Popen(['airodump-ng',
                      '-w', 'single',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      '--bssid', mac,
                      '-c', channel,
                      MONINTERFACE])


def general_scan():
    subprocess.Popen(['airodump-ng',
                      '-w', 'general',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      MONINTERFACE])
