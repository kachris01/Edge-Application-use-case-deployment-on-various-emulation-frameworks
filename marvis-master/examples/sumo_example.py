#!/usr/bin/env python3

from marvis import ArgumentParser, Network, DockerNode, Scenario, WiFiChannel
from marvis.mobility_input import SUMOMobilityInput


def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0", default_channel_type=WiFiChannel)

    edge_server = DockerNode('mec-svc-1', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"EDGE_NODE", "REGION":"bronx"}  ) 
    
    cloud_server = DockerNode('cloud-server', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"CLOUD_NODE"} ) 
    
    car = DockerNode('car-workload', docker_image="taxi-exp:0.0.1", environment_variables={"NODE_TYPE":"IOT_NODE"}, volumes={"/home/kchris01/data":"/data"})
    
    channel = net.create_channel(frequency=5860, channel_width=10, tx_power=18.0,
                                 standard=WiFiChannel.WiFiStandard.WIFI_802_11p,
                                 data_rate=WiFiChannel.WiFiDataRate.OFDM_RATE_BW_6Mbps)
    
    channel.connect(cloud_server)                             
                                 
    channel.connect(car)
    
    channel.connect(edge_server)
    
    

    scenario.add_network(net)

    sumo = SUMOMobilityInput(sumo_host='localhost', sumo_port=8000)
    sumo.add_node_to_mapping(edge_server, 'n0', obj_type='junction')
    sumo.add_node_to_mapping(cloud_server, 'n0', obj_type='junction')
    sumo.add_node_to_mapping(car, 'train')

    scenario.add_mobility_input(sumo)

    with scenario as sim:
        # To simulate forever, do not specify the simulation_time parameter.
        sim.simulate(simulation_time=30)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
