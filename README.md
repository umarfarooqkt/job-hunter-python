# job-hunter-python
This is a newer version of job hunter application

Job Hunter gathers open job listing from open source api's and stores them in a postgres database. A restful service on flask is launched to serve specific job applications.

This is a python version of my jobhunter application This version has some updated features with some cool explorations

System installations required:
- docker : containers
- kubectl : kubernetes api for cluster management
- python3.7

#### Kubernetes deployment
Running this application on a Kubernetes cluster is a bit of an overkill but if you want to...

- Deploy a kubernetes cluster (Google cloud is the preferred option), make sure your cluster has three or more nodes.
  This is because the deployment launches 2 or more replication. Let kubernetes have enough nodes to gain the full 
  advantage of those replications.
- Build the provided docker container (Projec Id refers to the gcloud project id)
   <p> $ docker build -t gcr.io/${PROJECT_ID}/main-app-four:v1 ./ </p>
- Push the container to a container registery, from the name you can tell I intend to use googles container registery
   <p> $ docker push gcr.io/${PROJECT_ID}/main-app-four:v1 </p>
- Create a deployement (Use the deployment.yaml)
   <p> $ kubectl create -f deployment.yaml </p>
- Now expose the deployment to the outside world, using the kubernetes load balancer
   <p> $ kubectl expose deployment job-hunter-app --type=LoadBalancer --port 80 --target-port 5000 </p>

There you go, you should have a kubernetes deployment at this point


#### Method 1 
Use the requirements.txt file if the pipenv does not work.

#### Method pipenv (deprecated)
- need to install pipenv globally before running the following command
more on pipenv https://realpython.com/pipenv-guide/
To Run using all the dependencies use $pipenv shell (to access the dependencies)

----

## Testing strategy

### Database

One approach to testing the database is to use monkey patching to replace the actual database dependencies.

Advantages: 
- Faster unit tests. 
- Can run anywhere without depending on a connection to a db or local db setup.
- Monkey patching really reduces the amount of work required for mocking.

Disadvantages:
- Too much monkey patching might reliability of tests.
- SQL logic dependable methods can't be accurately tested.
- Unit Tests should be as close to real world usage of methods in my opinion but monkey patching reduces that.

Second approach to testing is to use the real production ready database based unit tests. This is the primary types of tests I write in this project.
In my database manager I separate commits from database query based methods (this is a good practice anyways for example an error occurs somewhere in a request so a rollback might need to be done) this way I am able to test out methods and then roll them back, keeping them isolated.

Advantages:
- Testing really world usage of method. 
- In depth testing of SQL logic as well.
- Data integrity tests.
- Can catch more errors potentially, maybe even unrelated ones.

Disadvantages:
- Slower tests. 
- Might not be isolated.
- Need Internet connection or local database setup.
