from logging import getLogger

from marvis import ArgumentParser, Network, DockerNode, Scenario

def main():

    logger = getLogger('scenario')

    scenario = Scenario()

    net = Network('10.0.0.0', '255.255.255.0', base='0.0.0.2')
    net.block_ip_address('10.0.0.1')
    channel = net.create_channel()

    server_a = DockerNode('server_a',
        docker_build_dir='./docker/fault-tolerant-app/temperature-server')
    channel.connect(server_a)

    server_b = DockerNode('server_b',
        docker_build_dir='./docker/fault-tolerant-app/temperature-server')
    channel.connect(server_b)

    voter = DockerNode('voter',
        docker_build_dir='./docker/fault-tolerant-app/temperature-voter')
    channel.connect(voter)

    scenario.add_network(net)

    @scenario.workflow
    def on_and_off(workflow):

        # disconnect servers intermittently
        workflow.sleep(5)
        logger.info('disconnecting temperature server a')
        server_a.go_offline()
        workflow.sleep(5)
        logger.info('disconnecting temperature server b')
        server_b.go_offline()
        workflow.sleep(5)
        logger.info('reconnecting temperature servers')
        server_a.go_online()
        server_b.go_online()

        # introduce a network delay
        workflow.sleep(5)
        logger.info('setting network delay higher than check interval')
        channel.set_delay("1100ms")
        workflow.sleep(5)
        logger.info('removing network delay')
        channel.set_delay("0ms")

    with scenario as sim:
        sim.simulate(simulation_time=30)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
