# job-hunter-python
This is a newer version of job hunter application

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

One approach to testing the database is to use  monkey patching to replace the actual database with an in memory sql lite.

