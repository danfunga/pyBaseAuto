

# PyAutoBase 프로젝트 구조

`PyAutoBase`는 Com2uS의 프로야구 매크로를 자동화하는 Python 기반의 프로젝트입니다. 이 프로젝트는 다양한 모드를 지원하며, 각 모드는 독립적으로 동작하고, 작업을 완료한 후 다음 모드로 전환됩니다. 전체 흐름은 GUI와 매크로 루프를 통해 제어됩니다.

## 설계
BaseAuto
  * GameController 
    * ImageDetector
      * 추후 AI를 통한 ImageDetect를 수행하면 좋겠다.
    * ImageClicker
  * ModeMap <ModeName, Mode >
  * ConfigManager
    * Config를 File에 저장 및 관리
    * Statistic의 경우를 별도로 할지 함께 할지
    * ConfigStatManager??
  * BaseAutoGUI
    * ConfigStatManager의 data와 동기가 되는 GUI
    * 최초 Config를 File에서 읽어서 GUI에 표현하고
    * start시 GUI의 값을 읽어서 File에 저장 Sync
  * Player
    * Config의 Mode 값으로 player를 생성된다.
    * Config의 Mode가 단독이라면 
      * Config의 Enabled 정보로 Setting된다
      * Count는 각 mode 별로 얻어온다.
      * 단독일 경우와 개별일 경우를 얻어온다. static
      * 


## 프로젝트 디렉토리 구조

```
PyAutoBase/
├── README.md # 프로젝트 설명 파일
├── main.py # 프로그램 시작점 (BaseAuto 실행)
├── src/ # 소스 코드
│ ├── init.py # 패키지 초기화 파일
│ ├── base_auto.py # BaseAuto 클래스 (매크로 루프 및 초기화)
│ ├── controller/ # 제어 관련 클래스들 (이미지 탐지 및 클릭)
│ │ ├── init.py # 패키지 초기화 파일
│ │ ├── image_detector.py # 이미지 탐지 클래스(ImageDetector)
│ │ └── image_clicker.py # 이미지 클릭 클래스 (ImageClicker)
│ ├── mode/ # 다양한 모드들 (홈런 모드, 랭킹 모드 등)
│ │ ├── init.py # 패키지 초기화 파일
│ │ ├── home_run_mode.py # 홈런 모드 (HomeRunMode)
│ │ └── ranking_mode.py # 랭킹 모드 (RankingMode)
│ └── gui/ # GUI 관련 코드
│ ├── init.py # 패키지 초기화 파일
│ └── gui.py # GUI 클래스
├── config/ # 설정 파일 (config.json 등)
├── requirements.txt # 필요한 패키지 목록
└── utils/ # 유틸리티 함수들
└── logger.py # 로깅 유틸리티
```

## 주요 디렉토리 설명

### `src/`
`src/` 디렉토리는 프로젝트의 주요 소스 코드가 포함된 디렉토리입니다. 각 기능은 `controller`, `mode`, `gui` 등 여러 서브 디렉토리로 나누어져 있습니다.

- **`base_auto.py`**: `BaseAuto` 클래스를 포함하며, 매크로의 루프와 상태 관리, 모드 전환을 담당합니다.
- **`controller/`**: 이미지 탐지 및 클릭과 관련된 기능을 제공하는 클래스들이 포함됩니다.
    - **`image_detector.py`**: 화면에서 이미지 탐지 및 좌표 반환 기능을 수행합니다.
    - **`image_clicker.py`**: 탐지된 좌표를 클릭하거나 키보드 입력을 처리합니다.
- **`mode/`**: 매크로에서 실행될 각 모드들을 정의하는 디렉토리입니다.
    - **`home_run_mode.py`**: 홈런 모드 작업을 처리합니다.
    - **`ranking_mode.py`**: 랭킹 모드 작업을 처리합니다.
- **`gui/`**: GUI 구성 요소를 포함하며, 사용자가 프로그램을 제어할 수 있도록 합니다.
    - **`gui.py`**: 프로그램의 GUI 관련 코드가 포함됩니다.

### `config/`
프로젝트 설정 파일들이 포함됩니다. 예를 들어, `config.json` 파일에는 사용자가 정의할 수 있는 설정 값들이 저장됩니다.

### `requirements.txt`
이 파일은 프로젝트에서 필요한 Python 패키지를 나열합니다. 예를 들어, `opencv`, `pyautogui`, `tkinter` 등이 포함될 수 있습니다.

### `utils/`
프로젝트 전반에 걸쳐 재사용되는 유틸리티 함수들을 포함합니다. 예를 들어, 로깅 기능을 담당하는 `logger.py`가 있을 수 있습니다.

## 실행 방법

1. **필요한 라이브러리 설치**:
   ```bash
   pip install -r requirements.txt
