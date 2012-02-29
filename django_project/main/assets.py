#!/usr/bin/env python
# encoding: UTF-8

from django_assets import env as environment

environment.register('index_sass', 'styles/index.sass', filters='sass', output='styles/index.css')
environment.register('global_js', 'javascripts/global.js', filters='rjsmin', output='javascripts/global_min.js')
