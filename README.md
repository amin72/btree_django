# BTree Project

BTree is a property searching system, helps you to look homes and make inquiries to realtors.


## settings

Required settings must be put into settings.ini located at btree/btree/config/

Bellow we list required settings which must be include in settings.ini.
Be sure to change values.

### database setting:
[database]
DATABASE_USER: btree
DATABASE_PASSWORD: testpassword
DATABASE_HOST: localhost
DATABASE_PORT:
DATABASE_ENGINE: django.db.backends.postgresql
DATABASE_NAME: btree_db

### DEBUG setting:
[debug]
DEBUG=False

### ALLOWED_HOSTS settings:
[hosts]
ALLOWED_HOSTS=127.0.0.1, btreeproject.com

ALLOWED_HOSTS is required if only DEBUG is set to False.
