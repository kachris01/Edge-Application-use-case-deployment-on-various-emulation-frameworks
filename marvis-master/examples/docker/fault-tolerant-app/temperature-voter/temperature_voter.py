#!/usr/bin/env python3


"""
prints ``SERVERS`` average temperature values every second (if possible)
"""

import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from struct import unpack
from time import sleep, monotonic
from multiprocessing import Pool

SERVERS = ('server_a', 'server_b')
CHECK_INTERVAL = 1

def get_temperature(sock):
  """
  requests temperature from :param:``sock``; returns ``None`` on error
  """
  try:
    sock.sendall(b'temp')
    return unpack('f', sock.recv(8))[0]
  except:
    print('warning: could not get data from', sock.getpeername())
    return None

def main():

  # create a socket per temperature server
  socks = tuple(socket(AF_INET, SOCK_DGRAM) for _ in SERVERS)
  for host_name, sock in zip(SERVERS, socks):
    sock.settimeout(CHECK_INTERVAL)
    sock.connect((gethostbyname(host_name), 4242))

  # create a Process pool for requesting temperatures in parallel
  pool_map = Pool(len(socks)).map

  next_check = monotonic()
  while True:
    temperatures = [temperature
                    for temperature in pool_map(get_temperature, socks)
                    if temperature is not None]
    try:
      print('avg:', sum(temperatures)/len(temperatures))
    except ZeroDivisionError:
      print('error: could not get any temperature values')
    finally:
      next_check += CHECK_INTERVAL
      sleep(max(0, next_check - monotonic()))

if __name__ == '__main__':
  main()
