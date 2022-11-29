#!/bin/bash

airodump-ng --background 1 -w single --output-format csv -I 1 --bssid $1 -c 6 wlp0s20f3mon


