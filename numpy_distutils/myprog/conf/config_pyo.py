#!/usr/bin/env python

# -----------------------------------------------------------------------------
#                                 General
# -----------------------------------------------------------------------------

exec_file    = 'dyn.py'
package_name = 'DynKernel'
subpackages  = ['borders', 'geom', 'lhs', 'phys', 'turb', 'rhs', 'io',
                'tmo', 'utilities']

description  = "Kernel for dyn : DynFluid CFD code."
version      = "11.10.06"
author       = "P-Y. Outtier, C. Content"
author_email = "pierre-yves.outtier@ensam.eu ; cedric.content@ensam.eu"

# -----------------------------------------------------------------------------
#                              Dependencies
# -----------------------------------------------------------------------------

needed_packages = ['DynTecplot']

# -----------------------------------------------------------------------------
#                              Compilation
# -----------------------------------------------------------------------------

nb_proc      = 3
compiler     = 'gcc'
fcompiler    = 'gfortran'

###############################################################################
# End of file DynKernel/config/config_default.py
