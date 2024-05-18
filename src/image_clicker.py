import win32api
import win32con
import win32gui
import time

class Clicker:
    # caption = _string_caption or 'BlueStacks'
    # local hwnd1 = FindWindow('Qt5154QWindowOwnDCIcon', _string_caption)
    # local hwnd2 = FindWindowEx(hwnd1, '', 'plrNativeInputWindowClass', 'plrNativeInputWindow')
    # local hwnd3 = FindWindowEx(hwnd2, '', 'BlueStacksApp', '_ctl.Window')
    # print('hwnd1 : '..hwnd1, 'hwnd2 : '..hwnd2, 'hwnd3 : '..hwnd3)
    


    def click_at_location(self, handle, location):
        if location and handle:
            # 이미지의 중심 좌표 계산
            center_x = location[0] + location[2] // 2
            center_y = location[1] + location[3] // 2
            
            innerHandle = win32gui.FindWindowEx(handle, None, None,None)

            win32gui.PostMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
            # win32api.SetCursorPos((center_x, center_y))
            # 메뉴창으 눌린다.
            lParam = win32api.MAKELONG(center_x, center_y)
            win32api.PostMessage(innerHandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32api.PostMessage(innerHandle, win32con.WM_LBUTTONUP, None, lParam)

            print(f"Clicked on image  at ({center_x}, {center_y})")
            return True
        else:
            print(f"Image  not found on screen or handle not provided.")
            return False