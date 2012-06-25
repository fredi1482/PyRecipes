#!/usr/bin/env python

# -----------------------------------------------------------------------------
#                                 General
# -----------------------------------------------------------------------------

verbose       = 'info'
log_file_name = "dyn.log"
log_to_file   = True
log_to_stdout = True
print_tree    = True

# -----------------------------------------------------------------------------
#                        Compilation and installation
# -----------------------------------------------------------------------------

tools         = ['DynTecplot']
pluggins      = []

nb_proc      = 1
compiler     = 'gcc'
fcompiler    = 'gfortran'

###############################################################################
# End of file DynKernel/config/config_default.py
