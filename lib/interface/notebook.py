from gi.repository import Gtk, Gio
from ..util.util import Util

class Notebook :

  def __init__(self, window):
    notebook = Gtk.Notebook()

    app_config = Util.load_application_configuration()
    tabs = app_config['tabs']

    for tab in tabs:
      self.render_tab(notebook, tab)

    window.add(notebook)

  def render_tab(self, notebook, tab_object):
    pageTitle = Gtk.HBox()
    pageTitle.pack_start(Gtk.Image.new_from_icon_name(tab_object['icon'], Gtk.IconSize.MENU
    ), True, True, 0)
    pageTitle.pack_start(Gtk.Label(tab_object['name']), True, True, 10)
    pageTitle.show_all()

    pageContent = Gtk.Box()
    pageContent.pack_start(Gtk.Label(tab_object['name']), True, True, 0)

    notebook.append_page(pageContent, pageTitle)
