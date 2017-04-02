from gi.repository import Gtk, Gio

class Repositories:
  def __init__(self, window):
    self.grid = Gtk.Grid()
    self.grid.set_column_homogeneous(True)
    self.grid.set_row_homogeneous(True)
    self.add(self.grid)
