# pyglyvim

Helper functions for writing Vim plugins with Python

## Highlights
* Define vim commands as python functions
* Manipulate the location list
* Add/remove signs

## Usage
1. Place the pyglyvim.py file in your plugin directory.
2. Load your python module in your plugin's .vim file.
  * See the [example plugin](./pyglyvimExample/plugin/pyglyvimExample.vim) for details.
3. From your python code, `import pyglyvim`.

See [vim documentation](http://vimdoc.sourceforge.net/htmldoc/if_pyth.html) for details on vim's built-in python interface.

## Example Plugin
Take a look at the [example plugin](./pyglyvimExample/).

## Functions

### cd(directory)
Changes current directory

### get_current_directory()
Returns the current working directory

### get_variable(name)
Returns the value of the given vim variable

### define_command(command_name, fn)
Defines a vim command with the given name that calls a Python function

### clear_location_list()
Clears the location list

### add_line_to_location_list(line_number, text, type)
Adds a line to the location list by line number

### open_location_list()
Opens the location list

### clear_signs()
Clears all signs in the current window

### define_sign(sign_name, text, text_highlight)
Defines a sign

### add_sign(sign_id, line_number, sign_name, file_path)
Adds a sign at the given line for the given sign name. file_path defaults to the path of the current buffer.
