class Mode:
    def __init__(self):
        self.is_done = False  # 작업 완료 여부 추적

    def start(self):
        print(f"{self.__class__.__name__} 시작!")

    def perform_action(self):
        # 각 모드별 동작 수행
        print(f"{self.__class__.__name__} 동작 수행 중...")
        self.is_done = True  # 작업 완료 표시

    def is_finished(self):
        return self.is_done  # 작업 완료되었는지 체크