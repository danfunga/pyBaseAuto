# -*- coding: utf-8 -*-

from src.controller import ImageController
# from src.image_finder import finder

def main():
    # 윈도우 제목과 "나가기" 디렉토리 경로
    window_title = "main"  # 실제 윈도우 제목으로 변경
    directory_path = 'images/leave/'  # "나가기" 디렉토리 경로
    print("한글을 포함한 문자열 출력")

    # ImageController 인스턴스 생성
    controller = ImageController(window_title)
    # get_screenshot_by_window_title(window_title)

    # if controller.click_fixed_location( (477,290,10,10) ):
        # print("Clicked on an image in 'leave' directory successfully.")
    # else:
        # print("No images found in 'leave' directory.")

    # "나가기" 디렉토리 내부의 이미지를 클릭
    if controller.click_image(directory_path):
        print("Clicked on an image in 'leave' directory successfully.")
    else:
        print("No images found in 'leave' directory.")

if __name__ == '__main__':
    main()