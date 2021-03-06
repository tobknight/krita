'''
This script is licensed CC 0 1.0, so that you can learn from it.

------ CC 0 1.0 ---------------

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

https://creativecommons.org/publicdomain/zero/1.0/legalcode
'''
from PyQt5.QtWidgets import QMessageBox
import krita
from tenscripts import uitenscripts
import importlib


class TenScriptsExtension(krita.Extension):

    def __init__(self, parent):
       super(TenScriptsExtension, self).__init__(parent)

       self.actions = []
       self.scripts = []

    def setup(self):
        self.readSettings()
        
    def createActions(self, window):
        action = window.createAction("ten_scripts", "Ten Scripts")
        action.setToolTip("Assign ten scripts to ten shortcuts.")
        action.triggered.connect(self.initialize)
        self.loadActions(window)

    def initialize(self):
        self.uitenscripts = uitenscripts.UITenScripts()
        self.uitenscripts.initialize(self)

    def readSettings(self):
        self.scripts = Application.readSetting("tenscripts", "scripts", "").split(',')

    def writeSettings(self):
        saved_scripts = self.uitenscripts.saved_scripts()

        for index, script in enumerate(saved_scripts):
            self.actions[index].script = script

        Application.writeSetting("tenscripts", "scripts", ','.join(map(str, saved_scripts)))

    def loadActions(self, window):
        for index, item in enumerate(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
            action = window.createAction("execute_script_" + item, "Execute Script " + item, "")
            action.script = None
            action.triggered.connect(self._executeScript)

            if index < len(self.scripts):
                action.script = self.scripts[index]

            self.actions.append(action)

    def _executeScript(self):
        script = self.sender().script
        if script:
            try:
                spec = importlib.util.spec_from_file_location("users_script", script)
                users_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(users_module)
                
                if hasattr(users_module, 'main') and callable(users_module.main):
                    users_module.main()

                self.showMessage('script {0} executed'.format(self.sender().script))
            except Exception as e:
                self.showMessage(str(e))
        else:
            self.showMessage("You didn't assign a script to that action")

    def showMessage(self, message):
        self.msgBox  = QMessageBox(Application.activeWindow().qwindow())
        self.msgBox.setText(message)
        self.msgBox.exec_()


Scripter.addExtension(TenScriptsExtension(Application))
