from common import *
import common

class Open_datasetCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = Settings()
        self.ftp_client = z_OS_FTP_Client(settings)

        self.window.show_input_panel("Name of loaded dataset", 
            "*.*", self.on_input, None, None)     


    def on_input(self, user_input):
        if user_input != '':
            result = self.ftp_client.open_dataset(user_input)
            self.display(result)
            print("Dataset " + user_input + "opened")
        else:
            sublime.error_message("Empty dataset name") 

    def display(self,text):
        view = self.window.new_file()
        view.run_command("new_zos_file",{ "text" : text});

class Save_datasetCommand(sublime_plugin.TextCommand):

    def run(self,edit):
        settings = Settings()
        self.window = sublime.active_window()
        self.ftp_client = z_OS_FTP_Client(settings)

        self.window.show_input_panel("Name of saved dataset", 
            "*.*", self.on_input, None, None)      

    def on_input(self, user_input):
        active_file_name = self.view.file_name()

        if active_file_name is None:
            sublime.error_message("Save file before submitting")
            return

        file_path = os.path.join(common.__location__,active_file_name)

        if user_input != '':
            self.ftp_client.save_dataset(file_path,user_input)
            print("Dataset " + user_input + "saved")
        else:
            sublime.error_message("Empty dataset name")

    def display(self,text):
        view = self.window.new_file()
        view.run_command("new_zos_file",{ "text" : text});