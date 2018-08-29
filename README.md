# openpose_quick_demo

環境
windows GPU 安裝 cudnn..
Anaconda3 - python with basic library




1.Download the files.
2.Check configurations in **configuration** section

Put your target videos into folder "target_videos" and ready for the execution.
Video's extention should be '.mp4' or '.avi'.


body = True
face = False
hand = False

use 3 parameters to decide 5 detection modes:
# body+face+hand
# body+hand
# body+face
# only face => 
# only body

use_gpu = True
display_processed_window = False **default



save_as_json = True
save_as_video = False
save_as_images = Fale


output_json
output_video
output_images


3.Run the "runop.py" script.

 


json 

節點 請參考


其他用法
可以直接用command line 然後flag可參考
