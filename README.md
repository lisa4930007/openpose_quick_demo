# openpose_quick_demo

## Prerequisites: 
OS: Windows (8, 10) with CUDA (Nvidia GPU)

## Download and install
1. CUDA 8 & cuDNN 5.1<br/>
2. Anaconda3 which contains python with basic library <br/>

## Follow the steps:
1. Download [openpose_quick_demo.zip](https://drive.google.com/file/d/1NZDv_lqPTIm7O-yfCI3T6puDZ49KSlit/view?usp=sharing) file.<br/>
2. Put your target videos into folder "target_videos" and ready for the execution.<br/>
(待確認) Video's extention should be '.mp4' or '.avi'.<br/>

3. Open "runop.py" script in program editor(Spyder), and check configurations in **configurations** section<br/>
You can set "True" or "False" for each parameters to decide to run it or not according to your purpose.
> body = True<br/>
> face = False<br/>
> hand = False<br/>
>> use "body", "face", "hand" to decide 5 detection modes:
>>- body+face+hand
>>- body+hand
>>- body+face
>>- only face   **[Note that option only possible for faster (but less accurate) face keypoint detection.]**<br/>
>>- only body

> run_on_gpu = True   **[Otherwise, run on CPU.]**<br/>
> display_processing_window = False   **[Display the processing_window or not]**<br/>
> save_as_json = True<br/>
> save_as_video = False<br/>
> save_as_images = Fale<br/>

4. Run the script!<br/>
5. Output data "skeleton json files", "processing video", "processing images" are stored in folders "output_json", "output_video, "output_images", respectively.


## Output Format
Please look at details from [link](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md)

## Advanced (待新增)
directly use command line <br/>
[flag參考](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/demo_overview.md)
tryrebase
