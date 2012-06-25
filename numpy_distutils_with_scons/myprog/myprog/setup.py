
def configuration(parent_package = '', top_path = None):
    from numpy.distutils.misc_util import Configuration
    loc_config = Configuration('myprog', parent_package, top_path)
    loc_config.add_subpackage('popo')
    loc_config.add_subpackage('toc')
    return loc_config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
#
###############################################################################
# End of file DynKernel/setup.py
