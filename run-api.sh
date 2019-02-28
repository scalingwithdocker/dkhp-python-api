#!/bin/bash
pipenv run  gunicorn -b "0.0.0.0:19228"  app.api.server:api --reload