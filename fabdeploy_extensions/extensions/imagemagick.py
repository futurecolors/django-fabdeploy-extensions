# -*- coding: utf-8 -*-
from fab_deploy import utils
from fab_deploy import system

@utils.run_as_sudo
def imagemagick_install():
    """ Installs Image Magick """
    os = utils.detect_os()
    options = {'squeeze': '-t squeeze-backports'}
    system.aptitude_install('imagemagick', options.get(os, ''))