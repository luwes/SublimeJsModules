import os
import sublime
import sublime_plugin

class JsModulesFileCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    active_view = window.active_view()
    if active_view:
      active_file_name = active_view.file_name()
      shell_cmd = "cjs-to-es6 {0}".format(active_file_name)
      window.run_command('exec', {
        'shell_cmd': shell_cmd
      })

class JsModulesDirCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    active_view = window.active_view()
    if active_view:
      active_dir = os.path.dirname(active_view.file_name())
      shell_cmd = "cjs-to-es6 {0}".format(active_dir)
      window.run_command('exec', {
        'shell_cmd': shell_cmd
      })
