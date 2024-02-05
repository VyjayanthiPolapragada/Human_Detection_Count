#main 

#importing libraies 

import easygui
import human_detection as hd

print("Welcome to human detector")

file=input("Enter which type of file to choose: Image/Video/Camera")
print('Press Q to exit')

#no path is assigned in case of camera
if file=='Camera':
    path=None
    hd.humanDetector(path,file)
else:
    path=easygui.fileopenbox(title='Upload Image/Video file')
    hd.humanDetector(path,file)
print('Thank you!')