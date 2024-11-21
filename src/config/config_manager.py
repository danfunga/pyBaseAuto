import configparser
import os


class ConfigManager:
    DEFAULT_ALONE_MODE_ROLE_ENABLE = {
        '리그': 1,
        '랭대': 1,
        '홈런': 1,
        '패넌': 1,
        '스테': 1,
        '타홀': 1,
        '히스': 1,
        '친구': 1,
        '보상': 1,
        '실대': 0,
    }
    DEFAULT_COUNT_PER_SINGLE_MODE = {
        '리그': -1,
        '랭대': -1,
        '홈런': -1,
        '패넌': -1,
        '스테': -1,
        '타홀': -1,
        '히스': -1,
        '친구': 40,
        '보상': 1,
        '실대': 2,
    }
    DEFAULT_COUNT_PER_ALONE_MODE = {
        '리그': (5, -1),
        '랭대': (-1, -1),
        '홈런': (-1, -1),
        '패넌': (1, 1),
        '스테': (3, 3),
        '타홀': (-1, -1),
        '히스': (-1, -1),
        '친구': (10, -1),
        '보상': (1, -1),
        '실대': (2, 1),
    }

    # '단독'을 맨 앞에, '등반'을 맨 뒤에 추가
    DEFAULT_ROLE_LIST = ['단독'] + list(DEFAULT_ALONE_MODE_ROLE_ENABLE.keys())

    def __init__(self, config_file='config/config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        role_order = [role for role in ConfigManager.DEFAULT_ALONE_MODE_ROLE_ENABLE.keys()]
        # 'role_order'를 쉼표로 구분된 문자열로 결합
        role_order_str = ','.join(role_order)
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
            'StandaloneMode_Roles':
                ConfigManager.DEFAULT_ALONE_MODE_ROLE_ENABLE
            ,
            'Detail_Settings': {
                'role_order': role_order_str,
                'enable_use_equip_on_ranking_battle': '0',
                'enable_boost': '0',
                'enable_front_active': '1'
            },
            'Delay_Settings': {
                'click_delay': '1',
                'change_window_delay': '2',
                'skip_delay': '0.1',
                'reboot_delay': '20'
            },
            'Statistics': {
                role: 0 for role in ConfigManager.DEFAULT_ALONE_MODE_ROLE_ENABLE.keys()
            }
        }
        self.default_settings['Statistics'].update({'재기동': 0, '메롱': 0})

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
