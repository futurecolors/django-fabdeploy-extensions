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

    utils.upload_config_template('celeryd.sh', '/etc/init.d/celeryd_%s' % env.conf['INSTANCE_NAME'], use_sudo=True)
    utils.upload_config_template('celeryd.conf', '/etc/default/celeryd_%s' % env.conf['INSTANCE_NAME'], use_sudo=True)

    sudo('mkdir -p /var/log/celery')
    sudo('chmod 777 /var/log/celery')

    sudo('chmod +x /etc/init.d/celeryd_%s' % env.conf['INSTANCE_NAME'])
    sudo('update-rc.d celeryd_%s defaults' % env.conf['INSTANCE_NAME'])
    celery_start()


@utils.run_as_sudo
def celery_start():
    ''' Start Celery '''
    sudo('/etc/init.d/celeryd_%s start' % env.conf['INSTANCE_NAME'])

@utils.run_as_sudo
def celery_stop():
    ''' Stop Celery '''
    sudo('/etc/init.d/celeryd_%s stop' % env.conf['INSTANCE_NAME'])

@utils.run_as_sudo
def celery_restart():
    ''' Restart Celery '''
    sudo('/etc/init.d/celeryd_%s restart' % env.conf['INSTANCE_NAME'])

@utils.run_as_sudo
def celery_reload():
    ''' Reload Celery '''
    sudo('/etc/init.d/celeryd_%s reload' % env.conf['INSTANCE_NAME'])


@utils.run_as_sudo
def celerybeat_setup():
    """ Setups Celerybeat. """

    utils.upload_config_template('celerybeat.sh', '/etc/init.d/celerybeat_%s' % env.conf['INSTANCE_NAME'], use_sudo=True)

    if not files.exists('/etc/init.d/celeryd_%s' % env.conf['INSTANCE_NAME']):
        print "You must setup “celeryd” before “celerybeat”!!!"
        return

    sudo('chmod +x /etc/init.d/celerybeat_%s' % env.conf['INSTANCE_NAME'])
    sudo('update-rc.d celerybeat_%s defaults' % env.conf['INSTANCE_NAME'])
    celerybeat_start()


@utils.run_as_sudo
def celerybeat_start():
    ''' Start Celerybeat '''
    sudo('/etc/init.d/celerybeat_%s start' % env.conf['INSTANCE_NAME'])


@utils.run_as_sudo
def celerybeat_stop():
    ''' Stop Celerybeat '''
    sudo('/etc/init.d/celerybeat_%s stop' % env.conf['INSTANCE_NAME'])


@utils.run_as_sudo
def celerybeat_restart():
    ''' Restart Celerybeat '''
    sudo('/etc/init.d/celerybeat_%s restart' % env.conf['INSTANCE_NAME'])


@utils.run_as_sudo
def celerybeat_reload():
    ''' Reload Celerybeat '''
    sudo('/etc/init.d/celerybeat_%s reload' % env.conf['INSTANCE_NAME'])
