from time import sleep

import requests
import os
def get_random_metrics(data_size=10, filesize=1000000, file="/data/yellow_tripdata_2018-01.csv"):
    import random
    data = []
    f = open(file, "r")

    offset = random.randrange(filesize)
    f.seek(offset)  # go to random position


    for i in range(0,data_size):
        f.readline()  # discard - bound to be partial line
        random_line = f.readline()
        data+=[random_line]

    f.close()
    return data
service_to_network = {
'mec-svc-1': 'edge-net-1', 'mec-svc-2': 'edge-net-2'
}
  
  
def propagate_to_edge(data):
    sent = False
    for fog_node in ['mec-svc-1']:
        try:
            requests.post("http://%s:8000/"%fog_node, data=str(data), timeout=10)
            sent = True
            print(str(data))
            break
        except:
            continue
    if not sent:
        try:
            requests.post("http://cloud-server:8000/", data=str(data))
        except Exception as e:
            print(e)
            print(str(data))
            # sleep(5)
            # propagate(data=data)

def propagate(data):
    try:
        requests.post("http://cloud-server:8000/", data=str(data))
    except Exception as e:
        print(e)
        print("data is lost2")
        sleep(5)
        propagate(data=data)
