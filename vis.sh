#!/bin/bash

root_folder= #'./ExPI/' ## set your path
actor=$1
action=$2
camera=$3
vis=$4

# vis in 2d/3d/2d3d
python vis_mocap.py --root_folder $root_folder --actor_name $actor  --action_name $action --camera_name $camera --vis $vis

# jpg2mp4
cd out
ffmpeg -pattern_type glob -i $actor'_'$action'_'$vis'_cam'$camera'_*.jpg'\
       -c:v libx264 -pix_fmt yuv420p \
       -movflags +faststart 'vis'$vis'_'$actor'_'$action'_'$camera'.mp4'
rm *.jpg
cd ..

