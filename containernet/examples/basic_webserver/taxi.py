#!/usr/bin/python
"""
This is an example how to simulate a client server environment.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

setLogLevel('info')

net = Containernet(controller=Controller)
net.addController('c0')

info('*** Adding server and client container\n')
edge_server = net.addDocker('mec', ip='10.0.0.253',  dimage="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"EDGE_NODE", "REGION":"bronx"} )

cloud_server = net.addDocker('cloud', ip='10.0.0.251', dimage="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"CLOUD_NODE"})

car = net.addDocker('car', ip='10.0.0.252', dimage="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"IOT_NODE"})


info('*** Setup network\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')


net.addLink(car, s1)
net.addLink(s1, s2, cls=TCLink, delay='20ms', bw=1)
net.addLink(s2, edge_server)
net.addLink(s2, s3, cls=TCLink, delay='200ms', bw=1)
net.addLink(s3, cloud_server)

net.start()

#info('*** Starting to execute commands\n')

#info('Execute: client.cmd("time curl 10.0.0.251")\n')
#info(car.cmd("time curl 10.0.0.251") + "\n")

#info('Execute: client.cmd("time curl 10.0.0.251/hello/42")\n')
#info(car.cmd("time curl 10.0.0.251/hello/42") + "\n")

CLI(net)

net.stop()
