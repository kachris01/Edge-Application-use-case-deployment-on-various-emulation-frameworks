# Marvis [![Github Actions CI](https://github.com/diselab/marvis/actions/workflows/main.yml/badge.svg)](https://github.com/diselab/marvis/actions/workflows/main.yml)

Marvis is a hybrid testbed for evaluating distributed IoT applications.
It can combine real hardware and virtualized nodes in a co-simulation, featuring the network simulator [ns-3](https://nsnam.org) and other domain-specific simulators (currently included is the traffic simulator [SUMO](https://sumo.dlr.de)).
For more information on the idea behind Marvis, please refer to our publication [Towards a Staging Environment for the Internet of Things](https://arxiv.org/pdf/2101.10697.pdf).

It is recommended to run Marvis using our pre-built docker image.
If you don't want to use the recommended setup, Marvis can also be installed directly on your machine and has so far been tested with **Debian 10 Buster**, **Ubuntu 18.04 Bionic Beaver**, and **Ubuntu 20.04 Focal Fossa**.


## Prerequisites 🤖

You need a [working installation of docker](https://docs.docker.com/engine/install/ubuntu/). You can test your docker installation with:
```sh
docker run hello-world
```

## Get Started 🌤

First download the project, for example, via git:

```sh
git clone https://github.com/diselab/marvis.git
cd marvis
```

To run Marvis, we recommend to use our pre-built docker image (if on Windows, exchange `$(pwd)` with `%cd%`):
```sh
docker run -it --rm --cap-add=ALL -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/examples:/marvisscenarios --net host --pid host --userns host --privileged ghcr.io/diselab/marvis:latest /bin/bash
```

Inside the container, you can now run the `basic_example.py`:

```sh
cd marvisscenarios
python3 basic_example.py
```

You should see two docker containers pinging each other. The ping should have a delay of ~400ms.

Now, have look at our [other examples](https://github.com/diselab/marvis/tree/master/examples)!


## Use Marvis with SUMO 🚗

To run Marvis with the SUMO traffic simulator, you first have to [install SUMO](https://sumo.dlr.de/docs/Installing/index.html) on the same host as Marvis.

If you run Marvis in the recommended docker setup, you have to start SUMO before Marvis via:

```sh
sumo-gui --remote-port 8813 -c examples/docker/sumo/sumo-scenario/scenario.sumocfg
```

(You can also use sumo without the GUI, just use the command `sumo`).
If you run Marvis locally on your machine, just provide the configuration path to the SUMO setup in your Marvis scenario. Marvis will start SUMO by itself.

To execute the example scenario run inside the container:

```sh
cd marvisscenarios
python3 sumo_example.py
```

## Citing Marvis 📖
If you use Marvis in your work, please cite our paper

**Towards a Staging Environment for the Internet of Things**. Jossekin Beilharz, Philipp Wiesner, Arne Boockmeyer, Florian Brokhausen, Ilja Behnke, Robert Schmid, Lukas Pirl, and Lauritz Thamsen. In the Proceedings of the *2021 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops)*. Presented in the Work in Progress (WiP) session of the conference. IEEE. 2021. [pdf](https://arxiv.org/pdf/2101.10697.pdf)

You can use the bibtex

```
@inproceedings{Beilharz2021_StagingEnvironmentIoT,
  author={Beilharz, Jossekin and Wiesner, Philipp and Boockmeyer, Arne and Brokhausen, Florian and Behnke, Ilja and Schmid, Robert and Pirl, Lukas and Thamsen, Lauritz},
  booktitle={2021 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops)}, 
  title={Towards a Staging Environment for the Internet of Things}, 
  year={2021},
  pages={312-315},
  doi={10.1109/PerComWorkshops51409.2021.9431087}
}
```


## Development & Contribution

We always welcome contributions or forks.
Please refer to our [CONTRIBUTING](https://github.com/diselab/marvis/blob/master/CONTIBRUTING.md) guide on how to develop and extend Marvis.


## Contributors

 - Malte Andersch
 - Felix Gohla
 - Martin Michaelis
 - Benedikt Schenkel
 - and the [diselab-Team](https://diselab.berlin)
