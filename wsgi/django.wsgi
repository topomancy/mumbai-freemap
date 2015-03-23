# django.wsgi for chaloBEST
import os
import sys
#import site
 
project_module = 'geobombay'

root_dir = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(__file__)), '..'))

#using virtualenv's activate_this.py to reorder sys.path
activate_this = os.path.join(root_dir, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.append(root_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = project_module + '.settings'
#reload if this django.wsgi gets touched
#from ox.django import monitor
#monitor.start(interval=1.0)

#monitor.track(os.path.abspath(os.path.dirname(__file__)))
 
import django.core.handlers.wsgi
 
application = django.core.handlers.wsgi.WSGIHandler()
