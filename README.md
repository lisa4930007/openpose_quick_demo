# openpose_quick_demo

## Prerequisites: 
OS: Windows (8, 10) with CUDA (Nvidia GPU)

## Download and install
1.CUDA 8 & cuDNN 5.1<br/>
2.Anaconda3 - python with basic library<br/>

## Steps:
1.Download the files.<br/>
2.Put your target videos into folder "target_videos" and ready for the execution.<br/>
(待確認) Video's extention should be '.mp4' or '.avi'.<br/>

3.Check configurations in **configuration** section<br/>
<br/>
body = True<br/>
face = False<br/>
hand = False<br/>
<br/>
**use "body", "face", "hand" to decide 5 detection modes:**<br/>
1.body+face+hand<br/>
2.body+hand<br/>
3.body+face<br/>
4.only face [Note that option only possible for faster (but less accurate) face keypoint detection.]<br/>
5.only body<br/>
<br/>
use_gpu = True [Otherwise, run on CPU.]<br/>
display_processing_window = False [Display the processing_window or not]<br/>
<br/>
save_as_json = True<br/>
save_as_video = False<br/>
save_as_images = Fale<br/>

3.Run the "runop.py" script.<br/>
4.Output data "skeleton json files", "processing video", "processing images" are stored in folders "output_json", "output_video, "output_images" respectively.

## Output Format
[link](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md)

## Advanced 
directly use command line 
[flag參考](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/demo_overview.md)
