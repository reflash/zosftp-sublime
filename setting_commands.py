from common import *
import common


class Set_settingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.settings = Settings()
        self.window.show_input_panel("Enter your login",
                "", self.on_login_input, None, None)

    def on_login_input(self, user_input):
        if user_input != '':
            self.settings.login = user_input
            self.window.show_input_panel("Enter your password",
                "", self.on_password_input, None, None)
        else:
            sublime.error_message("Empty login")

    def on_password_input(self, user_input):
        if user_input != '':
            self.settings.password = user_input
            self.window.show_input_panel("Enter your host",
                "", self.on_host_input, None, None)
        else:
            sublime.error_message("Empty password")

    def on_host_input(self, user_input):
        if user_input != '':
            print(common.__filename__)
            self.settings.host = user_input
            with open(common.__filename__, 'w') as outfile:
                json.dump(self.settings.__dict__, outfile)
            print("Settings saved")
        else:
            sublime.error_message("Empty host address")

class Change_settingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.open_file(common.__filename__)
