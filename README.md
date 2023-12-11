# Edge-Application-use-case-deployment-on-various-emulation-frameworks

Fog and Edge Computing have become crucial when it comes to connecting the gap between latency-sensitive applications and sensing devices. Despite its importance, testing IoT applications is still a huge task that requires the manual creation of extensive physical and virtual infrastructures with different resources and network requirements. This often results in insignificant implementation due to unexpected overheads. In order to address these issues, developers are relying on Fog and Edge Computing frameworks to rapidly create usage value using cloud-based technologies such as containers. This project aims to compare different Fog and Edge Computing frameworks such as Containernet and Marvis using pre-existing containerized applications.


## Prerequisites 
Your machine should run Ubuntu **20.04 LTS** and **Python3**.

You need a [working installation of docker](https://docs.docker.com/engine/install/ubuntu/). You can test your docker installation with:
```sh
docker run hello-world
```

## Fogify-Demo





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
