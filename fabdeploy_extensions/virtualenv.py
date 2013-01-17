# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import run, env, cd
from fab_deploy import utils
from fabdeploy_extensions.extensions.nginx import nginx_restart

def virtualenv_create():
    run('mkdir -p envs')
    run('mkdir -p src')
    with cd('envs'):
        run('virtualenv --no-site-packages %s' % env.conf['INSTANCE_NAME'])

        # installing latest pip
        run('git clone https://github.com/pypa/pip.git')
        with cd('pip'):
            run('python setup.py install')


@utils.inside_src
def pip_update(what=None, options='', restart=True):
    """ Updates pip without reinstalling everything! """
    what = utils._pip_req_path(what or env.conf.PIP_REQUIREMENTS_ACTIVE)
    run('pip install %s -r %s --exists-action s' % (options, what))