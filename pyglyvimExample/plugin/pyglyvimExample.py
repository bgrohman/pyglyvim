import vim
import pyglyvim

def pyglyvim_example_command():
	print "This is an example plugin!"
	print "This command 1) adds a sign to the first and last lines, and 2) adds the first and last lines to the location list."

	last_line = len(vim.current.buffer)
	pyglyvim.clear_signs()
	pyglyvim.add_sign(1, 1, "pyglyvim_example_sign", file_path=vim.current.buffer.name)
	pyglyvim.add_sign(2, last_line, "pyglyvim_example_sign")

	pyglyvim.clear_location_list()
	pyglyvim.add_line_to_location_list(1, text="Pyglyvim added this line", type="W")
	pyglyvim.add_line_to_location_list(last_line, text="Pyglyvim added this line, too")
	pyglyvim.open_location_list()

pyglyvim.define_sign("pyglyvim_example_sign", text="PV", text_highlight="Error")
pyglyvim.define_command("PyglyvimExample", pyglyvim_example_command)
