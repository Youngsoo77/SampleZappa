# Use this code snippet in your app.
import os

STAGE = os.getenv('STAGE', 'local')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_config(stage):
    debug = True if stage in ['local', 'dev', 'test'] else False
    if stage == "local":
        from configparser import RawConfigParser

        local_config = RawConfigParser()
        local_config.read(os.path.join(BASE_DIR, 'SampleZappa', 'local-settings.ini'), encoding='utf-8')

        _config = {
            'debug': debug,
            'secret_key': {
                'secret_key': local_config.get('base', 'SECRET_KEY'),
            },
            'db': {
                'name': local_config.get('db', 'NAME'),
                'host': local_config.get('db', 'HOST'),
                'password': local_config.get('db', 'PASSWORD'),
                'port': local_config.get('db', 'PORT'),
                'user': local_config.get('db', 'USER'),
            },
        }
    else:
        _config = None

    return _config


config = get_config(STAGE)
