from gi.repository import Gtk, Gio
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import util
class Notebook :

  def __init__(self, window):
    notebook = Gtk.Notebook()
    print(util)
    application_configurations = util.load_json('application.json')
    tabs = application_configurations['tabs']

    for tab in tabs:
      self.render_tab(notebook, tab)

    window.add(notebook)

  def render_tab(self, notebook, tab_object):

    # Tab Title
    pageTitle = Gtk.HBox()
    pageTitle.pack_start(Gtk.Image.new_from_icon_name(
      tab_object['icon'],
      Gtk.IconSize.MENU
    ), True, True, 0)
    pageTitle.pack_start(Gtk.Label(tab_object['name']), True, True, 10)
    pageTitle.show_all()

    """
      Tab content
    """
    pageContent = Gtk.Box()
    pageContent.pack_start(Gtk.Label(tab_object['name']), True, True, 0)

    notebook.append_page(pageContent, pageTitle)
