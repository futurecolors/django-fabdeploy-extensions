# -*- coding: utf-8 -*-
from fab_deploy import utils
from fabric.contrib.files import append
import crypt


@utils.run_as_sudo
def create_htpasswd(username, password, file=None):
    """ Make htpasswd file """
    htpasswd_line = '{0}:{1}'.format(username, crypt.crypt(password, password))
    htpasswd_file = file or '/etc/nginx/htpasswd'
    append(htpasswd_file, htpasswd_line, use_sudo=True)