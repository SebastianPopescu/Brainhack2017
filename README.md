# Brainhack2017


Loading the .nii files

1. from command line in /home/username
   type realpath /home/username/CamCan/gm_data/* > ./realpath_camcan_gm.txt
   
2. from command line in /home/username
   type realpath /home/username/CamCan/wm_data/* > ./realpath_camcan_wm.txt

3. then go in the folder where you downloaded this repository and do the follwoing

    python load_CamCan.py --username=username --matter=gm
    python load_CamCan.py --username=username --matter=wm
    
You should obtain some .CSV files in /home/username/CamCan
