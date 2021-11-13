# Load Gtk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

def list_item_setup(factory, list_item):
    list_item.set_child(Gtk.Label())

def list_item_bind(factory, list_item):
    label = list_item.get_child()
    label.set_label(list_item.get_item().get_string())

# Whien the application is launched…
def on_activate(app):
    # … create a new window…
    win = Gtk.ApplicationWindow(application=app)
   
    list_item_factory = Gtk.SignalListItemFactory()
    list_item_factory.connect("setup", list_item_setup)
    list_item_factory.connect("bind", list_item_bind)

    model = Gio.ListStore()
    for i in range(1000):
        model.append(Gtk.StringObject.new("{}".format(i)))

    list_view = Gtk.ListView(
        model=Gtk.NoSelection(model=model),
        factory=list_item_factory,
    )

    scrolled_win = Gtk.ScrolledWindow()
    scrolled_win.set_child(list_view)
    scrolled_win.set_min_content_height(200)

    win.set_child(scrolled_win)
    win.present()

# Create a new application
app = Gtk.Application(application_id='com.example.GtkApplication')
app.connect('activate', on_activate)

# Run the application
app.run(None)

