#!/bin/sh

export FLASK_APP='app.py'

pip install -r requirements.txt

if [ "${DOCKER_ENV}" = 'True' ]; then
    python data_miner.py &
fi

flask run --host 0.0.0.0