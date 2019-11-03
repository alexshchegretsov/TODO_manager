# -*- coding: utf-8 -*-

import multiprocessing
import os

bind = '0.0.0.0:' + os.environ.get('PORT', '8000')
max_requests = 1000
workers = (multiprocessing.cpu_count() * 2) + 1
env = {'DJANGO_SETTINGS_MODULE': 'todo_engine.settings'}
reload = True
