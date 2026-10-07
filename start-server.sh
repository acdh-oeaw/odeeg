#!/usr/bin/env bash
# start-server.sh
echo "Hello from ODEEG"

uv run manage.py collectstatic --no-input
uv run gunicorn odeeg.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"