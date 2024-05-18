# -*- coding: utf-8 -*-

from src.app_controller import AppController
from src.config_manager import ConfigManager


# from src.image_finder import finder
class BaseAuto:
    def __init__(self):
        self.config_manager = ConfigManager()
        app_title = self.config_manager.get('Settings', 'app_title')
        self.controller = AppController(app_title)
    def start(self):
        # Settings 섹션의 값을 가져오기
        app_title = self.config_manager.get('Settings', 'app_title', fallback='N/A')
        play_role = self.config_manager.get('Settings', 'play_role', fallback='N/A')
        game_type = self.config_manager.get('Settings', 'game_type', fallback='N/A')
        print(f"App Title: {app_title}")
        print(f"Play Role: {play_role}")
        print(f"Game Type: {game_type}")

        # GUI_POSITION 섹션의 값을 가져오기
        gui_config = self.config_manager.get_section('Gui_Config')
        print("GUI Config:", gui_config)

        # STANDALONE_ENABLED_MODE 섹션의 값을 가져오기
        standalone_mode = self.config_manager.get_section('StandaloneMode_Roles')
        print("Standalone Mode Roles:", standalone_mode)

        # Detail_Settings 섹션의 값을 가져오기
        detail_settings = self.config_manager.get_section('Detail_Settings')
        print("Detail Settings:", detail_settings)

        # Delay_Settings 섹션의 값을 가져오기
        delay_settings = self.config_manager.get_section('Delay_Settings')
        print("Delay Settings:", delay_settings)

        # Statistics 섹션의 값을 가져오기
        statistics = self.config_manager.get_section('Statistics')
        print("Statistics:", statistics)

        # 필요에 따라 설정 값 변경
        # self.config_manager.set('Settings', 'app_title', 'Updated App Title')
        updated_app_title = self.config_manager.get('Settings', 'app_title')
        print(f"Updated App Title: {updated_app_title}")

        directory_path = '../images/leave/'
        # if controller.click_fixed_location((477, 290, 10, 10)):
        #     print("Clicked on an image in 'leave' directory successfully.")
        # else:
        #     print("No images found in 'leave' directory.")

        # "나가기" 디렉토리 내부의 이미지를 클릭

        if self.controller.click_image(directory_path):
            print("Clicked on an image in 'leave' directory successfully.")
        else:
            print("No images found in 'leave' directory.")
