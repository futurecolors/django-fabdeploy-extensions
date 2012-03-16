# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib import files
from fab_deploy import utils
from fab_deploy import system


__all__ = [
    'celery_setup', 'celery_start', 'celery_restart', 'celery_reload', 'celery_stop',
    'celerybeat_setup', 'celerybeat_start', 'celerybeat_restart', 'celerybeat_reload', 'celerybeat_stop',
]


@utils.run_as_sudo
def celery_setup():
    """ Setups Celery. """
    sudo('adduser --system --no-create-home --disabled-login --disabled-password --group celery')

    utils.upload_config_template('celeryd.sh', '/etc/init.d/celeryd', use_sudo=True)
    utils.upload_config_template('celeryd.conf', '/etc/default/celeryd', use_sudo=True)

    sudo('mkdir -p /var/log/celery')
    sudo('chmod 777 /var/log/celery')

    sudo('chmod +x /etc/init.d/celeryd')
    sudo('update-rc.d celeryd defaults')
    celery_start()


@utils.run_as_sudo
def celery_start():
    ''' Start Celery '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celeryd start')

@utils.run_as_sudo
def celery_stop():
    ''' Stop Celery '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celeryd stop')

@utils.run_as_sudo
def celery_restart():
    ''' Restart Celery '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celeryd restart')

@utils.run_as_sudo
def celery_reload():
    ''' Reload Celery '''
    sudo('/etc/init.d/celeryd reload')


@utils.run_as_sudo
def celerybeat_setup():
    """ Setups Celerybeat. """

    utils.upload_config_template('celerybeat.sh', '/etc/init.d/celerybeat', use_sudo=True)

    if not files.exists('/etc/init.d/celeryd'):
        print "You must setup “celeryd” before “celerybeat”!!!"
        return

    sudo('chmod +x /etc/init.d/celerybeat')
    sudo('update-rc.d celerybeat defaults')
    celerybeat_start()


@utils.run_as_sudo
def celerybeat_start():
    ''' Start Celerybeat '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celerybeat start')


@utils.run_as_sudo
def celerybeat_stop():
    ''' Stop Celerybeat '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celerybeat stop')


@utils.run_as_sudo
def celerybeat_restart():
    ''' Restart Celerybeat '''
    with settings(warn_only=True):
        sudo('/etc/init.d/celerybeat restart')


@utils.run_as_sudo
def celerybeat_reload():
    ''' Reload Celerybeat '''
    sudo('/etc/init.d/celerybeat reload')