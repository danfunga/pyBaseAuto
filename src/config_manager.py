import configparser
import os

class ConfigManager:
    def __init__(self, config_file='config/config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.default_settings = {
            'Settings': {
                'window_title': 'main'
            }
        }
        
        # Ensure the config directory exists
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        # If the config file does not exist, create it with default settings
        if not os.path.exists(self.config_file):
            self.create_default_config()
        
        self.config.read(self.config_file)
    
    def create_default_config(self):
        for section, options in self.default_settings.items():
            self.config[section] = options
        with open(self.config_file, 'w') as configfile:
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
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
    
    def get_section(self, section):
        if not self.config.has_section(section):
            raise configparser.NoSectionError(section)
        return dict(self.config.items(section))
    
    def add_section(self, section):
        if not self.config.has_section(section):
            self.config.add_section(section)
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
    
    def remove_section(self, section):
        if self.config.has_section(section):
            self.config.remove_section(section)
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
    
    def remove_option(self, section, option):
        if self.config.has_section(section) and self.config.has_option(section, option):
            self.config.remove_option(section, option)
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)