#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2013, Mehmet Nuri ÖZTÜRK <mnozturk2@gmail.com>
# Please read the COPYING file.
#

from distutils.core import setup
datas = [("/usr/share/pixmaps", ["icons/padi.png"]), ('share/applications', ['data/padi.desktop'])]

setup(name = "padi",
    version = "0.1",
    description = "Pardus Alternative Desktop Installer",
    author = "Mehmet Nuri Öztürk",
    author_email = "mnozturk2@gmail.com",
    url = "https://github.com/mehmetnuriozturk/Padi",
    packages = ["padi"],
    data_files = datas,
    scripts = ["data/padi"])

