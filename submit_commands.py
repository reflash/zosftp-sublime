from common import *
import common


def display(text):
    window = sublime.active_window()
    view = window.new_file()
    view.run_command("new_zos_file",{ "text" : text});


class Submit_job_and_waitCommand(sublime_plugin.TextCommand):
    
    def run(self,edit):
        settings = Settings()
        ftp_client = z_OS_FTP_Client(settings)

        active_file_name = self.view.file_name()

        if active_file_name is None:
            sublime.error_message("Save file before submitting") 
            return

        file_path = os.path.join(common.__location__,active_file_name)

        result = ftp_client.submit_job_and_wait(file_path)

        display(result)

        print("Job submitted")



class Submit_jobCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = Settings()
        ftp_client = z_OS_FTP_Client(settings)
        view = self.window.active_view()

        active_file_name = view.file_name()

        if active_file_name is None:
            sublime.error_message("Save file before submitting")
            return

        file_path = os.path.join(common.__location__,active_file_name)

        result = ftp_client.submit_job(file_path)

        print("Job submitted")



class Submit_job_with_host_and_waitCommand(sublime_plugin.TextCommand):
    
    def run(self,edit):
        window = sublime.active_window()

        self.active_file_name = self.view.file_name()

        if self.active_file_name is None:
            sublime.error_message("Save file before submitting") 
            return

        window.show_input_panel("Enter host name: ", 
            "*.*", self.on_input, None, None) 

    def on_input(self, user_input):
        if user_input != '':
            settings = Settings()
            settings.host = user_input

            file_path = os.path.join(common.__location__,self.active_file_name)

            ftp_client = z_OS_FTP_Client(settings)
            result = ftp_client.submit_job_and_wait(file_path)
            display(result)

            print("Job submitted")
        else:
            sublime.error_message("Empty host name") 



class Submit_job_with_hostCommand(sublime_plugin.WindowCommand):

    def run(self,edit):
        view = self.window.active_view()
        self.active_file_name = view.file_name()

        if self.active_file_name is None:
            sublime.error_message("Save file before submitting") 
            return

        self.window.show_input_panel("Enter host name: ", 
            "*.*", self.on_input, None, None) 

    def on_input(self, user_input):
        if user_input != '':
            settings = Settings()
            settings.host = user_input

            file_path = os.path.join(common.__location__,self.active_file_name)

            ftp_client = z_OS_FTP_Client(settings)
            result = ftp_client.submit_job(file_path)
            
            print("Job submitted")

        else:
            sublime.error_message("Empty host name") 

