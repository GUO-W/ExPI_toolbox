#!/usr/bin/env python
# encoding: utf-8
# Software ExPI_toolbox
# Copyright Inria
# Year 2021
# Contact : wen.guo@inria.fr

import csv
import os
import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib._png import read_png
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from tqdm import tqdm
import argparse
import xml.dom.minidom as xmldom
import math
from util import vis_acro_2d, vis_acro_3d, read_calib, read_gt_clean, world2img, order_orig,\
        check_img2world, find_standform_3dline, find_norm_3dline, find_point_3dline, nearest_intersection

def parse_args():
    parser = argparse.ArgumentParser(description='vis 3D mocap for acro dataset')
    parser.add_argument('--root_folder',
            help = 'path to your data',
            default = '/mnt/beegfs/perception/wguo/acro_dataset/data/',
            type = str)
    parser.add_argument('--actor_name',
            help = 'acro1 or acro2',
            default = 'acro1',
            type = str)
    parser.add_argument('--action_name',
            help = 'action name',
            default = 'a-frame2',
            type = str)
    parser.add_argument('--camera_name',
            help = 'camera name',
            default = 20,
            type = int)
    parser.add_argument('--vis',
            help = '2d or 3d or 2d3d',
            default = '2d3d',
            type = str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    actor_name = args.actor_name #'acro1'
    action_name = args.action_name #'cartwheel6'
    root_path = args.root_folder + actor_name + '/' + action_name + '/'
    img_folder = root_path + 'IMG/cam-0'+str(args.camera_name)+'/'
    nb_kpts = 36

	## read gt
    gt = read_gt_clean(root_path)

    ## read camara calib file
    P,K,R,T,xc,yc,K1,K2 = read_calib(root_path + 'calib-new.xml', args.camera_name)

    ## vis
    for img_name in tqdm(os.listdir(img_folder)):
        #kpts = gt[img_name]
        #kpts = np.array(kpts).reshape(nb_kpts,3)
        #kpts_dict = {order[i]:kpts[i] for i in range(nb_kpts)}
        #kpts_3d = [kpts_dict[o] for o in order_orig]
        #kpts_3d = np.array(kpts_3d, dtype=np.float32).reshape((nb_kpts, 3))#.tolist()
        kpts_3d  = gt[img_name]

        #check_img2world(kpts_3d,root_path)
        if args.vis == '3d':
            ### vis_3d
            save_path = './out/' + actor_name+'_'+ action_name + '_3d_cam' + str(args.camera_name) + '_' + img_name
            vis_acro_3d(kpts_3d, save_path) #480*640*3

        if args.vis == '2d':
            ### project world3D to img2D
            kpts_2d = world2img(kpts_3d, P,K,R,T, xc, yc, K1, K2)
            ### vis_2d
            cvimg = cv2.imread(img_folder + img_name, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
            img_2d = vis_acro_2d(cvimg, kpts_2d, './out/' + actor_name+'_'+ action_name + '_2d_cam' + str(args.camera_name) + '_' + img_name) #2048*2048*3

        if args.vis == '2d3d':
            ### vis_3d
            vis_acro_3d(kpts_3d, './out/' + actor_name + '_' + action_name + '_3d_' + img_name) #480*640*3
            ### project world3D to img2D
            kpts_2d = world2img(kpts_3d, P,K,R,T, xc, yc, K1, K2)
            ### vis_2d
            cvimg = cv2.imread(img_folder + img_name, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
            img_2d = vis_acro_2d(cvimg, kpts_2d)#, './out/' + actor_name+'_'+ action_name + '_2d_cam' + str(args.camera_name) + '_' + img_name)
            ### concat 2d 3d
            img_3d = cv2.imread('./out/' + actor_name + '_' + action_name + '_3d_' + img_name)
            x_2d,y_2d = img_2d.shape[0:2]
            x_3d,y_3d = img_3d.shape[0:2]
            img_3d = cv2.resize(img_3d, (x_3d*2,y_3d*2))
            img_3d = cv2.copyMakeBorder(img_3d, int((x_2d-x_3d*2)/2), int((x_2d-x_3d*2)/2), int((y_2d-y_3d*2)/2), int((x_2d-x_3d*2)/2), cv2.BORDER_CONSTANT,value=[255,255,255])
            img_3d = cv2.resize(img_3d, (x_2d,y_2d))
            img_2d3d = cv2.hconcat([img_2d,img_3d])
            if use_gt_new:
                save_path = './out/' + actor_name+'_'+ action_name + '_2d3d_cam' + str(args.camera_name) + '_cleaned_' + img_name
            else:
                save_path = './out/' + actor_name+'_'+ action_name + '_2d3d_cam' + str(args.camera_name) + '_old_' + img_name
            cv2.imwrite(save_path, img_2d3d)

if __name__ == '__main__':
        main()



