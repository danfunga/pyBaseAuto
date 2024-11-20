import configparser
import os


class ConfigManager:
    def __init__(self, config_file='config/config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.default_settings = {
            'Gui_Config': {
                'pos_x': '20',
                'pos_y': '448'
            },
            'Settings': {
                'app_title': 'main',
                'play_role': '단독',
                'game_type': '전체'
            },
            'StandaloneMode_Roles': {
                '랭대': '1',
                '리그': '1',
                '보상': '1',
                '스테': '1',
                '실대': '0',
                '친구': '1',
                '클협': '0',
                '타홀': '1',
                '홈런': '1',
                '히스': '1'
            },
            'Detail_Settings': {
                'role_order': '리그,실대,홈런,랭대,히스,스테,타홀,클협,친구,보상',
                'enable_use_equip_on_ranking_battle': '0',
                'enable_front_active': '1'
            },
            'Delay_Settings': {
                'click_delay': '1',
                'change_window_delay': '2',
                'skip_delay': '0.1',
                'reboot_delay': '20'
            },
            'Statistics': {
                '등반': '0',
                '랭대': '0',
                '로얄': '0',
                '리그': '0',
                '보상': '0',
                '스테': '0',
                '실대': '0',
                '친구': '0',
                '클협': '0',
                '타홀': '0',
                '홈런': '0',
                '히스': '0',
                '매니저': '0',
                '매니저_성공': '0',
                '재기동': '0',
                '재기동_성공': '0',
                '탭닫기': '1',
                '탭닫기_성공': '1'
            }
        }

        # Ensure the config directory exists
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)

        # If the config file does not exist, create it with default settings
        if not os.path.exists(self.config_file):
            self.create_default_config()

        self.config.read(self.config_file, 'utf-8')

    def create_default_config(self):
        for section, options in self.default_settings.items():
            self.config[section] = options
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def get(self, section, option, fallback=None):
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            if fallback is not None:
                return fallback
            else:
                raise e

    def set(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def get_section(self, section):
        if not self.config.has_section(section):
            raise configparser.NoSectionError(section)
        return dict(self.config.items(section))

    def add_section(self, section):
        if not self.config.has_section(section):
            self.config.add_section(section)
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

    def remove_section(self, section):
        if self.config.has_section(section):
            self.config.remove_section(section)
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

    def remove_option(self, section, option):
        if self.config.has_section(section) and self.config.has_option(section, option):
            self.config.remove_option(section, option)
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

    # def save(self):
    #     with open(self.config_file, 'w',encoding='utf-8') as configfile:
    #         self.config.write(configfile)

