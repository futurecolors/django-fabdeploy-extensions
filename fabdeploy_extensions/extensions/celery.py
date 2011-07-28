# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib import files
from fab_deploy import utils
from fab_deploy import system


__all__ = ['celery_setup', 'celery_start', 'celery_restart', 'celery_reload']


@utils.run_as_sudo
def celery_setup():
    """ Setups uWSGI. """
    sudo('adduser --system --no-create-home --disabled-login --disabled-password --group celery')

    utils.upload_config_template('celeryd.sh', '/etc/init.d/celeryd', use_sudo=True)
    sudo('chmod +x /etc/init.d/celeryd')
    sudo('update-rc.d celeryd defaults')
    celery_start()


@utils.run_as_sudo
def celery_start():
    ''' Start uWSGI '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celeryd start')


@utils.run_as_sudo
def celery_restart():
    ''' Restart uWSGI '''
    sudo('/etc/init.d/celeryd restart')


@utils.run_as_sudo
def celery_reload():
    ''' Start uWSGI '''
    sudo('/etc/init.d/celeryd reload')