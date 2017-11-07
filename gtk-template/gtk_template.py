import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import multiprocessing as mp #For things branching of from the main loop


class myWindow(Gtk.Window):

	def __init__(self):
		#Make window
		Gtk.Window.__init__(self, title="Template for gtk")
		self.set_border_width(10)
		#Make a vbox for elements
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)
		
		#Progress bar - Example element
		self.progressbar = Gtk.ProgressBar()
		vbox.pack_start(self.progressbar, True, True, 0)
		
		self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
		self.activity_mode = True #make progress bar pulse
		
		#config
		self.progressbar.set_pulse_step(0.03) # step for progress bar
		self.set_default_size(800, 600)
		
	def on_timeout(self, user_data):
		if self.activity_mode:
			self.progressbar.pulse()
		#Keep the main loop action quick - If doing a long running task, use seperate process with mp
		#Return true for no error
		return True

win = myWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
