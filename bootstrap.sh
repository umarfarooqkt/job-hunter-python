#!/bin/sh

export FLASK_APP='app.py'

pip install -r requirements.txt

flask run --host 0.0.0.0