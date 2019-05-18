#! /bin/bash

var_user="root"
var_pass="root"

check_user=`grep -i 'export postgres_user' ~/.bashrc`
check_pass=`grep -i 'export postgres_pass' ~/.bashrc`

if [ -z "$check_user" ]; then
    echo "Not present, adding credentials"
    echo 'export postgres_user="root"' >> ~/.bashrc
    echo 'export postgres_pass="root"' >> ~/.bashrc
    echo 'export postgres_port="5432"' >> ~/.bashrc
    echo 'export db_host="localhost"' >> ~/.bashrc
else
    echo "The postgres database credentials were already set"
fi