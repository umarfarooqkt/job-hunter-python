FROM python:3.7

# Installing packages
RUN apt-get update -y \
    && python -m pip install --user --upgrade pip

WORKDIR /usr/src/app
COPY bootstrap.sh requirements.txt ./
COPY service_manager/app.py ./
COPY data_gathering ./

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]