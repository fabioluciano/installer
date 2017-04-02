import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
import sys
from lib.interface.header import Header
from lib.interface.notebook import Notebook
from lib.util.util import Util

class Window(Gtk.ApplicationWindow):
  def __init__(self, application):
    app_config = Util.load_application_configuration()
    Gtk.ApplicationWindow.__init__(self, title=app_config['name'], application=application)
    self.set_default_size(600, 600)

class Application(Gtk.Application):
  def __init__(self):
    Gtk.Application.__init__(self)

  def do_activate(self):
    window = Window(self)

    Header(window)
    Notebook(window)

    window.show_all()

  def do_startup(self):
    Gtk.Application.do_startup(self)


    quit_action = Gio.SimpleAction(name="quit")
    quit_action.connect("activate", self.quit_callback)
    self.add_action(quit_action)


  def quit_callback(self, action, parameter):
      print("You clicked \"Quit\"")
      self.quit()

x = Application()
exit_status = x.run(sys.argv)
sys.exit(exit_status)
