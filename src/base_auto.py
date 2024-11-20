# -*- coding: utf-8 -*-

# from src.controller import game_controller
from controller import GameController

from config.config_manager import ConfigManager


# from src.image_finder import finder
class BaseAuto:
    def __init__(self):
        self.config_manager = ConfigManager()
        app_title = self.config_manager.get('Settings', 'app_title')
        self.controller = GameController(app_title)
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

    # def launch(self):
    #     # 초기화 및 GUI 준비
    #     print("BaseAuto 준비 중...")
    #     self.is_running = True
# def start(self):
#     # 매크로 작업 시작
#     print("매크로 시작!")
#     while self.is_running:
#         if self.is_stopping:
#             if self.current_mode.is_finished():
#                 print("모드 종료 완료. 종료 중...")
#                 break  # 모드가 끝났다면 종료
#         else:
#             if self.current_mode is None:
#                 print("현재 모드가 설정되지 않았습니다.")
#                 break
#
#             self.current_mode.perform_action()
#
#             if self.current_mode.is_finished():
#                 print(f"{self.current_mode.__class__.__name__} 작업 완료.")
#                 self.transition_to_next_mode()
#
# def transition_to_next_mode(self):
#     # 현재 모드 종료 후 다음 모드로 전환
#     next_mode = self.current_mode.get_next_mode()
#     if next_mode:
#         print(f"{next_mode.__class__.__name__} 모드로 전환 중...")
#         self.set_mode(next_mode)
#     else:
#         print("모든 작업이 끝났습니다. 종료합니다.")
#         self.stop()
#
# def set_mode(self, mode):
#     # 모드 설정
#     self.current_mode = mode
#     self.current_mode.start()
#
# def stop(self):
#     # 종료 신호 받으면 작업을 마무리하고 종료
#     print("종료 신호를 받았습니다. 작업을 마무리 중...")
#     self.is_stopping = True