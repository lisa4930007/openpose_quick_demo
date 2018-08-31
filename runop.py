# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:25:52 2018

Openpose_quick_demo

@author: Yun-Ting Lai
"""

import sys
import os
from os.path import join, exists, splitext
from datetime import datetime
   
##### Configurations #####

body = True
face = False
hand = False
run_on_gpu = True
display_processed_window = True
save_as_json = True
save_as_video = False
save_as_images = False

##########################

datetime = datetime.now().strftime('%m%d%H%M%S') # month;day;hour;minute;second

unit='1'
if run_on_gpu:
    unit = '2'
    
para1=''
if display_processed_window: 
    para1=' --display -1 '
    
if body==True and face==True and hand==True: # body+face+hand
    para2=' --render_pose '+unit+' -face --face_render '+unit+' --face_net_resolution 320x320 -hand --hand_render '+unit+' --hand_net_resolution 320x320 --hand_tracking '
elif body==True and face==False and hand==True: # body+hand
    para2=' --render_pose '+unit+' -hand --hand_render '+unit+' --hand_net_resolution 320x320 --hand_tracking '
elif body==True and face==True and hand==False: # body+face
    para2=' --render_pose '+unit+' -face --face_render '+unit+' --face_net_resolution 320x320 '
elif body==False and face==True and hand==False: # only face
    para2=' --render_pose '+unit+' -face --face_render '+unit+' --face_net_resolution 320x320 --body_disable '
elif body==True and face==False and hand==False: # only body
    para2=' --render_pose '+unit
else:
    sys.exit("Oops! We do not have this option!")

# 取得 target_videos 所有檔案與子目錄名稱
files = os.listdir('target_videos')
for filename in files:
    name, ext = splitext(filename)
    
    if ext != '.mp4' and ext != '.avi':
        print ('Video format: '+ext+'; Only support: mp4, avi.')
        continue

    main_process='bin\OpenPoseDemo.exe --video target_videos/'+filename+' '+para2+para1

    if save_as_json:
        main_process+=' --write_json output_json/'+name+'_'+datetime
    if save_as_video:
        main_process+=' --write_video output_video/'+name+'_'+datetime+'.avi '
    if save_as_images:
        main_process+=' --write_images output_images/'+name+'_'+datetime

    os.system(main_process)
    print ('Process of video '+filename+' finished')