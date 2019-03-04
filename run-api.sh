#!/bin/bash
echo curl -X GET http://localhost:19228/meta
pipenv run  gunicorn -b "0.0.0.0:19228"  app.api.server:api --reload