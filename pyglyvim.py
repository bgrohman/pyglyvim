# Pyglyvim
# MIT License
# See https://github.com/bgrohman/pyglyvim

import vim

# Misc
def cd(directory):
	vim.command("cd {0}".format(directory))

# Location list
def clear_location_list():
	vim.command("lexpr []")

def add_line_to_location_list(line_number):
	vim.command('laddexpr expand("%:.") . ":" . {0} . ":" . getline({0})'.format(line_number))

def open_location_list():
	vim.command("lwindow")

# Signs
def clear_signs():
	vim.command("sign unplace * file={0}".format(vim.current.buffer.name))

def define_sign(sign_name, text="*", text_highlight="Error"):
	vim.command("sign define {0} text={1} texthl={2}".format(sign_name, text, text_highlight))

def add_sign(sign_id, line_number, sign_name, file_path=vim.current.buffer.name):
	vim.command('sign place {0} line={1} name={2} file={3}'.format(sign_id, line_number, sign_name, file_path))
