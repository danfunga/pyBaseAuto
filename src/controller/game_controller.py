# -*- coding: utf-8 -*-
import win32gui
from src.controller.image_detector import ImageDetector
from src.controller.image_clicker import ImageClicker as ImageClicker


class GameController:
    def __init__(self, window_title):
        self.window_title = window_title
        self.image_detector = ImageDetector()
        self.image_clicker = ImageClicker()
        self.appHandle = self.get_app_handle()

    def get_app_handle(self):
        appHandle = win32gui.FindWindow(None, self.window_title)
        if appHandle == 0:
            print(f"Failed to find window with title '{self.window_title}'")
        else:
            print(f"Window with title '{self.window_title}' found successfully.")
        return appHandle

    def find_image(self, image_path):
        found, screen_shot = self.image_detector.capture_window_image(self.appHandle)
        if found:
            found, file_name, location = self.image_detector.find_directory_on_Screen(screen_shot, image_path)
            if found:
                print(f"Image found : {file_name}: {location}")
            else:
                print("Image not found after capturing screenshot.")
            return found, location
        else:
            print("Failed to capture screenshot of window.")
            return False, None

    def click_image(self, image_path):
        found, location = self.find_image(image_path)
        if found:
            success = self.image_clicker.click_at_location(self.appHandle, location)
            if success:
                print(f"Success to click {location}")
            else:
                print("failed to click {location}")

            return success
        else:
            print("Find Failed")
            return False

    def click_fixed_location(self, location):
        success = self.image_clicker.click_at_location(self.appHandle, location)
        if success:
            print(f"Success to click {location}")
        else:
            print("failed to click {location}")
        return success
