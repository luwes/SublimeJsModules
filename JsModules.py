import os
import sublime
import sublime_plugin

class JsModulesFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    active_file = self.view.file_name()
    shell_cmd = "cjs-to-es6 {0}".format(active_file)
    self.view.window().run_command('exec', {
      'shell_cmd': shell_cmd
    })

class JsModulesDirCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    active_dir = os.path.dirname(self.view.file_name())
    shell_cmd = "cjs-to-es6 {0}".format(active_dir)
    self.view.window().run_command('exec', {
      'shell_cmd': shell_cmd
    })
