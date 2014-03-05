# Pyglyvim
# MIT License
# See https://github.com/bgrohman/pyglyvim
import sys
import vim

# Misc
def cd(directory):
	vim.command("cd {0}".format(directory))

def get_current_directory():
	return vim.eval("getcwd()")

def get_variable(name):
	return vim.eval(name)

# Commands
commands = {}
def define_command(command_name, fn):
	commands[command_name] = fn
	vim.command("command! {0} python pyglyvim_call_command('{0}')".format(command_name))

def call_command(command_name):
	commands[command_name]()

# Location list
def clear_location_list():
	vim.command("lexpr []")

def add_line_to_location_list(line_number, text="", type=""):
	vim.eval("setloclist(0, [{'bufnr': %s, 'lnum': %s, 'text': '%s', 'type': '%s'}], 'a')" % (vim.current.buffer.number, line_number, text, type))

def open_location_list():
	vim.command("lwindow")

def close_location_list():
	vim.command("lclose")

# Signs
def clear_signs():
	vim.command("sign unplace * file={0}".format(vim.current.buffer.name))

def define_sign(sign_name, text="*", text_highlight="Error"):
	vim.command("sign define {0} text={1} texthl={2}".format(sign_name, text, text_highlight))

def add_sign(sign_id, line_number, sign_name, file_path=None):
	if file_path is None:
		file_path = vim.current.buffer.name
	vim.command('sign place {0} line={1} name={2} file={3}'.format(sign_id, line_number, sign_name, file_path))

# handle vim commands defined via pyglyvim
vim.command("python from pyglyvim import call_command as pyglyvim_call_command")
