
    
def Screenshot():
    import numpy as np
    import cv2
    import pyautogui
    import time
    import os
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite("Files_Jarvis\\Screenshots\\image.png", image)  
    f_path = "D:\\All Mess\\Jarvis AI Main Project\\Files_Jarvis\\Screenshots\\image.png"
    t = os.path.getctime(f_path)
    t_str = time.ctime(t)
    t_obj = time.strptime(t_str)
    form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    form_t = form_t.replace(":", "꞉")

    os.rename(
        f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1])





  