# Marvis Contributing Guide

We always welcome contributions to Marvis.

When issuing a pull request, pease make sure:

- [`pylint`](https://www.pylint.org/) does not show any additional errors or warnings
- your code and pull request are well documented (including how to test your feature if it is more complex)


## Developig Marvis

This section is only relevant if you want to adapt or contribute to Marvis.

#### Develop Marvis within Docker

You first have to clone the Marvis repository:
```sh
git clone https://github.com/diselab/marvis.git
```

Then build the Marvis docker images:
```sh
cd marvis
sudo make
```

If you change any code, please make sure to run `sudo make` again to update the images.

Afterward, check the name and the tag of the image with:
```sh
sudo docker images
```
The tag will be some commit hash or `dirty` if you changed the code.

In the end, you can run your container:
```sh
sudo docker run -it --rm --cap-add=ALL -v /var/run/docker.sock:/var/run/docker.sock -v /absolute/path/to/your/marvis/scenario/folder:/marvisscenarios --net host --pid host --userns host --privileged ghcr.io/diselab/marvis:[your-tag]
```

And test the installation:
```sh
cd marvisscenarios
python3 your-scenario.py
```


### Develop Marvis without Docker

In the case, you want to run Marvis on your local machine, an [ns-3
installation](https://www.nsnam.org/wiki/Installation) with *NetAnim* Python bindings is necessary.

The following instructions describe how to install Marvis system-wide.
If you want to install Marvis for your user only (`pip3 install --user
…`), in a `virtualenv`, or in a `pipenv`, feel free to do so. However, we
won't cover instructions on how to get the `PYTHONPATH`/virtualenv/pipenv together with privilege escalation (sudo) working.

First, make sure you have the required packages to build dependencies
installed:

```shell script
apt install \
  build-essential \
  cargo \
  git \
  libssl-dev \
  python3-dev \
  python3-pip \
  python3-setuptools \
  python3-wheel \
  rustc
```

The recommended Python version is Python 3.7. Python 3.8 is right now not supported (if you are running Ubuntu 20.04, make sure to install Python 3.7).
Also, make sure you have pip3 version 21 or up
(if not, try `pip3 install --upgrade pip`).


#### User Installation

If you do not plan to modify the source code of Marvis yourself,
Marvis can be installed with the following command:

```shell script
# without ns-3
pip3 install git+https://github.com/diselab/marvis.git

# including ns-3
pip3 install 'git+https://github.com/diselab/marvis.git#egg=marvis[ns-3]'
```

The second of the commands above will use our
[Python Wheels repository](https://github.com/osmhpi/python-wheels)
for easier installation of binary dependencies, such as ns-3.

To run an example test case, download this repository, go to the example folder and run:
```shell script
python3 basic_example.py
```

#### Developer Installation

If you do plan to modify the source code of Marvis, clone this
repository and to install dependencies, run, e.g.:

```shell script
# without ns-3
pip3 install -e .

# including ns-3
pip3 install -e '.[ns-3]'

# including dev tools, if you want to contribute <3
pip3 install -e '.[dev]'

# including ns-3 and dev tools
pip3 install -e '.[ns-3,dev]'
```

In this case, where you do not install Marvis itself but just its
dependencies, the code of Marvis needs to be in your `PYTHONPATH`.
E.g.:

```shell script
export PYTHONPATH=$PYTHONPATH:$PWD/path/to/marvis-repo
```
