"""
Template to create config.py file.
Do not add 'config.py' to SCM.
"""

import os
from celery.schedules import crontab


_basedir = os.path.abspath(os.path.dirname(__file__))

MHN_SERVER_HOME = _basedir

# Local settings.
DEBUG = True
SECRET_KEY = 'sXCtq1n88awl8GMXeCkGz1A8oz7QiChC'
SUPERUSER_EMAIL = 'snehal-govind.jambare@epita.fr'
SUPERUSER_PASSWORD = 'kali'
SERVER_BASE_URL = '111.111.111.125'
HONEYMAP_URL = '111.111.111.125:3000'
DEPLOY_KEY = 'H99aKziW'
LOG_FILE_PATH = '/var/log/mhn/mhn.log'

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
DEFAULT_MAIL_SENDER = ''
MAIL_DEBUG = DEBUG

# Other settings.
FEED_AUTH_REQUIRED = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'mhn.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_LOGIN_URL = '/ui/login/'
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = BROKER_URL
RENDERED_RULES_PATH = os.path.join(_basedir, 'mhn/static/mhn.rules')
CELERYBEAT_SCHEDULE = {
    'fetch-emerging-rules': {
            'task': 'mhn.tasks.rules.fetch_sources',
            'schedule': crontab(hour=12),
            'args': ()
    }
}
SNORT_RULES_SOURCE = {
    'name': 'Emerging Threats',
    'uri': 'https://rules.emergingthreats.net/open/snort-2.9.0/emerging.rules.tar.gz'
}
HONEYPOT_CHANNELS = {
    'dionaea': [
        'mwbinary.dionaea.sensorunique',
        'dionaea.capture',
        'dionaea.capture.anon',
        'dionaea.caputres',
        'dionaea.connections'
    ],
    'conpot': ['conpot.events'],
    'snort': ['snort.alerts'],
    'kippo': ['kippo.sessions'],
    'cowrie': ['cowrie.sessions'],
    'thug': ['thug.files', 'thug.events'],
    'glastopf': ['glastopf.files', 'glastopf.events'],
    'amun': ['amun.events'],
    'wordpot': ['wordpot.events'],
    'shockpot': ['shockpot.events'],
    'p0f': ['p0f.events'],
    'suricata': ['suricata.events'],
    'elastichoney': ['elastichoney.events'],
    'drupot': ['drupot.events'],
    'agave': ['agave.events'],
}
