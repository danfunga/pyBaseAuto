# -*- coding: utf-8 -*-
import win32gui
from src.image_finder import ImageFinder
from src.image_clicker import ImageClicker as ImageClicker


class AppController:
    def __init__(self, window_title):
        self.window_title = window_title
        self.imageFinder = ImageFinder()
        self.imageClicker = ImageClicker()
        self.appHandle = self.get_app_handle()

    def get_app_handle(self):
        appHandle = win32gui.FindWindow(None, self.window_title)
        if appHandle == 0:
            print(f"Failed to find window with title '{self.window_title}'")
        else:
            print(f"Window with title '{self.window_title}' found successfully.")
        return appHandle

    def find_image(self, image_path):
        found, screenShot = self.imageFinder.capture_window_image(self.appHandle)
        if found:
            found, fileName, location = self.imageFinder.find_directory_on_Screen(screenShot, image_path)
            if found:
                print(f"Image found : {fileName}: {location}")
            else:
                print("Image not found after capturing screenshot.")
            return found, location
        else:
            print("Failed to capture screenshot of window.")
            return False, None

    def click_image(self, image_path):
        found, location = self.find_image(image_path)
        if found:
            success = self.imageClicker.click_at_location(self.appHandle, location)
            if success:
                print(f"Success to click {location}")
            else:
                print("failed to click {location}")

            return success
        else:
            print("Find Failed")
            return False

    def click_fixed_location(self, location):
        success = self.imageClicker.click_at_location(self.appHandle, location)
        if success:
            print(f"Success to click {location}")
        else:
            print("failed to click {location}")
        return success
