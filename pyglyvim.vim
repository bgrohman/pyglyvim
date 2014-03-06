" Pyglyvim
" MIT License
" See https://github.com/bgrohman/pyglyvim
" See http://vimdoc.sourceforge.net/htmldoc/if_pyth.html for details on vim's python interface
if !has('python')
	finish
endif

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

python << EndPython
import vim
import sys

plugin_path = vim.eval("s:plugin_path")
sys.path.append(plugin_path)

import pyglyvim
EndPython
