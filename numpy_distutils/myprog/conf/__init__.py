#!/usr/bin/env python

# Imports ---------------------------------------------------------------------
import imp
import sys
import re
import os
import string

# Define get_config -----------------------------------------------------------

def get_config(name = None):
    rf = ['config_default']
    if (name == None):
        name = re.sub('[\.-]','_',os.uname()[1])
    vname = 'config.config_' + name.split('_')[-1]
    sys.path+=['./conf']
    try:
        m = __import__(vname)
        print 'DynHoLab configuration: %s'%name.split('_')[0]
        rf += [vname]
    except ImportError:
        m = __import__('config_default')
        print 'DynHoLab configuration: default'
    return (m,rf)

###############################################################################
# End of file DynKernel/config/__init__.py
