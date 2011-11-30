# -*- coding: utf-8 -*-
from fabric.api import run, sudo, env
from fab_deploy import utils
from fab_deploy.system import aptitude_install


__all__ = ['sphinx_install', 'sphinx_setup', 'sphinx_indexer', 'sphinx_start']

def get_sphinx_config():
    id = env.conf['NAME']
    settings_file = '_settings/applications/sphinx/sphinx_{0}.conf'.format(id)

    return settings_file


@utils.run_as_sudo
def sphinx_install():
    """ Install sphinx search """
    aptitude_install('sphinxsearch')
    sudo('sed -i "s/START=no/START=yes/g" /etc/default/sphinxsearch')


@utils.inside_project
def sphinx_setup(apps='--all'):
    """ Sphinx setup """
    sudo('DJANGO_SETTINGS_ENVIRONMENT={0} python manage.py generate_sphinx_config {1} > {2}'.format(env.conf['NAME'], apps, get_sphinx_config()))

    make_log_files()
    sphinx_indexer()
    sphinx_start()


@utils.run_as_sudo
def make_log_files():
    """ Generate sphinx config from django """
    sphinx_config = run('cat {0}'.format(get_sphinx_config()))
    for line in sphinx_config.splitlines():
        option = line.replace(' ', '').split('=')
        if len(option) == 2 and option[1].endswith('.log'):
            sudo('touch {0}'.format(option[1]))


@utils.inside_project
@utils.run_as_sudo
def sphinx_indexer():
    """ Setup sphinx indexing """
    indexer_command = 'indexer --config {0} --all --rotate'.format(get_sphinx_config())
    sudo(indexer_command)
    # Has to reindex with Celery
    # crontab_update('0-59 * * * * {0}'.format(indexer_command), 'indexer')


@utils.inside_project
@utils.run_as_sudo
def sphinx_start():
    """ Run searchd daemon """
    sudo('/usr/bin/searchd --config {0}'.format(get_sphinx_config()))


@utils.inside_project
@utils.run_as_sudo
def sphinx_stop():
    """ Stop searchd daemon """
    sudo('/usr/bin/searchd --config {0} --stop'.format(get_sphinx_config()))
