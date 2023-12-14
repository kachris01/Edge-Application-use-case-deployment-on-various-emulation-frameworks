# Edge-Application-use-case-deployment-on-various-emulation-frameworks

Fog and Edge Computing have become crucial when it comes to connecting the gap between latency-sensitive applications and sensing devices. Despite its importance, testing IoT applications is still a huge task that requires the manual creation of extensive physical and virtual infrastructures with different resources and network requirements. This often results in insignificant implementation due to unexpected overheads. In order to address these issues, developers are relying on Fog and Edge Computing frameworks to rapidly create usage value using cloud-based technologies such as containers. This project aims to compare different Fog and Edge Computing frameworks such as Containernet and Marvis using pre-existing containerized applications.


## Prerequisites 
Your machine should run Ubuntu **20.04 LTS** and **Python3**.

Before starting, we have to install docker, docker-compose and docker swarm on the infrastructure. 
For more information, we suggest the official [documentation](https://docs.docker.com/).

You can test your docker installation with:
```sh
docker run hello-world
```

Furthermore, the system executes some low-level commands in order to apply specific characteristics to the network. 
For this reason, on each cluster of the swarm cluster, we should install the traffic control tool (tc-tool). 
On Debian-based destributions, tc-tool comes bundled with iproute, so in order to install it you have to run:

```bash
apt-get install iproute
```

You need a [working installation of docker](https://docs.docker.com/engine/install/ubuntu/). 

## Fogify-Demo
Preparing the demo application.

Move to fogify-demo-master/application directory
Run command

```sh
sudo sh ./build-image.sh
```
To run the taxi example in fogify, In directory fogify-demo-master/demo_files/ run command: 
```sh
docker-compose up
```

You need to download yellow_tripdata_2018-01.csv file and specify its path in fogify-demo-master/demo_files/docker-compose.yaml file line 7


## Marvis
Move to marvis-master directory and run the following command to start a Docker container:
```sh
docker run -it --rm --cap-add=ALL -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/examples:/marvisscenarios --net host --pid host --userns host --privileged ghcr.io/diselab/marvis:latest /bin/bash
```
To execute the application run inside the container:
```sh
cd marvisscenarios
python3 taxi.py
```

## Containernet
As we had problems with containernet installation option 1, we procude with option 2:
You can build the container locally:

```bash
docker build -t containernet/containernet .
```

or alternatively pull the latest pre-build container:

```bash
docker pull containernet/containernet
```

You can then start the containernet. You can change the volumes as needed with your files and directories:

```bash
docker run --name containernet -it --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock -v /home/$USER/Desktop/containernet/examples/basic_webserver/:/home/$USER/Desktop/containernet/examples/basic_webserver/ containernet/containernet bash
```

To execute the application run inside the container:
```sh
cd /home/$USER/Desktop/containernet/examples/basic_webserver
python3 taxi.py
```
If a problem like "Conflict ("Conflict. The container name "/mn.mec-svc-1" is already in use by container "ea841c6202383e85692417509cb4bd81a8c0161ae521742589d25b1f2d2aaed7". You have to remove (or rename) that container to be able to reuse that name."))" is occupied run the command: 
```sh
sudo mn -c
```
or
```sh
docker ps
docker stop <ids>
docker rm $(docker ps -a -q)
```
where <ids> are the ids of the containers we want to stop
