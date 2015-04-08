#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import sys
import subprocess
import shlex
from git import Repo


def main():
    if not os.path.exists('./.git'):
        sys.stderr.write("not a git repository root dir...\n")
        exit(1)
    repo = Repo('.')
    conf = repo.config_reader()
    remote_url = conf.get_value('remote "origin"', 'url')
    uri = None
    if 'git@github.com:' in remote_url[:15]:
        uri = "https://github.com/{path}/pulls".format(path=remote_url[15:-4])
    elif 'https://github.com/' in remote_url[:19]:
        uri = remote_url[19:-4] if '.git' in remote_url[19:] else remote_url[19:]
    else:
        uri = "https://github.com/{path}/pulls".format(path=uri)
    sys.stderr.write("opening url={uri}".format(uri=uri))
    try:
        args = shlex.split("open {uri}".format(uri=uri))
        p = subprocess.Popen(args, preexec_fn=os.setsid)
        exit(0)
    except Exception, exc:
        sys.stderr.write(exc.message)
        exit(1)
