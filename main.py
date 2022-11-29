import subprocess
from beep import track


def single_scan(mac, channel):
    subprocess.Popen(['airodump-ng',
                      '-w', 'single',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1',
                      '--bssid', mac,
                      '-c', channel])


def general_scan():
    subprocess.Popen(['airodump-ng',
                      '-w', 'general',
                      '--output-format', 'csv',
                      '--background', '1',
                      '-I', '1'])
