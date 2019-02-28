#!/bin/bash
echo 122
pipenv run gunicorn --daemon -b "0.0.0.0:19228" app.api.server222:api --reload
echo 333
echo curl GET -X localhost:19228/meta