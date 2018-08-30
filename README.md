# openpose_quick_demo

# Prerequisites:
OS: Windows (8, 10) with CUDA (Nvidia GPU)

# Download and install
1.CUDA 8 & cuDNN 5.1
2.Anaconda3 - python with basic library

# Steps:
1.Download the files.
2.Put your target videos into folder "target_videos" and ready for the execution.
(待確認) Video's extention should be '.mp4' or '.avi'.

3.Check configurations in **configuration** section

body = True
face = False
hand = False

**use "body", "face", "hand" to decide 5 detection modes:**
1.body+face+hand
2.body+hand
3.body+face
4.only face [Note that option only possible for faster (but less accurate) face keypoint detection.]
5.only body

use_gpu = True [Otherwise, run on CPU.]
display_processing_window = False [Display the processing_window or not]

save_as_json = True
save_as_video = False
save_as_images = Fale

3.Run the "runop.py" script.
4.Output data "skeleton json files", "processing video", "processing images" are stored in folders "output_json", "output_video, "output_images" respectively.

# [Output Format](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md)

# Advanced 
directly use command line
[flag參考](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/demo_overview.md)
