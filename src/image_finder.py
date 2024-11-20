# -*- coding: utf-8 -*-
import win32ui
import win32con
import win32gui
from PIL import Image
import numpy as np
import cv2
import os
# import logging

class ImageFinder:
    def __init__(self):
        self.init = 1
    #     self.logger = logging.getLogger(__name__)

    def capture_window_image(self, appHandle):
        try:
            left, top, right, bot = win32gui.GetWindowRect(appHandle)
            width = right - left
            height = bot - top

            hwndDC = win32gui.GetWindowDC(appHandle)
            mfcDC = win32ui.CreateDCFromHandle(hwndDC)
            saveDC = mfcDC.CreateCompatibleDC()

            saveBitMap = win32ui.CreateBitmap()
            saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)

            saveDC.SelectObject(saveBitMap)

            saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

            bmpinfo = saveBitMap.GetInfo()
            bmpstr = saveBitMap.GetBitmapBits(True)

            image = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
            image.save("screenShot.png")
            screenshot_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)            
            return True, screenshot_cv2
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False, None

    def find_directory_on_Screen(self, screen_image, target_image_path, confidence=0.8):
        for filename in os.listdir(target_image_path):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(target_image_path, filename)
                template = cv2.imread(image_path, cv2.IMREAD_COLOR)        
                if template is None:
                    print(f"Image '{image_path}' not found.")
                    return False, None
        
                # 템플릿 매칭을 수행
                result = cv2.matchTemplate(screen_image, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
                # 일치율이 confidence보다 높으면 해당 위치를 반환
                if max_val >= confidence:
                    return True, image_path,(max_loc[0],max_loc[1], template.shape[1], template.shape[0])
                return False, None, None
        return False, None, None