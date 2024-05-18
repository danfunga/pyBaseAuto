import tkinter as tk
from src.config_manager import ConfigManager
from src.base_auto import BaseAuto
import subprocess


class BaseAutoGui:
    def __init__(self, root):
        self.root = root
        self.root.title("BaseAuto GUI")

        self.config_manager = ConfigManager()

        # Load GUI position from config
        gui_config = self.config_manager.get_section('Gui_Config')
        self.root.geometry(f"+{gui_config.get('pos_x', '100')}+{gui_config.get('pos_y', '100')}")

        # Frame for Title, Role, Type
        info_frame = tk.Frame(root, relief=tk.SOLID, bd=2)
        info_frame.pack()

        # Setting Title
        setting_title_label = tk.Label(info_frame, text="Setting")
        setting_title_label.pack()

        # App Title
        app_title_label = tk.Label(info_frame, text="Title:")
        app_title_label.pack(side=tk.LEFT)
        self.app_title_var = tk.StringVar()
        self.app_title_var.set(self.config_manager.get('Settings', 'app_title', fallback='N/A'))
        self.app_title_entry = tk.Entry(info_frame, textvariable=self.app_title_var, width=8)
        self.app_title_entry.pack(side=tk.LEFT)
        self.app_title_entry.configure(relief=tk.SOLID, bd=2)

        # Play Role
        play_role_label = tk.Label(info_frame, text="Role:")
        play_role_label.pack(side=tk.LEFT)
        self.play_role_var = tk.StringVar()
        self.play_role_var.set(self.config_manager.get('Settings', 'play_role', fallback='N/A'))
        self.play_role_options = ['단독', '리그', '랭대', '홈런', '히스', '스테', '친구', '타홀', '실대', '보상', '등반']
        # self.play_role_options = ['단독', '리그', '랭대', '홈런', '히스', '스테', '친구', '타홀', '실대', '클협', '보상']
        self.play_role_menu = tk.OptionMenu(info_frame, self.play_role_var, *self.play_role_options)
        self.play_role_menu.pack(side=tk.LEFT, padx=5, pady=5)
        self.play_role_menu.configure(relief=tk.SOLID, bd=2)

        # Game Type
        game_type_label = tk.Label(info_frame, text="Type:")
        game_type_label.pack(side=tk.LEFT)
        self.game_type_var = tk.StringVar()
        self.game_type_var.set(self.config_manager.get('Settings', 'game_type', fallback='전체'))
        self.game_type_options = ['전체', '공격', '수비']
        self.game_type_menu = tk.OptionMenu(info_frame, self.game_type_var, *self.game_type_options)
        self.game_type_menu.pack(side=tk.LEFT, padx=5, pady=5)
        self.game_type_menu.configure(relief=tk.SOLID, bd=2)

        # Standalone Mode Roles
        standalone_label = tk.Label(root, text="Standalone Mode Roles:")
        standalone_label.pack()

        # Checkboxes for each role
        standalone_mode_roles = self.config_manager.get_section('StandaloneMode_Roles')
        self.standalone_var = {}

        checkboxes_frame = tk.Frame(root, relief=tk.SOLID, bd=2)
        checkboxes_frame.pack()
        count = 0
        for role, value in standalone_mode_roles.items():
            var = tk.IntVar(value=int(value))
            self.standalone_var[role] = var
            checkbox = tk.Checkbutton(checkboxes_frame, text=role, variable=var)
            checkbox.grid(row=count // 5, column=count % 5, sticky="w")
            count += 1

        # Adjust the width of info_frame to match checkboxes_frame
        info_frame.config(width=checkboxes_frame.winfo_reqwidth())

        # Adjust the height of checkboxes_frame to match info_frame
        checkboxes_frame.config(height=info_frame.winfo_reqheight())

        # Save Button
        save_button = tk.Button(root, text="Save", command=self.save_config)
        save_button.pack(side=tk.RIGHT)

        # Start Button
        start_button = tk.Button(root, text="Start", command=self.start_base_auto)
        start_button.pack(side=tk.RIGHT)

        # Reload Button
        reload_button = tk.Button(root, text="Reload", command=self.reload_script)
        reload_button.pack(side=tk.RIGHT)

    def save_config(self):
        # Save the edited values to the config file
        self.config_manager.set('Settings', 'app_title', self.app_title_var.get())
        self.config_manager.set('Settings', 'play_role', self.play_role_var.get())
        self.config_manager.set('Settings', 'game_type', self.game_type_var.get())
        for role, var in self.standalone_var.items():
            self.config_manager.set('StandaloneMode_Roles', role, str(var.get()))

        # Save GUI position to config
        pos_x = self.root.winfo_x()
        pos_y = self.root.winfo_y()
        self.config_manager.set('Gui_Config', 'pos_x', str(pos_x))
        self.config_manager.set('Gui_Config', 'pos_y', str(pos_y))
        print("설정을 저장 하였습니다.")

    def start_base_auto(self):
        base_auto = BaseAuto()
        base_auto.start()

    def reload_script(self):
        # Reload the script by importing it again
        # Save GUI position to config
        pos_x = self.root.winfo_x()
        pos_y = self.root.winfo_y()
        self.config_manager.set('Gui_Config', 'pos_x', str(pos_x))
        self.config_manager.set('Gui_Config', 'pos_y', str(pos_y))

        self.root.destroy()

        subprocess.run(["python", "main.py"])
