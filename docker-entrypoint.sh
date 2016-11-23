#!/bin/bash

if [ "$1" != "" ]; then
    exec "$@"
    exit
fi


# collect statics

exec gunicorn --bind 0.0.0.0:80  --log-level=debug ismynetworkalived.wsgi:application