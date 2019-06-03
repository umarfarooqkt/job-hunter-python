#! /bin/bash

var_user="root"
var_pass="root"

check_user=`grep 'export POSTGRES_USER' ~/.bashrc`
check_pass=`grep 'export POSTGRES_PASS' ~/.bashrc`

if [ -z "$check_user" ]; then
    echo "Not present, adding credentials"
    echo 'export POSTGRES_USER="root"' >> ~/.bashrc
    echo 'export POSTGRES_PASS="root"' >> ~/.bashrc
    echo 'export POSTGRES_PORT="5432"' >> ~/.bashrc
    echo 'export DB_HOST="localhost"' >> ~/.bashrc
else
    echo "The postgres database credentials were already set"
fi

# check_venv=`ls | grep venv`
# if [ -z "$check_venv" ]; then
#     virtualenv venv
# fi
# source venv/bin/activate
# pip install -r requirements.txt
# if [ -z "$FLASK_APP" ]; then
#     echo "Adding the flask app"
#     echo 'export FLASK_APP="app.py"' >> ~./bashrc
# fi 