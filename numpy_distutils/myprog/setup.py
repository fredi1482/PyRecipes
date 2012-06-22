#!/usr/bin/env python
#
###############################################################################
#                    THIS IS THE ONLY PART TO CHANGE                          #
###############################################################################
#
config_file = 'config_default'
#
###############################################################################
#                         END OF PART TO CHANGE                               #
###############################################################################
#
#
import sys
import os.path
import re


#===============================================================================
# Install path
#===============================================================================
def install_path():
    '''
    Return install path.
    '''
    if is_local_installation():
        temp = local_prefix()
    else:
        temp = sys.prefix
    return temp

#===============================================================================
# Local prefix
#===============================================================================
def local_prefix():
    '''
    Return local prefix.
    '''
    for term in sys.argv:
        if re.compile('--prefix=').search(term) != None:
            temp = term[9:]
    return temp

#===============================================================================
# Lib suffix
#===============================================================================
def lib_suffix():
    '''
    Return the lib suffix.
    
    import distutils.sysconfig
    distutils.sysconfig.get_python_lib()
    '''
    return "lib/python%s.%s/site-packages" % (sys.version_info[0], 
                                                      sys.version_info[1])

#===============================================================================
# Lib install path
#===============================================================================
def lib_install_path():
    '''
    Return install path.
    '''
    if is_local_installation():
        temp = local_prefix()
    else:
        temp = sys.prefix
    return os.path.join(temp, lib_suffix())


#===============================================================================
# Is a local installation
#===============================================================================
def is_local_installation():
    '''
    Say if it is a local installation or not.
    '''
    local_inst = False
    for term in sys.argv:
        if re.compile('--prefix=').search(term) != None:
            local_inst = True
    return local_inst


#===============================================================================
# Create symbolic link in bin
#===============================================================================
def symbolic_link_in_bin(package_name, exec_file):
    '''
    Create symbolic link.
    '''
    if is_local_installation():
        exec_path = os.path.join(lib_install_path(),
                                     package_name ,exec_file)
        exec_path = os.path.abspath(exec_path)
        os.chmod(exec_path, 0755)
        link_path = os.path.join(install_path(), 'bin',
                                 os.path.splitext(exec_file)[0])
        link_path = os.path.abspath(link_path)
        if not os.path.exists(os.path.join(install_path(), 'bin')):
            os.mkdir(os.path.join(install_path(), 'bin'))
        if os.path.exists(os.path.join(install_path(), 'bin',
                          os.path.splitext(exec_file)[0])):
            pass
            #print "Already exist !"
            #print "For informtion :"
            #print "  " + link_path + " --> " + exec_path
        else:
            os.symlink(exec_path, link_path)
            #print link_path + " --> " + exec_path




#
# Imports ---------------------------------------------------------------------
import os

# Get configuration from config file ------------------------------------------
import conf
m, rf = conf.get_config(config_file)

# Test installation of requires modules ---------------------------------------

# Execute scons to compile Fortran librairies ---------------------------------

# Define configuration --------------------------------------------------------

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)
    config.add_subpackage('myprog')
    return config


# Define setup ----------------------------------------------------------------

def setup_package():
    from numpy.distutils.core import setup
    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    src_path = local_path
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)
    
    try:
        setup(name = 'myprog',
              configuration = configuration,
              description = 'my prog is rubbish',
              version = '1.0.0',
              author = 'P.-Y. Outtier',
              author_email = 'pierre-yves.outtier@ensam.eu'
             )
    except StandardError as e:
        print 'Error of compilation and installation:'
        print e
    finally:
        del sys.path[0]
        os.chdir(old_path)
        return

if __name__ == '__main__':
    setup_package()
    symbolic_link_in_bin('myprog', 'the_main_of_myprog.py')


###############################################################################
# End of file setup.py
