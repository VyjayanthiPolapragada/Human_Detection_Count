# Human Detector
Detect humans in real-time, image or video and count the detected people using OpenCV and HOG Descriptor

HOG (Histogram of Oreinted Gradient) - a feature descriptor used with OpenCV for object detection
The algorithm of HOG Descriptor is combined with SVM (Support Vector Machine) in OpenCV and this pre-trained model is used to detect people from the given file

Different functions are used for this detection:
1. human_detection.py: contains different functions implemented depending on the file format uploaded
2. main.py: main python code combining easygui to upload image/video and pass the arguments to detect people from the same

Libraries used: opencv,imutils,numpy,os,easygui 







