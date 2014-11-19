#! /usr/bin/env python
#-*- coding: utf-8 -*-

import os, yaml 
from TutsplusDownloader import Tutsplus

if os.path.exists("local.yaml"):
    filename = "local.yaml"
else:
    filename = "config.yaml"

stream = open(filename, 'r')
config = yaml.load(stream)

t = Tutsplus(config)
