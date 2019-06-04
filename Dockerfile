FROM python:3.7

# Installing packages
RUN apt-get update -y \
    && python -m pip install --user --upgrade pip

WORKDIR /usr/src/app
COPY bootstrap.sh requirements.txt ./
COPY service_manager ./
COPY data_gathering ./
COPY scripts ./

ENV DOCKER_ENV='True' \
    DB_HOST='0.0.0.0' \
    POSTGRES_PORT='5432'

CMD [ "python", "database_script.py" ]

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]