from marvis import ArgumentParser, Network, DockerNode, SwitchNode, Scenario


def main():
    scenario = Scenario()
    
    net = Network("10.0.0.0", "255.255.255.0")
    
    switch1 = SwitchNode('switch-1')
    switch2 = SwitchNode('switch-2')
    switch3 = SwitchNode('switch-3')
    
    edge = DockerNode('mec-svc-1', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"EDGE_NODE", "REGION":"bronx"}  ) 
    
    cloud = DockerNode('cloud-server', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"CLOUD_NODE"} ) 
    
    car = DockerNode('car-workload', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"IOT_NODE"}, volumes={"/home/kchris01/data":"/data"})
    
    channel1 = net.create_channel()
    channel1.connect(car)
    channel1.connect(switch1)

    channel2 = net.create_channel(delay="20ms")
    channel2.connect(switch1)
    channel2.connect(switch2)
    
    channel3 = net.create_channel()
    channel3.connect(edge)
    channel3.connect(switch2)
    
    channel4 = net.create_channel(delay="200ms")
    channel4.connect(switch2)
    channel4.connect(switch3)
    
    channel5 = net.create_channel()
    channel5.connect(switch3)
    channel5.connect(cloud)

    scenario.add_network(net)
   
    with scenario as sim:
        # To simulate forever, do not specify the simulation_time parameter.
        sim.simulate(simulation_time=60)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
