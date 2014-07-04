from gi.repository import Gtk
import subprocess
import os
import sys

class Handler:
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	def onClickBtn1(self, button):
		euid = os.geteuid()
		if euid != 0:
			print("Script not started as root. Running sudo..")
			args = ['sudo', sys.executable] + sys.argv + [os.environ]
			# the next line replaces the currently-running process with the sudo
			os.execlpe('sudo', *args)

		print('Running. Your euid is', euid)
		'''bashCommand = "apt-get install mypaint"
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print(output)'''
		
	def onClickBtn2(self, button):
		print("Aprete boton 2")
        


builder = Gtk.Builder()
builder.add_from_file("Gestor.glade")
builder.connect_signals(Handler())

window = builder.get_object("VentanaP")
window.show_all()

Gtk.main()
