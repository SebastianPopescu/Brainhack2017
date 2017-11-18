#!/bin/sh


username='adam'

realpath /home/$username/CamCan/gm_data/* > /home/$username/realpath_camcan_gm.txt

python load_CamCan.py --username=$username