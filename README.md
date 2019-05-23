# job-hunter-python
This is a newer version of job hunter application

This is a python version of my jobhunter application This version has some updated features with some cool explorations

- need to install pipenv globally before running the following command
- will also need to install python3.7

#### Method 1
more on pipenv https://realpython.com/pipenv-guide/
To Run using all the dependencies use $pipenv shell (to access the dependencies)

#### Method 2 
Use the requirements.txt file if the pipenv does not work.

----

## Testing strategy

### Database

One approach to testing the database is to use  monkey patching to replace the actual database with an in memory sql lite.

