![Python](https://img.shields.io/badge/python-3.8.8-3670A0?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-1.7.1-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24.1-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
[[Project]](https://github.com/zachnguyen03/opencv_spycam)

# OpenCV Spycam - Official Implementation
This is the official code of our **"SCMIT: Style Consistent Multi-Domain Image-to-Image Translation"**, TBD, 2024

## **Requirements**
-opencv-python>=4.9.0.80

## **Initialzing spycam**
1. Webcam mode
`python main.py --mode webcam`
2. Video mode
`python main.py --mode video`

## **Parameters**
1. **IP address**: used to specify the destination for cv2.VideoCapture
- Set to 0: OpenCV capture your computer's webcam
- Set to a RTSP address: OpenCV captures the camera (e.g CCTV) from the specified RTSP IP address
2. **Codec**: specify the codec which cv2.VideoWriter uses to make the output video
- Available codecs: 'MJPG' (recommended for 'avi'), 'DVIX', 'MP4V' 
3. **FPS**: specify the FPS of the output video (default: 10.0)
4. **Mode**: specify the starting mode of the VideoCapture 
- This mode can be changed during the capture by pressing SPACE key

## **Features**
1. Applying filter to VideoCapture - In progress


