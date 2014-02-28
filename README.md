pyglyvim
========

Helper functions for writing Vim plugins with Python

## Functions

### cd(directory)
Changes current directory

### clear_location_list()
Clears the location list

### add_line_to_location_list(line_number)
Adds a line to the location list by line number

### open_location_list()
Opens the location list

### clear_signs()
Clears all signs in the current window

### define_sign(sign_name, text, text_highlight)
Defines a sign

### add_sign(sign_id, line_number, sign_name, file_path)
Adds a sign at the given line for the given sign name. file_path defaults to the path of the current buffer.
