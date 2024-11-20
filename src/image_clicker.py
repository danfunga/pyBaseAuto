import win32api
import win32con
import win32gui
import time


class ImageClicker:

    def click_at_location(self, handle, location):
        if location and handle:
            # 이미지의 중심 좌표 계산
            center_x = location[0] + location[2] // 2
            center_y = location[1] + location[3] // 2

            innerHandle = win32gui.FindWindowEx(handle, None, None, None)

            # Active를 해야 하네..
            win32gui.PostMessage(innerHandle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)

            lParam = win32api.MAKELONG(center_x, center_y)
            win32api.PostMessage(innerHandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32api.PostMessage(innerHandle, win32con.WM_LBUTTONUP, None, lParam)

            print(f"Clicked on image  at ({center_x}, {center_y})")
            return True
        else:
            print(f"Image  not found on screen or handle not provided.")
            return False
