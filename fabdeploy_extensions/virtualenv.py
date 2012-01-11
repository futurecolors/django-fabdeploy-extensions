# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import run, env, cd

def virtualenv_create():
    run('mkdir -p envs')
    run('mkdir -p src')
    with cd('envs'):
        run('virtualenv --no-site-packages %s' % env.conf['INSTANCE_NAME'])

        # installing latest pip
        run('git clone https://github.com/pypa/pip.git')
        with cd('pip'):
            run('python setup.py install')