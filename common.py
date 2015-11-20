import sublime, sublime_plugin
import os, sys
import json

# z_os_ftp is the folder in our plugin
sys.path.append(os.path.dirname(__file__))

from z_os_ftp import z_OS_FTP_Client


class New_fileCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.insert(edit, 0, ''.join(text))

class Settings():
    def __init__(self):
        if os.path.isfile(__filename__):
            file = open(__filename__,'r')
            self.__dict__ = json.loads(file.read())               


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

__filename__ = os.path.join(__location__, 'settings.json')

